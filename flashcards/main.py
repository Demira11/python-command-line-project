# main.py

from flashcards import create_flashcard, train, list_flashcards, search_flashcards
import argparse
def main():
    parser = argparse.ArgumentParser(description="Flashcards CLI")
    parser.add_argument("--create", action="store_true", help="Create a new flashcard")
    parser.add_argument("--train", action="store_true", help="Start a training session")
    parser.add_argument("--list", action="store_true", help="List all flashcards")

    args = parser.parse_args()

    if args.create:
        create_flashcard()
    elif args.train:
        train()
    elif args.list:
        list_flashcards()
    else:
        print("Invalid command. Use --create, --train, or --list.")

if __name__ == "__main__":
    main()
