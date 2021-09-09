from tkinter import *
from PIL import Image, ImageTk, ImageFont, ImageDraw
import random
from datetime import datetime

def add_watermark():
    global im, image_to_water_mark
    # Create an Image Object from an Image

    width, height = im.size

    draw = ImageDraw.Draw(im)
    text = "Yahaya"

    font = ImageFont.truetype("Arial.ttf", 50)
    textwidth, textheight = draw.textsize(text, font)

    # calculate the x,y coordinates of the text
    margin = 10
    x = width - textwidth - margin
    y = height - textheight - margin

    # draw watermark in the bottom right corner
    draw.text((x, y), text, font=font)
    # im.show()
    watermark_image = Image.open("images/watermark_main.png")
    w_size = (50, 50)
    watermark_image.thumbnail(w_size)

    im.paste(watermark_image, (x-50, y), mask=watermark_image)

    image_to_water_mark = ImageTk.PhotoImage(im)
    canvas.itemconfig(cat_img, image=image_to_water_mark)


def save_image():
    global im
    now = datetime.now()
    current_time = now.strftime("%H%M%S")
    im.save(f'images/MY-{now.year}-{now.month}-{now.day}{current_time}.jpg')
    window.destroy()


def add_image():
    global cat_img
    cat_img = canvas.create_image(375, 285, image=image_to_water_mark)
    canvas.grid(row=0, column=0)

    button = Button(text="Add Watermark", command=add_watermark)
    button.grid(row=2, column=0)
    button.config(highlightthickness=0)

    save_button = Button(text="Save Image", command=save_image)
    save_button.grid(row=4, column=0)
    save_button.config(highlightthickness=0)


window = Tk()
window.title("Watermark Image - Application")
window.geometry("750x690")

# Image
im = Image.open("images/cat.jpg")

size = (750, 550)
im.thumbnail(size)
image_to_water_mark = ImageTk.PhotoImage(im)
canvas = Canvas(width=800, height=600)
cat_img = None


add_button = Button(text="Load Image", command=add_image)
add_button.grid(row=2, column=1)
add_button.config(highlightthickness=0)

window.mainloop()
