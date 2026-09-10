# asml-product-p6-thermal — Product Spec (M0)

**Parent:** asml-bench [#49](https://github.com/gtmsko46-debug/asml-bench/issues/49)  
**Stage:** Spec → Build → Review → Ship  
**Rule:** Bots orchestrate; all *solver/sandbox* code via lasercode (Foreman→Operator). Docs/spec PRs OK offline.

## Champion job
Optic / first-mirror thermal survival under shared-source load — decide inherit TH-04 reticle-heat KEEP eval vs separate product holdout.

## Public API (target)
```python
from asml_product_p6_thermal import thermal_overlay
report = thermal_overlay(dose=..., throughput=..., optic_state=...)
```

## Lab bind
| Field | Value |
|-------|-------|
| Sandbox | `inherit labs/th-04-reticle-heat/solver.py OR labs/p6-thermal/solver.py` |
| Frozen eval | Decision required in Spec close: inherit TH-04 holdout XOR new product HOLDOUT (EI) |
| Assumption card | `reticle-heat-v1 or p6-thermal-v1` |
| Dual-gate | dual-gate; if inherit TH-04, cite research KEEP IDs explicitly |
| HOLDOUT | pin when EI freezes product holdout (no eval edits by solvers) |

## KEEP / promote bar
- Dual-provider KEEP on same frozen eval + digest
- Critic clear (no oracle / metric reuse)
- Repro Bot clean-tree PASS
- Diplomat dual stamp before product `reference_*` sync

## Must not
- Edit `eval.py` / `fixture/*` from solver tickets
- Ship single-provider KEEP as product baseline
- Claim fab-grounded numbers (synthetic cards only)

## Milestones
1. **M0 Spec** — this document + README champion job (this PR)
2. **M1 Package** — importable module + SEED `reference_*` + tests
3. **M2 Dual-gate** — HT pair via Foreman; Critic+Repro+Diplomat
4. **M3 Ship** — `reference_*` sync + ship-queue Issue close

## Bay
Queued behind P1 deepen / P2 HT-1023/1024 unless CoS assigns spare Operator. Spec/docs do not steal bay.
