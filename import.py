import sys
import time
from colorama import Fore, Style, init

# Set output encoding to UTF-8
sys.stdout.reconfigure(encoding='utf-8')

# Initialize colorama
init(autoreset=True)

def print_ascii_art_slowly():
    ascii_art_lines = [
        Fore.RED + r"               ⑧  :::::::::::::::::::::::::::::::::::::::::::::::::-===--::::::::::::::::::::...................:::::. ⑧",
        Fore.RED + r"               ⑧  :::::::::::::::::::::::::::::::::::::::::--+*#############+-:::::::::::::.....................:::::. ⑧",
        # Add other lines here as needed...
        Fore.CYAN + r"                               ②         ______  __ __   ____  ____   __  _      __ __   ___   __ __ ",
        Fore.GREEN + r"                               ②        |      ||  |  | /    ||    \ |  |/ ]    |  |  | /   \ |  |  |",
        Fore.YELLOW + r"                               ②        |      ||  |  ||  o  ||  _  ||  ' /     |  |  ||     ||  |  |",
        Fore.BLUE + r"                               ②        |_|  |_||  _  ||     ||  |  ||    \     |  ~  ||  O  ||  |  |",
        Fore.MAGENTA + r"                               ②          |  |  |  |  ||  _  ||  |  ||     \    |___, ||     ||  :  |",
        # Continue adding lines here...
    ]

    for line in ascii_art_lines:
        print(line)
        time.sleep(0.3)  # Slow down the printing

if __name__ == "__main__":
    print_ascii_art_slowly()
