from __future__ import annotations
import importlib.util, os, sys
from pathlib import Path
from types import ModuleType
from typing import Callable
from . import reference_thermal

PredictFn = Callable[[dict], list]
_CACHED: tuple[str, PredictFn] | None = None

def _load(path: Path) -> ModuleType:
    spec = importlib.util.spec_from_file_location("asml_p6_thermal_sandbox", path)
    if spec is None or spec.loader is None:
        raise ImportError(str(path))
    mod = importlib.util.module_from_spec(spec)
    sys.modules["asml_p6_thermal_sandbox"] = mod
    spec.loader.exec_module(mod)
    return mod

def get_predict(*, force_reload: bool = False) -> tuple[str, PredictFn]:
    global _CACHED
    if _CACHED is not None and not force_reload:
        return _CACHED
    explicit = os.environ.get("ASML_P6_SOLVER_PATH")
    if explicit:
        p = Path(explicit).expanduser().resolve()
        if p.is_dir():
            p = p / "solver.py"
        if p.is_file():
            mod = _load(p)
            fn = getattr(mod, "predict_overlay", None) or getattr(mod, "solve", None)
            if fn is None:
                raise AttributeError(str(p))
            _CACHED = (str(p), fn)
            return _CACHED
    bench = os.environ.get("ASML_BENCH_ROOT")
    if bench:
        for sub in ("p6-thermal", "th-04-reticle-heat"):
            p = Path(bench).expanduser().resolve() / "labs" / sub / "solver.py"
            if p.is_file():
                mod = _load(p)
                fn = getattr(mod, "predict_overlay", None) or getattr(mod, "solve", None)
                if fn is None:
                    raise AttributeError(str(p))
                _CACHED = (str(p), fn)
                return _CACHED
    _CACHED = ("reference", reference_thermal.predict_overlay)
    return _CACHED

def reset_loader_cache() -> None:
    global _CACHED
    _CACHED = None
