"""A clean inference import must not initialize the host or training stack."""

import subprocess
import sys


def test_compact_inference_import_is_host_independent():
    script = """
import sys
from pathlib import Path
import theseo_model_garden
from theseo_model_garden.compact_package import CONTRACT, empty_encoder
assert not Path(theseo_model_garden.__file__).resolve().is_relative_to(Path.cwd() / 'src')
assert CONTRACT['format'] == 'compact-spatial-code-v1'
assert CONTRACT['promotion_eligible'] is False
assert empty_encoder().output_dim == 729
for forbidden in ('theseo_anysearch', 'ray', 'pydantic', 'scipy', 'sklearn'):
    assert forbidden not in sys.modules, forbidden
"""
    result = subprocess.run([sys.executable, "-c", script], capture_output=True, text=True, check=False)
    assert result.returncode == 0, result.stderr
