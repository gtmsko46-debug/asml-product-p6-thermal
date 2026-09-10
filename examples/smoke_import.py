from asml_product_p6_thermal import thermal_overlay
print(thermal_overlay({"duty_cycle": 0.8, "exposure_s": 1.0, "reticle_reflectivity": 0.9, "n_dies": 8}).to_dict())
