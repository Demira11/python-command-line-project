
import argparse
from models import FlashCard

def create_flashcard(front, back):
    return FlashCard.create(front=front, back=back)



def main():
    parser = argparse.ArgumentParser(description='Flash Cards Command Line Application')
    parser.add_argument('--create', action='store_true', help='Create a new flashcard')
    

    args = parser.parse_args()

    if args.create:
        front = input('Enter the question (front of the card): ')
        back = input('Enter the answer (back of the card): ')
        create_flashcard(front, back)
        print('Flashcard created successfully!')

   

if __name__ == "__main__":
    main()
