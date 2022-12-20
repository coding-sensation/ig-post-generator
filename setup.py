import sys
import subprocess
import pkg_resources

required =  {"numpy", "regex", "pillow", "panda", "shortuuid", "aggdraw", "psutil", "scipy", "pyspectator", "pyperclip", "matplotlib", "requests", "pyspellchecker", "speechrecognition", "pytesseract", "pytz", "shortuuid"}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed

def install_packages():
    if missing:
        python = sys.executable
        subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)
    else:
        print("All packages are already installed.\n")