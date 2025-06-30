from bot.utils.moon import Moonphase


if __name__ == '__main__':
    image = Moonphase.make_gallery()
    image.save("gallery.png")
