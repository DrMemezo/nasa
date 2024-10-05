""" This module reads text from .story_text.txt, filters them by heading(<h>) and body(<o>) and outputs them in a typewriter fashion"""
from rich.console import Console
import sys
import re
from time import sleep
import os

CONSOLE = Console()

def slow_print(message:str, wait:float=0.1,
                style:str="white", end:str="\n"):
    """NOTE: Only pass strings!!"""
    
    if message == "" or message is None: # Does not print whitespaces
        return
    
    global CONSOLE

    for char in message:
        CONSOLE.print(char,style=style, end="")
        sleep(wait)
    print(end=end)

def clear_screen() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')

def wait_for_user() -> None:
    print("Enter 'q' to quit, else enter any key")
    user_input = input().strip().lower()
    if user_input == 'q':
        sys.exit(0)

def story():
    global CONSOLE
    # Read file
    with open(".story_text.txt", "r") as file:
        contents = file.read().strip()
    # Parse
    headings = re.findall(pattern=r"<h>(.*)<h>",string=contents)
    bodys = re.findall(pattern=r"<o>(.*)<o>",string=contents)
    sections = dict(zip(headings, bodys))
    # Ouput each section
    CONSOLE.print("\tENTERING STORY MODE, PROGRAM WILL EXIT AFTER YOU QUIT OR FINISH THE STORY\n\tPRESS <Ctrl>+C to quit anytime!\n\t\tHAPPY READING!", style="deep_pink3")
    sleep(3)
    clear_screen()
    CONSOLE.print("A Climate Story", style="cyan2")
    for head, bod in sections.items():
        slow_print(head, style="white bold underline", wait=0.05)
        try:
            slow_print(bod, wait=0.01)
        except KeyboardInterrupt:
            break
        wait_for_user()
        clear_screen()
    sys.exit(0)    

def info(time:int):
    global CONSOLE
    # Validate time
    if time not in range(1750, 2101):
        CONSOLE.print("Please enter a time frame between 1750, and 2100")
        sys.exit(1)
    
    frames = {
        "1800-1849": "Factories start up in the UK and the US, and ideas of industrialization are exported throughout the globe",
        "1850-1919": "Emissions rise in the United States, due to the switch from burning wood to burning coal",
        "1929-1939": "The Great Depression causes a steep decline in CO2 emissions",
        "1950-1990": "Russia experienced rapid growth, but the dissolution of the soviet union caused a steep decline in CO2 emissions",
        "1991-2010": "China leads Asian countries in CO2 emissions, and overtakes the US as the top CO2 emitter in 2006",
        "2019-2021": "The COVID Pandemic caused a steep decline in CO2 emissions.",
        "2023-2050": "(PREDICTED) 80% of the Maldives has been submerged, due to the rise in sea levels. Frequency of natural disasters increases, millions of lives are lost to heatwaves, floods, and our way of life is severly threatened."
    }

    for frame in frames:
        lower, upper = tuple(map(int, frame.split('-'))) # Gets the median(?) year in the timeframe
        if time in range(lower, upper+1):
            slow_print(frame, style="cyan2 bold underline", wait=0.09)
            slow_print(frames[frame], wait=0.01)
            return
    
    CONSOLE.print(f"Please input a time in between the following time frames:\n{list(frames.keys())}")
    sys.exit()


if __name__ == "__main__":
    print("Did you mean to type 'nasa.py'?")