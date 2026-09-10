"""Ensure the public identity gate fails on modified solver bytes."""
import json
from pathlib import Path
import shutil
import tempfile
import unittest

from verify_public_snapshot import ROOT, verify


class SnapshotTests(unittest.TestCase):
    def test_frozen_candidates(self):
        self.assertEqual(len(verify(replay=True)['artifacts']), 4)

    def test_changed_bytes_fail(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            shutil.copyfile(ROOT / 'public-snapshot.json', root / 'public-snapshot.json')
            manifest = json.loads((root / 'public-snapshot.json').read_text())
            first = manifest['artifacts'][0]['path']
            (root / first).parent.mkdir(parents=True)
            (root / first).write_bytes((ROOT / first).read_bytes() + b'\n')
            with self.assertRaisesRegex(ValueError, 'identity mismatch'):
                verify(root)


if __name__ == '__main__':
    unittest.main()
