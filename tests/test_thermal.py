import pytest
from asml_product_p6_thermal import thermal_overlay
from asml_product_p6_thermal.loader import reset_loader_cache

@pytest.fixture(autouse=True)
def _e(monkeypatch):
    monkeypatch.delenv("ASML_BENCH_ROOT", raising=False)
    reset_loader_cache()

def test_smoke():
    r = thermal_overlay({"duty_cycle": 0.8, "n_dies": 8})
    assert len(r.overlay_nm) == 8
    assert r.mean_abs_nm >= 0

def test_missing():
    with pytest.raises(KeyError):
        thermal_overlay({})
