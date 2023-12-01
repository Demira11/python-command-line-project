import argparse
from flashcards.flashcards import create_flashcard, train, list_flashcards, search_flashcards

def main():
    parser = argparse.ArgumentParser(description="Flashcards CLI")
    parser.add_argument('--create', action='store_true', help='Create a new flashcard')
    parser.add_argument('--train', action='store_true', help='Train with flashcards')
    parser.add_argument('--list', action='store_true', help='List all flashcards')
    parser.add_argument('--search', type=str, help='Search for a flashcard by title')

    args = parser.parse_args()

    if args.create:
        create_flashcard()
    elif args.train:
        train()
    elif args.list:
        list_flashcards()
    elif args.search:
        search_flashcards(args.search)

if __name__ == "__main__":
    main()
