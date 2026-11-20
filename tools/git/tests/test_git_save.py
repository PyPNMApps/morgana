# Copyright 2026 MORGANA contributors
# SPDX-License-Identifier: Apache-2.0
"""Exercise save guards in disposable repositories, never the user's Git history."""
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[3]
MESSAGE = "Feature: Preserve test checkpoint\n- Include reviewed work\n- Tests: Isolated gate passes"


class SaveTests(unittest.TestCase):
    """Own temporary Git state for each local helper contract test."""

    def setUp(self) -> None:
        """Create an isolated root with local identity and a controlled no-op gate."""
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        (self.root / "tools/git").mkdir(parents=True)
        (self.root / "scripts").mkdir()
        shutil.copyfile(ROOT / "tools/git/git-save.sh", self.root / "tools/git/git-save.sh")
        self.gate = self.root / "scripts/validate.sh"
        self.gate.write_text("#!/usr/bin/env bash\nexit 0\n")
        self.git("init", "-q", "-b", "master")
        self.git("config", "user.name", "Isolated Test")
        self.git("config", "user.email", "test@example.invalid")

    def git(self, *arguments: str) -> subprocess.CompletedProcess[str]:
        """Run literal Git arguments in this temporary repository; fail on error."""
        return subprocess.run(["git", *arguments], cwd=self.root, text=True,
                              capture_output=True, check=True, timeout=10)

    def save(self) -> subprocess.CompletedProcess[str]:
        """Invoke the copied save helper without touching an external repository."""
        return subprocess.run(["bash", "tools/git/git-save.sh", "--commit-msg", MESSAGE],
                              cwd=self.root, text=True, capture_output=True, timeout=15)

    def test_initial_save_includes_unstaged_staged_and_symlink(self) -> None:
        """Initial save includes all reviewed files, preserves links and ignores local data."""
        (self.root / ".gitignore").write_text("local/\n")
        (self.root / "local").mkdir()
        (self.root / "local/private.txt").write_text("private fixture\n")
        (self.root / "staged.txt").write_text("staged\n")
        self.git("add", "staged.txt")
        (self.root / "unstaged.txt").write_text("new\n")
        (self.root / "link").symlink_to("unstaged.txt")
        result = self.save()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(self.git("status", "--porcelain").stdout, "")
        files = self.git("ls-tree", "-r", "--name-only", "HEAD").stdout.splitlines()
        self.assertIn("staged.txt", files)
        self.assertIn("unstaged.txt", files)
        self.assertNotIn("local/private.txt", files)
        self.assertIn("120000", self.git("ls-tree", "HEAD", "link").stdout)
        self.assertEqual(self.git("log", "-1", "--format=%B").stdout.rstrip(), MESSAGE)
        self.assertEqual(self.git("remote").stdout, "")
        self.assertEqual(self.git("tag").stdout, "")

    def test_gate_failure_keeps_candidate_without_commit(self) -> None:
        """A failed gate retains staged work and creates no commit."""
        self.gate.write_text("exit 7\n")
        (self.root / "payload").write_text("keep\n")
        self.assertNotEqual(self.save().returncode, 0)
        self.assertIn("payload", self.git("diff", "--cached", "--name-only").stdout)
        self.assertFalse((self.root / ".git/refs/heads/master").exists())

    def test_gate_index_change_is_rejected(self) -> None:
        """A gate that stages additional content cannot commit a changed candidate."""
        self.gate.write_text("echo changed > injected\ngit add injected\n")
        result = self.save()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("staged candidate changed", result.stderr)
        self.assertFalse((self.root / ".git/refs/heads/master").exists())

    def test_gate_worktree_change_is_rejected(self) -> None:
        """Unstaged gate changes remain available and stop the commit."""
        self.gate.write_text("echo changed > injected\n")
        result = self.save()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Working files changed", result.stderr)
        self.assertTrue((self.root / "injected").exists())

    def test_empty_second_save_is_rejected(self) -> None:
        """A clean checkpoint cannot produce an empty follow-up commit."""
        self.assertEqual(self.save().returncode, 0)
        head = self.git("rev-parse", "HEAD").stdout
        self.assertNotEqual(self.save().returncode, 0)
        self.assertEqual(self.git("rev-parse", "HEAD").stdout, head)


if __name__ == "__main__":
    unittest.main()
