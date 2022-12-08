from asyncore import read
import os.path
import os
from pathlib import Path
from PIL import Image, ImageDraw
import aggdraw
from io import BytesIO
import random
import compress as cs
#
# 
# 
# 
# 
# 
# 
languages = ["c", "cpp", "java", "python"]
# 
# 
# 
#
#
def add_margin(pil_img, top, right, bottom, left, color):
    width, height = pil_img.size
    new_width = width + right + left
    new_height = height + top + bottom
    result = Image.new(pil_img.mode, (new_width, new_height), color)
    result.paste(pil_img, (left, top))
    return result
#
#
#
#
#
def get_file_extension(file_path):
    split_tup = os.path.splitext(file_path)
    file_extension = split_tup[1]
    return file_extension
#
#
#
#
# 
def add_corners(image, radius):
    mask = Image.new('L', image.size)
    draw = aggdraw.Draw(mask)
    brush = aggdraw.Brush('white')
    width, height = mask.size
    draw.pieslice((0, 0, radius*2, radius*2), 90, 180, 255, brush)
    draw.pieslice((width - radius*2, 0, width, radius*2), 0, 90, None, brush)
    draw.pieslice((0, height - radius * 2, radius *
                   2, height), 180, 270, None, brush)
    draw.pieslice((width - radius * 2, height - radius *
                   2, width, height), 270, 360, None, brush)
    draw.rectangle((radius, radius, width - radius, height - radius), brush)
    draw.rectangle((radius, 0, width - radius, radius), brush)
    draw.rectangle((0, radius, radius, height-radius), brush)
    draw.rectangle((radius, height-radius, width-radius, height), brush)
    draw.rectangle((width-radius, radius, width, height-radius), brush)
    draw.flush()
    image = image.convert('RGBA')
    image.putalpha(mask)
    return image
#
#
#
#
#
def make_square(im):
    x, y = im.size
    size = max(256, x, y)
    new_im = Image.new('RGBA', (size, size), (255, 255, 255, 1))
    new_im.paste(im, (int((size - x) / 2), int((size - y) / 2)))
    return new_im
#
#
#
#
#
def round_images(image_path_name):
    if get_file_extension(image_path_name) != ".png":
        print("Invalid file type. Only PNG files are accepted.")
        return
    image = Image.open(image_path_name)
    image = add_corners(image, 25)
    image = make_square(image)
    image.save(image_path_name)

def create_missing_folders():
    if not cs.is_existing("code/ready"):
        os.makedirs("code/ready")
    if not cs.is_existing("code/not-ready"):
        os.makedirs("code/not-ready")
#
#
#
#
#
def get_code_ready(image_path):
    round_images(image_path)
    image = Image.open(image_path)
    new_image = Image.new("RGBA", image.size, "WHITE")
    new_image.paste(image, (0, 0), image)
    new_image.convert('RGB')
    final_image =  add_margin(new_image, 25, 25, 25, 25, (255, 255, 255))
    final_image.save('code/ready/code-' + str(random.randint(0,100)) + ".png", quality=95)
    print("Success!\n")

def create_code_for_post():
    create_missing_folders()
    file_name = input("Enter the name of the file that is not ready to be posted: ")
    file_name = file_name + ".png"
    get_code_ready("code/not-ready/" + str(file_name))