from bot.utils.moon import Moonphase

if __name__ == '__main__':
    m = Moonphase()
    image = m.draw_img()
    image.save("moonphase.png")
    gallery = Moonphase.make_gallery()
    gallery.save("gallery.png")
    with open("README.md", "w") as file:
        file.write(f"### Current Moon Phase: {m.__repr__()}\n"
                   "![Moon Phase](moonphase.png)\n"
                   "### Next Key Phases\n"
                   "![Gallery](gallery.png)")
