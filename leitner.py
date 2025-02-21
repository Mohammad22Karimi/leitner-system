import json
import os
from datetime import datetime, timedelta

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
    next_review = (datetime.now() + BOXES[1]).isoformat()
    boxes["1"].append({"word": word, "meaning": meaning, "next_review": next_review})
    print(f"Added '{word}' to box 1.")
    save_boxes(boxes)
    
def review_box(boxes, box_number):
    box_key = str(box_number)
    now = datetime.now()
    due_words = [item for item in boxes[box_key] if datetime.fromisoformat(item["next_review"]) <= now]
    
    if not due_words:
        print(f"No words to review in Box {box_number} today.")
        return
    
    print(f"Reviewing box {box_number}:")
    for item in due_words[:]: 
        word = item["word"]
        meaning = item["meaning"]
        response = input(f"'{word}'? ({meaning}) (y/n): ").strip().lower()
        if response == "y":
            if box_number < len(BOXES):
                next_box = str(box_number + 1)
                next_review = (datetime.now() + BOXES[box_number + 1]).isoformat()
                boxes[next_box].append({"word": word, "meaning": meaning, "next_review": next_review})
                print(f"Moved '{word}' to Box {next_box} (Next review on {next_review}).")
                
            else:
                print(f"'{word}' is in the final box. No further moves.")
            
        else:
            next_review = (datetime.now() + BOXES[1]).isoformat()
            boxes["1"].append({"word": word, "meaning": meaning, "next_review": next_review})
            print(f"Moved '{word}' back to Box 1 (Next review on {next_review}).")

        boxes[box_key].remove(item)
            
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
        
        if choice == "1":
            word = input("Enter the new word: ").strip()
            meaning = input(f"Enter the meaming of '{word}': ").strip()
            add_word(boxes, word, meaning)
        elif choice == "2":
            box_number = input("Enter the box number to review (1-5): ").strip()
            if box_number.isdigit() and 1 <= int(box_number) <= 5:
                review_box(boxes, int(box_number))
                
            else:
                print("Invalid box number. Please enter a number between 1 and 5.")
        
        elif choice == "3":
            print("Exiting the Leitner system. Goodbye!")
            break
        else: 
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()