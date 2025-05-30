import ephem
from PIL import Image, ImageDraw


class Moon:
    def __init__(self, date: ephem.Date):
        self._date = date
        self._moon = ephem.Moon(self._date)

    def phase(self):
        return self._moon.phase


class Moonphase:
    def __init__(self, date: ephem.Date = ephem.now()):
        self._date_1 = date
        self._date_2 = date + 1 / (24 * 60 * 60)
        self._moon_1 = Moon(self._date_1)
        self._moon_2 = Moon(self._date_2)
        self._phase_1 = self._moon_1.phase()
        self._phase_2 = self._moon_2.phase()
        self._increase = self._phase_2 > self._phase_1

    def _phase_name(self):
        if self._phase_1 <= 1:
            return "🌑 New Moon"
        if 99 <= self._phase_1 <= 100:
            return "🌕 Full Moon"
        if 1 < self._phase_1 < 49 and self._increase:
            return "🌒 Waxing Crescent"
        if 1 < self._phase_1 < 49 and not self._increase:
            return "🌘 Waning Crescent"
        if 49 <= self._phase_1 <= 51 and self._increase:
            return "🌓 First Quarter"
        if 49 <= self._phase_1 <= 51 and not self._increase:
            return "🌗 Last Quarter"
        if 51 < self._phase_1 < 99 and self._increase:
            return "🌔 Waxing Gibbous"
        if 51 < self._phase_1 < 99 and not self._increase:
            return "🌖 Waning Gibbous"

    def draw_img(self):
        image = Image.open("../assets/results/moonphase.png").convert("RGBA")
        scale = 2
        padding = 2
        width, height = image.size
        hirez_width, hirez_height = width * scale, height * scale
        hirez_shadow = Image.new("RGBA", (hirez_width, hirez_height), (0, 0, 0, 0))
        draw = ImageDraw.Draw(hirez_shadow)

        circle_radius = hirez_width // 2 + padding
        center = (hirez_width // 2, hirez_height // 2)
        bbox_circle = [
            center[0] - circle_radius,
            center[1] - circle_radius,
            center[0] + circle_radius,
            center[1] + circle_radius
        ]

        oval_radius = circle_radius * abs(self._phase_1 - 50) / 50
        bbox_oval = [
            center[0] - oval_radius,
            center[1] - circle_radius,
            center[0] + oval_radius,
            center[1] + circle_radius
        ]

        if self._phase_1 <= 1:
            draw.circle(center, circle_radius, fill=(0, 0, 0, 200))
            shadow = hirez_shadow.resize((width, height), resample=Image.Resampling.LANCZOS)
            return Image.alpha_composite(image, shadow)
        if 99 <= self._phase_1 <= 100:
            shadow = hirez_shadow.resize((width, height), resample=Image.Resampling.LANCZOS)
            return Image.alpha_composite(image, shadow)
        if 1 < self._phase_1 < 49 and self._increase:
            draw.pieslice(bbox_circle, start=90, end=270, fill=(0, 0, 0, 200))
            draw.ellipse(bbox_oval, fill=(0, 0, 0, 200))
            shadow = hirez_shadow.resize((width, height), resample=Image.Resampling.LANCZOS)
            return Image.alpha_composite(image, shadow)
        if 1 < self._phase_1 < 49 and not self._increase:
            draw.pieslice(bbox_circle, start=-90, end=90, fill=(0, 0, 0, 200))
            draw.ellipse(bbox_oval, fill=(0, 0, 0, 200))
            shadow = hirez_shadow.resize((width, height), resample=Image.Resampling.LANCZOS)
            return Image.alpha_composite(image, shadow)
        if 49 <= self._phase_1 <= 51 and self._increase:
            draw.pieslice(bbox_circle, start=90, end=270, fill=(0, 0, 0, 200))
            shadow = hirez_shadow.resize((width, height), resample=Image.Resampling.LANCZOS)
            return Image.alpha_composite(image, shadow)
        if 49 <= self._phase_1 <= 51 and not self._increase:
            draw.pieslice(bbox_circle, start=-90, end=90, fill=(0, 0, 0, 200))
            shadow = hirez_shadow.resize((width, height), resample=Image.Resampling.LANCZOS)
            return Image.alpha_composite(image, shadow)
        if 51 < self._phase_1 < 99 and self._increase:
            draw.circle(center, circle_radius, fill=(0, 0, 0, 200))
            draw.pieslice(bbox_circle, start=-90, end=90, fill=(0, 0, 0, 0))
            draw.ellipse(bbox_oval, fill=(0, 0, 0, 0))
            shadow = hirez_shadow.resize((width, height), resample=Image.Resampling.LANCZOS)
            return Image.alpha_composite(image, shadow)
        if 51 < self._phase_1 < 99 and not self._increase:
            draw.circle(center, circle_radius, fill=(0, 0, 0, 200))
            draw.pieslice(bbox_circle, start=90, end=270, fill=(0, 0, 0, 0))
            draw.ellipse(bbox_oval, fill=(0, 0, 0, 0))
            shadow = hirez_shadow.resize((width, height), resample=Image.Resampling.LANCZOS)
            return Image.alpha_composite(image, shadow)

    def __repr__(self):
        return f"{self._phase_name()} {self._phase_1:.2f}%"

if __name__ == '__main__':
    m = ephem.now()
    print(type(m), m)