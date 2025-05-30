import json
mars_facts = {"data": {"mass": (0.64169e24, "kg"),
                       "volume": (16.312e10, "km³"),
                       "radius": (3389.5, "km"),
                       "density": (3934, "kg/m³"),
                       "gravity": (3.73, "m/s²"),
                       "satelites": (2, ""),
                       "rings": (None, ""),
                       "distance from the sun": (227.956e6, "km"),
                       "sidereal orbit period": (686.980, "days"),
                       "sidereal rotation period": (24.6229, "hrs"),
                       "length of day": (24.6597, "hrs")}}
with open("mars.json", "w") as file:
    json.dump(mars_facts, file, indent=4)