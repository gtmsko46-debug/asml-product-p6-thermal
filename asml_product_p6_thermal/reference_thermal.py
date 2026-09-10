"""SEED thermal overlay — mirrors labs/th-04-reticle-heat/solver.py weak baseline."""
from __future__ import annotations

THERMAL_COEF = 0.05  # nm per absorbed duty unit; learn upward in harness


def predict_overlay(lot: dict) -> list[float]:
    duty = float(lot["duty_cycle"])
    exposure = float(lot.get("exposure_s", 1.0))
    refl = float(lot.get("reticle_reflectivity", 0.9))
    absorbed = duty * exposure * (1.0 - refl)
    base = THERMAL_COEF * absorbed
    n = int(lot.get("n_dies", 16))
    out = []
    for i in range(n):
        r = (i + 1) / n
        out.append(base * (0.7 + 0.3 * r))
    return out
