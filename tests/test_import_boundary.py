"""A clean inference import must not initialize the host or training stack."""

import subprocess
import sys
import os
from pathlib import Path


def test_compact_inference_import_is_host_independent():
    script = """
import sys
from theseo_model_garden.compact_package import CONTRACT, empty_encoder
assert CONTRACT['format'] == 'compact-spatial-code-v1'
assert CONTRACT['promotion_eligible'] is False
assert empty_encoder().output_dim == 729
for forbidden in ('theseo_anysearch', 'ray', 'pydantic', 'scipy', 'sklearn'):
    assert forbidden not in sys.modules, forbidden
"""
    env = dict(os.environ)
    env["PYTHONPATH"] = str(Path(__file__).resolve().parents[1] / "src")
    result = subprocess.run([sys.executable, "-c", script], capture_output=True, text=True, check=False, env=env)
    assert result.returncode == 0, result.stderr
