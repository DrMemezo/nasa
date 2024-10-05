"""THIS PROJECT HAS BEEN MADE FOR THE NASA SPACE APPS HACKATHON
PROJECT DEVELOPER: Jamal Uddin
PROJECT MANAGER: Jamal Uddin
REASEREACHER: Chaudry Mohommad 
license is mit i think idk much about that"""

import argparse
import sys
from story import story, info
from graph import show_graph_of
from rich import print

#! Take in input from the commad line
#! Output from the given options:
    #! Show: Displays a graph from the data
    #! Info: Info about a specific time frame
    #! Story about climate change: using cls/clear and slow_print to tell a story
    #! WhatToDo: What can the viewer do?  

def show(country):
    country = country.strip().title()
    acceptable = ["United States", "United Kingdom", "China", "India", "Germany"]
    if country in acceptable:
        show_graph_of(country)
        return
    
    print(f"ERROR: {country} is not supported\nAcceptable countries are: ", acceptable)
    sys.exit(1)

def main():
    parser = argparse.ArgumentParser(
                    prog='nasa.py',
                    description='A Story about climate change')
    # Arguments
    parser.add_argument('--story', help='A story about climate change', action="store_true")
    parser.add_argument('--show', nargs='?', type=str, const="United States", help='Country to show CO2 Emmisions (default: United States)')
    parser.add_argument('--info', type=int, help='Show some info about the specified time period')
    parser.add_argument('-d', help="Debug mode", action="store_true")

    args = parser.parse_args()
    
    if args.d:
        print(args)
    
    if args.story:
        story()

    if time := args.info:
        info(time) 
    
    if country := args.show:
        show(country.title())
    
if __name__ == "__main__":
    main()