from bot.utils.moon import Moonphase


if __name__ == '__main__':
    image = Moonphase().draw_img()
    image.save("moonphase.png")
    gallery = Moonphase.make_gallery()
    gallery.save("gallery.png")
