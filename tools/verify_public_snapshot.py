"""Check the published solver identities and optional synthetic candidate generation.

No model calls, private inputs, Lean judge, or organizer score are exercised.
"""
import argparse
import ast
import hashlib
import json
from pathlib import Path
import runpy

ROOT = Path(__file__).resolve().parents[1]


def verify(root=ROOT, replay=False):
    manifest = json.loads((root / 'public-snapshot.json').read_text(encoding='utf-8'))
    results = []
    for item in manifest['artifacts']:
        path = root / item['path']
        if path.resolve().parent.parent != (root / 'dist/final').resolve():
            raise ValueError('Unexpected solver path')
        raw = path.read_bytes()
        if len(raw) != item['bytes'] or hashlib.sha256(raw).hexdigest() != item['sha256']:
            raise ValueError('Frozen solver identity mismatch: ' + item['path'])
        ast.parse(raw, filename=item['path'])
        row = {'path': item['path'], 'sha256': item['sha256'], 'identity': 'PASS'}
        if replay:
            module = runpy.run_path(str(path), run_name='public_snapshot_check')
            reflexive = module['reflexive_proof']('x * y = x * y')
            direct = module['direct_substitution_proof']('x = y', 'x = y')
            if reflexive != 'intro x y\nrfl' or direct != 'intro x y\nexact hyp x y':
                raise ValueError('Synthetic candidate changed: ' + item['path'])
            if module['reflexive_proof']('x = y') is not None:
                raise ValueError('Non-reflexive equation accepted as reflexive')
            code = module['make_true_code'](reflexive)
            if code != module['make_true_code'](module['reflexive_proof']('x * y = x * y')):
                raise ValueError('Synthetic generation is not repeatable')
            row.update(candidate_replay='PASS', candidate_sha256=hashlib.sha256(code.encode()).hexdigest())
        results.append(row)
    return {'status': 'PASS', 'artifacts': results,
            'scope': 'Published bytes and synthetic candidate generation only; Lean acceptance and competition scores are NOT_CHECKED.'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--replay-candidates', action='store_true')
    args = parser.parse_args()
    print(json.dumps(verify(replay=args.replay_candidates), indent=2))
