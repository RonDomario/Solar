import json

mercury_facts = {"data": {"Mass": (0.33010, "×10²⁴ kg"),
                          "Volume": (6.083, "×10¹⁰ km³"),
                          "Radius": (2_439.7, " km"),
                          "Density": (5_429, " kg/m³"),
                          "Gravity": (3.70, " m/s²"),
                          "Satelites": (0, ""),
                          "Rings": ("No", ""),
                          "Distance from the sun": (57.909, "×10⁶ km"),
                          "Sidereal orbit period": (87.969, " days"),
                          "Sidereal rotation period": (1_407.6, " hrs"),
                          "Length of day": (4_222.6, " hrs")}}
venus_facts = {"data": {"Mass": (4.8673, "×10²⁴ kg"),
                        "Volume": (92.843, "×10¹⁰ km³"),
                        "Radius": (6_051.8, " km"),
                        "Density": (5_243, " kg/m³"),
                        "Gravity": (8.87, " m/s²"),
                        "Satelites": (0, ""),
                        "Rings": ("No", ""),
                        "Distance from the sun": (108.210, "×10⁶ km"),
                        "Sidereal orbit period": (224.701, " days"),
                        "Sidereal rotation period": (-5_832.6, " hrs"),
                        "Length of day": (2_802.0, " hrs")}}
earth_facts = {"data": {"Mass": (5.9722, "×10²⁴ kg"),
                        "Volume": (108.321, "×10¹⁰ km³"),
                        "Radius": (6_371.0, " km"),
                        "Density": (5_513, " kg/m³"),
                        "Gravity": (9.820, " m/s²"),
                        "Satelites": (1, ""),
                        "Rings": ("No", ""),
                        "Distance from the sun": (149.598, "×10⁶ km"),
                        "Sidereal orbit period": (365.256, " days"),
                        "Sidereal rotation period": (23.9345, " hrs"),
                        "Length of day": (24.0, " hrs")}}
mars_facts = {"data": {"Mass": (0.64169, "×10²⁴ kg"),
                       "Volume": (16.312, "×10¹⁰ km³"),
                       "Radius": (3_389.5, " km"),
                       "Density": (3_934, " kg/m³"),
                       "Gravity": (3.73, " m/s²"),
                       "Satelites": (2, ""),
                       "Rings": ("No", ""),
                       "Distance from the sun": (227.956, "×10⁶ km"),
                       "Sidereal orbit period": (686.980, " days"),
                       "Sidereal rotation period": (24.6229, " hrs"),
                       "Length of day": (24.6597, " hrs")}}
jupiter_facts = {"data": {"Mass": (1_898.13, "×10²⁴ kg"),
                          "Volume": (143_128, "×10¹⁰ km³"),
                          "Radius": (69_911, " km"),
                          "Density": (1_326, " kg/m³"),
                          "Gravity": (25.92, " m/s²"),
                          "Satelites": (95, ""),
                          "Rings": ("Yes", ""),
                          "Distance from the sun": (778.479, "×10⁶ km"),
                          "Sidereal orbit period": (4_332.589, " days"),
                          "Sidereal rotation period": (9.9250, " hrs"),
                          "Length of day": (9.9259, " hrs")}}
saturn_facts = {"data": {"Mass": (568.32, "×10²⁴ kg"),
                         "Volume": (82_713, "×10¹⁰ km³"),
                         "Radius": (58_232, " km"),
                         "Density": (687, " kg/m³"),
                         "Gravity": (11.19, " m/s²"),
                         "Satelites": (274, ""),
                         "Rings": ("Yes", ""),
                         "Distance from the sun": (1_432.041, "×10⁶ km"),
                         "Sidereal orbit period": (10_755.699, " days"),
                         "Sidereal rotation period": (10.656, " hrs"),
                         "Length of day": (10.656, " hrs")}}
uranus_facts = {"data": {"Mass": (86.811, "×10²⁴ kg"),
                         "Volume": (6_833, "×10¹⁰ km³"),
                         "Radius": (25_362, " km"),
                         "Density": (1_270, " kg/m³"),
                         "Gravity": (9.01, " m/s²"),
                         "Satelites": (28, ""),
                         "Rings": ("Yes", ""),
                         "Distance from the sun": (2_867.043, "×10⁶ km"),
                         "Sidereal orbit period": (30_685.400, " days"),
                         "Sidereal rotation period": (-17.24, " hrs"),
                         "Length of day": (17.24, " hrs")}}
neptune_facts = {"data": {"Mass": (102.409, "×10²⁴ kg"),
                          "Volume": (6_254, "×10¹⁰ km³"),
                          "Radius": (24_622, " km"),
                          "Density": (1_638, " kg/m³"),
                          "Gravity": (11.27, " m/s²"),
                          "Satelites": (16, ""),
                          "Rings": ("Yes", ""),
                          "Distance from the sun": (4_514.953, "×10⁶ km"),
                          "Sidereal orbit period": (60_189.018, " days"),
                          "Sidereal rotation period": (16.11, " hrs"),
                          "Length of day": (16.11, " hrs")}}
pluto_facts = {"data": {"Mass": (0.01303, "×10²⁴ kg"),
                        "Volume": (0.702, "×10¹⁰ km³"),
                        "Radius": (1_188, " km"),
                        "Density": (1_854, " kg/m³"),
                        "Gravity": (0.62, " m/s²"),
                        "Satelites": (5, ""),
                        "Rings": ("No", ""),
                        "Distance from the sun": (5_869.656, "×10⁶ km"),
                        "Sidereal orbit period": (90_560, " days"),
                        "Sidereal rotation period": (-153.2928, " hrs"),
                        "Length of day": (153.2820, " hrs")}}

with open("mercury.json", "w") as file:
    json.dump(mercury_facts, file, indent=4)
with open("venus.json", "w") as file:
    json.dump(venus_facts, file, indent=4)
with open("earth.json", "w") as file:
    json.dump(earth_facts, file, indent=4)
with open("mars.json", "w") as file:
    json.dump(mars_facts, file, indent=4)
with open("jupiter.json", "w") as file:
    json.dump(jupiter_facts, file, indent=4)
with open("saturn.json", "w") as file:
    json.dump(saturn_facts, file, indent=4)
with open("uranus.json", "w") as file:
    json.dump(uranus_facts, file, indent=4)
with open("neptune.json", "w") as file:
    json.dump(neptune_facts, file, indent=4)
with open("pluto.json", "w") as file:
    json.dump(pluto_facts, file, indent=4)
