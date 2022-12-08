from title import * 
from program import *
from time import sleep
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
    else:
        clear()
        return
    sleep(60)
    clear()

start()