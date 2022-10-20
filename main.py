from PIL import Image, ImageFont, ImageDraw
from datetime import datetime
import os 

# constants
languages = ["c", "cpp", "java", "python"]
titles_path = "titles/"
font_size = 100 # 55
font_family = "Post.otf"
top_word_position = 5
middle_word_position = 4
bottom_word_position = 3



def get_current_date():
    now = datetime.now()
    result = now.strftime("%Y-%m-%d-%H-%M-%S")
    return result


def print_invalid():
    print("\n! ! !\tInvalid Input\t! ! !")

def validate_title_length(title_choice):
    if(len(title_choice) > 11 or len(title_choice) <= 2):
        print_invalid()
        print("\nTitle Is Too Long\n")
        return False
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


def count_folders_in(path):
    return (len(next(os.walk(path))[1]))


def draw_this(img, text, position):
    I1 = ImageDraw.Draw(img)
    W, H = (img.width, img.height)
    myFont = ImageFont.truetype("fonts/" + font_family, font_size)
    w = I1.textlength(text, myFont)
    h = 51
    I1.text(((W-w)/2, (H-h)/int(position)), text,
    font=myFont,  fill=(0, 0, 0),
    stroke_fill="black")


def create_title_for_post():
    existing = os.path.exists(titles_path)
    if(not existing):
        os.makedirs(titles_path)
    post_number = input("\nEnter the number of your post: ")
    title_choice = input("\nEnter the title of your post: ")
    if(validate_title_length(title_choice)):
        new_folder_name = get_current_date()
        os.makedirs('titles/' + str(new_folder_name), exist_ok=True)
        title = validate_title_length(title_choice)
        for i in range(len(languages)):
            img = Image.open("languages/" + languages[i] + ".png")
            draw_this(img, "ADDING", top_word_position)
            draw_this(img, "NUMBERS", bottom_word_position)
            img.save("titles/" + str(new_folder_name) + "/title-" + post_number +
                        "-" + languages[i] + ".png")
            
create_title_for_post()