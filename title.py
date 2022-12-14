from PIL import Image, ImageFont, ImageDraw
from datetime import datetime
import os 

languages = ["c", "corner", "cpp", "cs", "go", "java", "javascript", "python", "tips"]
titles_path = "titles/"
font_size = 100 # 55
font_family = "Archive.otf"
top_word_position = 5
middle_word_position = 4
bottom_word_position = 3

def get_current_date():
    now = datetime.now()
    result = now.strftime("%Y-%m-%d-%H-%M-%S")
    return result

def print_invalid():
    print("\nInvalid Input")

def validate_title_length(title_choice):
    title_split = title_choice.split(" ")
    if(len(title_split) == 1):
        title = " ".join(title_split[0].upper())
    if(len(title_split) == 2):
        title = (" ".join(title_split[0])).upper(
        ) + "  " + (" ".join(title_split[1])).upper()
    if(len(title_split) == 3):
        title = (" ".join(title_split[0])).upper(
        ) + "  " + (" ".join(title_split[1])).upper() + "  " + (" ".join(title_split[2])).upper()
    return title


def draw_this(img, text, position):
    I1 = ImageDraw.Draw(img)
    W, H = (img.width, img.height)
    myFont = ImageFont.truetype(font_family, font_size)
    w = I1.textlength(text, myFont)
    h = 51
    I1.text(((W-w)/2, (H-h)/int(position)), text,
    font=myFont,  fill=(0, 0, 0),
    stroke_fill="black")

def draw_title(img, title):
    splited_title = ''.join(title).split("  ")
    length = len(splited_title)
    if(length == 1):
        draw_this(img, splited_title[0], middle_word_position)
    elif(length == 2):
        draw_this(img, splited_title[0], top_word_position)
        draw_this(img, splited_title[1], bottom_word_position)
    else:
        draw_this(img, splited_title[0] + "   " + splited_title[1] + "   " + splited_title[2], middle_word_position)
        return

def create_title_for_post():
    existing = os.path.exists(titles_path)
    if(not existing):
        os.makedirs(titles_path)
    title_choice = input("\nEnter the title of your post: ")
    if(validate_title_length(title_choice)):
        new_folder_name = get_current_date()
        os.makedirs('titles/' + str(new_folder_name), exist_ok=True)
        title = validate_title_length(title_choice)
        for i in range(len(languages)):
            img = Image.open("languages/" + languages[i] + ".png")
            draw_title(img, title)
            img.save("titles/" + str(new_folder_name) + "/title-" + languages[i] + ".png")
        print("Success!\n")
