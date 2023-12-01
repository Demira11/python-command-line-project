import argparse
from flashcards.flashcards import create_flashcard, train, list_flashcards


def main():
    parser = argparse.ArgumentParser(description="Flashcards CLI")
    parser.add_argument('--create', action='store_true', help='Create a new flashcard')
    parser.add_argument('--train', type=int, help='Start a training session with the specified number of cards')
    parser.add_argument('--list', action='store_true', help='List all flashcards')
    parser.add_argument('--review', type=int, help='Review flashcards with the specified number')

    args = parser.parse_args()

    if args.create:
        create_flashcard()  # Call your create_flashcard function here
    elif args.train:
        train(args.train)  # Call your train function here
    elif args.list:
        list_flashcards()  # Call your list_flashcards function here
    elif args.review:
        review_flashcards(args.review)  # Call your review_flashcards function here

if __name__ == "__main__":
    main()
