# Theseo Model Garden

Standalone voxel-encoder inference and artifact contracts, extracted from the
Theseo AnySearch perception-encoder experiment line. This repository is being
staged; its first change is an inference-only slice, not a release or a claim
that the experimental encoder is qualified for production use.

Source: `amadou-6e/theseo-anysearch` commit
`88e220ccdbca8c87c56875b5d742427eb7947540`, path
`theseo_anysearch/garden/`. Extraction tracker:
[theseo-anysearch #501](https://github.com/amadou-6e/theseo-anysearch/issues/501).

The compact artifact format remains `compact-spatial-code-v1`; its embedded
status is `experimental` and `promotion_eligible` is `false`. Use
`theseo_model_garden.compact_package.load_compact_package(path)` to load an
existing checked package. No model weights or raw experiment stores are in
this repository.

Installing this package for inference does not install AnySearch, Ray, RLlib,
or the native environment runtime. Training, collection, registry, tuning,
the garden CLI, historical pilot scripts, and the AnySearch policy adapter
remain in the source repository until separate migration PRs are reviewed.

Run `python -m pytest tests` for the artifact round-trip and integrity checks.
