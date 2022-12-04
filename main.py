from PIL import Image, ImageFont, ImageDraw
from datetime import datetime
from title import * 
from program import *
import shutil

# constants
languages = ["c", "cpp", "cs", "go", "java", "javascript", "python", "tips"]
titles_path = "titles/"
font_size = 100 # 55
font_family = "Archive.otf"
top_word_position = 5
middle_word_position = 4
bottom_word_position = 3

def clear():
    shutil.rmtree('code')
    shutil.rmtree('titles')
            
def start():
    choice = int(input("\n1. Title\n2. Code\n3. Clear\nEnter your choice: "))
    if choice == 1:
        create_title_for_post()
    elif choice == 2:
        create_code_for_post()
    elif choice == 3:
        clear()

start()