# Copyright 2026 MORGANA contributors
# SPDX-License-Identifier: Apache-2.0
"""Scientific package boundaries, attribution, integrity and export ownership."""
import importlib.util
from pathlib import Path
import subprocess
import tarfile
import tempfile
import unittest
from unittest.mock import patch

SCRIPT=Path(__file__).resolve().parents[1]/"source_bundle.py"
spec=importlib.util.spec_from_file_location("source_bundle",SCRIPT)
bundle=importlib.util.module_from_spec(spec)
spec.loader.exec_module(bundle)

class SourceBundleTests(unittest.TestCase):
    def setUp(self) -> None:
        """Create an isolated Git candidate with science and excluded private paths."""
        self.temporary=tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root=Path(self.temporary.name)
        subprocess.run(["git","init","-q",str(self.root)],check=True)
        self.scope=patch.object(bundle,"ROOT",self.root);self.scope.start();self.addCleanup(self.scope.stop)
        for name in bundle.FILES | {"crates/phy/src/lib.rs","examples/reference.json","skills/private/SKILL.md","docs/development/local/private.txt"}:
            target=self.root/name;target.parent.mkdir(parents=True,exist_ok=True);target.write_text("source\n")
        (self.root/"VERSION").write_text("0.1.0\n")

    def test_archive_inventory_licenses_and_private_exclusion(self):
        """Actual generated archive has exact reviewed content and excludes guidance."""
        target=self.root/"target/source-packages/test.tar.gz"
        digest,count=bundle.build(target)
        self.assertEqual(len(digest),64)
        with tarfile.open(target) as archive:
            names=archive.getnames();self.assertEqual(len(names),count)
            self.assertIn("morgana-0.1.0/LICENSE",names)
            self.assertIn("morgana-0.1.0/NOTICE",names)
            self.assertIn("morgana-0.1.0/SOURCE-MANIFEST.json",names)
            self.assertFalse(any("skills/" in n or "private" in n for n in names))
        with self.assertRaises(ValueError):bundle.build(target)

    def test_redirected_input_and_export_and_missing_required_inputs_reject(self):
        """Do not follow source/output symlinks or export an incomplete package."""
        target=self.root/"target/source-packages/test.tar.gz"
        (self.root/"LICENSE").unlink()
        with self.assertRaises(ValueError):bundle.build(target)
        (self.root/"LICENSE").symlink_to("NOTICE")
        with self.assertRaises(ValueError):bundle.build(target)
        with self.assertRaises(ValueError):bundle.build(self.root/"external.tar.gz")
