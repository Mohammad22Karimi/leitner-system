import json
import os
from datetime import timedelta

DATA_FILE = "leitner_box.json"

BOXES = {
    1: timedelta(days=1), # box 1 : review every 1 day
    2: timedelta(days=3), # box 2 : review every 3 day
    3: timedelta(days=7), # box 3 : review every 7 day
    4: timedelta(days=14), # box 4 : review every 14 day
    5: timedelta(days=30), # box 5 : review every 30 day
}

def initialize_boxes():
    if not os.path.exists(DATA_FILE):
        boxes = {box: [] for box in BOXES}
        with open(DATA_FILE, "w") as file:
            json.dump(boxes, file);

def load_boxes():
    with open(DATA_FILE, "r") as file:
        return json.load(file)

def save_boxes(boxes):
    with open(DATA_FILE, "w") as file:
        json.dump(boxes, file, indent=4)

def add_word(boxes, word, meaning):
    boxes["1"].append({"word": word, "meaning": meaning, "last_reiviewed": datetime.now().isoformat()})
    print(f"Added '{word}' to box 1.")
    save_boxes(boxes)
def main():
    initialize_boxes()
    boxes = load_boxes()
    
    while True:
        print("\nLeitner System Menu:")
        print("1. Add a new word")
        print("2. Review a box")
        print("3. Exit")
        choice = input("choose an option: ").strip()
        
        if choose == "1":
            word = input("Enter the new word: ").strip()
            meaning = input(f"Enter the meaming of '{word}': ").strip()
            add_word(boxes, word, meaning)
        