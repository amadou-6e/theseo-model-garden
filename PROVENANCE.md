# Source provenance

The initial inference slice is copied from
`amadou-6e/theseo-anysearch@88e220ccdbca8c87c56875b5d742427eb7947540`
under `theseo_anysearch/garden/`. Source module names are mapped to
`src/theseo_model_garden/` with the same relative filenames.

Adaptations are limited to namespace replacement, removal of import-time
registry mutation from the package initializer, and extraction of the
canonical payload and encoder-state hashes into `artifacts.py` so inference
does not import pilot contracts or evaluation dependencies. The hash
algorithms, compact contract constants, shapes, and loader checks are
unchanged. The pinned round-trip tests were copied from
`tests/test_garden/test_compact_package.py` with only import names changed.

The remaining source modules and the AnySearch consumer have **not** moved.
This is an intentionally staged extraction, not a wholesale promotion of
`exp/perception-encoder` into `develop`.
