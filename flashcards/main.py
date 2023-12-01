
import argparse

def create_flashcard():
    # Placeholder for creating a new flashcard
    print("Creating a new flashcard")

def train():
    # Placeholder for starting a training session
    print("Starting a training session")

def main():
    parser = argparse.ArgumentParser(description="Flashcards Command Line Application")

    # Define command-line arguments
    parser.add_argument('--create', action='store_true', help='Create a new flashcard')
    parser.add_argument('--train', action='store_true', help='Start a training session')

    # Parse the command-line arguments
    args = parser.parse_args()

    # Check which command was provided
    if args.create:
        create_flashcard()
    elif args.train:
        train()
    else:
        print("No valid command provided. Use --create or --train.")

if __name__ == "__main__":
    main()
