import ephem
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

root = Path(__file__).resolve().parent.parent.parent
moonphase_image = root / "assets" / "results" / "moonphase.png"


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
            return f"🌑 New Moon {self._phase_1:.2f}%"
        if 99 <= self._phase_1 <= 100:
            return f"🌕 Full Moon {self._phase_1:.2f}%"
        if 1 < self._phase_1 < 49 and self._increase:
            return f"🌒 Waxing Crescent {self._phase_1:.2f}%"
        if 1 < self._phase_1 < 49 and not self._increase:
            return f"🌘 Waning Crescent {self._phase_1:.2f}%"
        if 49 <= self._phase_1 <= 51 and self._increase:
            return f"🌓 First Quarter {self._phase_1:.2f}%"
        if 49 <= self._phase_1 <= 51 and not self._increase:
            return f"🌗 Last Quarter {self._phase_1:.2f}%"
        if 51 < self._phase_1 < 99 and self._increase:
            return f"🌔 Waxing Gibbous {self._phase_1:.2f}%"
        if 51 < self._phase_1 < 99 and not self._increase:
            return f"🌖 Waning Gibbous {self._phase_1:.2f}%"

    def draw_img(self):
        image = Image.open(moonphase_image).convert("RGBA")
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

    def draw_gallery(self, text: str):
        image = self.draw_img()
        image_width, image_height = image.size
        label_height = 200
        total_width, total_height = image_width, image_height + label_height
        new_image = Image.new("RGBA", (total_width, total_height), (0, 0, 0, 255))
        new_image.paste(image, (0, 0))
        font = ImageFont.load_default(48)
        draw = ImageDraw.Draw(new_image)
        lines = text.splitlines()
        spacing = 20
        line_height = font.getbbox("A")[3] + spacing
        text_height = line_height * len(lines)
        start = image_height + (label_height - text_height) // 2
        for i, line in enumerate(lines):
            bbox = draw.textbbox((0, 0), line, font=font)
            text_width = bbox[2] - bbox[0]
            x = (image_width - text_width) // 2
            y = start + i * line_height
            draw.text((x, y), line, font=font, fill="white")
        return new_image

    @classmethod
    def make_gallery(cls):
        now = ephem.Date(ephem.now())
        phases = [(ephem.next_first_quarter_moon, "Next first quarter is\n"),
                  (ephem.next_full_moon, "Next full moon is\n"),
                  (ephem.next_last_quarter_moon, "Next last quarter is\n"),
                  (ephem.next_new_moon, "Next new moon is\n"), ]
        phases.sort(key=lambda x: x[0](now) - now)
        images = []
        for phase, label in phases:
            when = phase(now)
            moon = cls(when)
            year, month, day, hour, minute, second = when.tuple()
            label_extra = f"on {day:02}/{month:02}/{year} at {hour:02}:{minute:02}:{round(second):02}"
            images.append(moon.draw_gallery(label + label_extra))
        width, height = images[0].size
        final = Image.new("RGBA", (width * 2, height * 2), (0, 0, 0, 255))
        final.paste(images[0], (0, 0))
        final.paste(images[1], (width, 0))
        final.paste(images[2], (0, height))
        final.paste(images[3], (width, height))
        return final

    def __repr__(self):
        return f"{self._phase_name()}"
