def z1():
    from PIL import Image
    n = "otkr.jpg"
    with Image.open(n) as img:
        img.load()
    n_img = img.crop((200, 291, 1000, 1024))
    n_img.save("new_img.jpg")

def z2():
    from PIL import Image
    otk_dict = {"Новый год": "ng.jpg", "День рождения": "dr.jpg", "8 марта": "8m.jpg"}

    p = input("Введите праздник: ")
    img = otk_dict.get(p)
    image = Image.open(img)
    image.show()


def z3():
    from PIL import Image, ImageDraw, ImageFont
    n = "otkr.jpg"
    with Image.open(n) as img:
        img.load()
    n_img = img.crop((200, 291, 1000, 1024))
    n_img.save("new_img.jpg")

    name = input("Кого вы хотите поздравить: ")
    txt = str(name) + ", поздравляю!"
    img_txt = ImageDraw.Draw(n_img)
    font = ImageFont.truetype("impact.ttf", size=65)
    img_txt.text((50,600), txt, font = font, fill = "yellow")
    n_img.show()
    n_img.save("nwn.jpg")


