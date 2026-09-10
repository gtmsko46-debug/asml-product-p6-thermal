# asml-product-p6-thermal

**Optic / first-mirror thermal survival under shared-source load — decide inherit TH-04 reticle-heat KEEP eval vs separate product holdout.**

| | |
|--|--|
| Spec | [`SPEC.md`](SPEC.md) · asml-bench [#49](https://github.com/gtmsko46-debug/asml-bench/issues/49) |
| Factory | [FACTORY.md](https://github.com/gtmsko46-debug/asml-bench/blob/main/products/FACTORY.md) |
| Stage | **Spec (M0)** — package/build waits bay |

```bash
# after M1
pip install -e '.[dev]'
```

Sandbox hill-climbs live on asml-bench (`inherit labs/th-04-reticle-heat/solver.py OR labs/p6-thermal/solver.py`); set `ASML_BENCH_ROOT` to pick up live weights once the loader exists.
