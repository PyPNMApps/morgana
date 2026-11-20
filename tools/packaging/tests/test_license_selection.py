# Copyright 2026 MORGANA contributors
# SPDX-License-Identifier: Apache-2.0
"""Fail closed on new license expressions and retain required extra obligations."""
import importlib.util
from pathlib import Path
import unittest

spec=importlib.util.spec_from_file_location("notices",Path(__file__).resolve().parents[2]/"python/notices.py")
notices=importlib.util.module_from_spec(spec)
spec.loader.exec_module(notices)

class LicenseSelectionTests(unittest.TestCase):
    def test_choices_preserve_conjunctions_and_unknown_terms_stop_review(self):
        """Exact reviewed alternatives are selected; additional terms never vanish."""
        self.assertEqual(notices.selected_license("MIT OR Apache-2.0 OR LGPL-2.1-or-later"),"Apache-2.0")
        self.assertEqual(notices.selected_license("(MIT OR Apache-2.0) AND Unicode-3.0"),"Apache-2.0 AND Unicode-3.0")
        self.assertEqual(notices.selected_license("Apache-2.0 WITH LLVM-exception"),"Apache-2.0 WITH LLVM-exception")
        with self.assertRaises(ValueError):notices.selected_license("Apache-2.0 AND UNKNOWN")
