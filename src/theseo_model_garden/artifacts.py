"""Canonical integrity helpers shared by inference and optional training tools."""

from __future__ import annotations

import hashlib
import json
from typing import Any

import torch
from torch import nn


def payload_sha256(payload: Any) -> str:
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":"),
                         ensure_ascii=True, allow_nan=False).encode("ascii")
    return hashlib.sha256(encoded).hexdigest()


def encoder_state_sha256(module: nn.Module) -> str:
    """Hash parameters and buffers without dtype-dependent serialization."""
    digest = hashlib.sha256()
    for name, tensor in sorted(module.state_dict().items()):
        value = tensor.detach().cpu().contiguous()
        header = {"name": name, "shape": list(value.shape), "dtype": str(value.dtype)}
        digest.update(json.dumps(header, sort_keys=True, separators=(",", ":")).encode("ascii"))
        digest.update(value.reshape(-1).view(torch.uint8).numpy().tobytes(order="C"))
    return digest.hexdigest()
