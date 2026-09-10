from __future__ import annotations
from dataclasses import asdict, dataclass
from typing import Any, Mapping, Sequence
from .loader import get_predict

ASSUMPTION_CARD = "reticle-heat-v1"
INHERIT_NOTE = "SEED inherits TH-04 solver shape; Spec #49 decide inherit holdout XOR new EI HOLDOUT."

@dataclass
class ThermalReport:
    overlay_nm: list[float]
    mean_abs_nm: float
    n_dies: int
    assumption_card_id: str = ASSUMPTION_CARD
    inherit_note: str = INHERIT_NOTE
    solver_source: str = "reference"
    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

def thermal_overlay(lot: Mapping[str, Any]) -> ThermalReport:
    if "duty_cycle" not in lot:
        raise KeyError("missing required field: duty_cycle")
    source, fn = get_predict()
    vec = [float(x) for x in fn(dict(lot))]
    mean_abs = sum(abs(x) for x in vec) / max(len(vec), 1)
    return ThermalReport(
        overlay_nm=vec,
        mean_abs_nm=float(mean_abs),
        n_dies=len(vec),
        solver_source=source,
    )
