from PIL import Image, ImageFont, ImageDraw
from datetime import datetime
from title import * 
from program import *
import shutil

def clear():
    if cs.is_existing("code"):
        shutil.rmtree('code')
    if cs.is_existing("titles"):
        shutil.rmtree('titles')
            
def start():
    clear()
    choice = int(input("\n1. Title\n2. Code\nEnter your choice: "))
    if choice == 1:
        create_title_for_post()
    elif choice == 2:
        create_code_for_post()

start()