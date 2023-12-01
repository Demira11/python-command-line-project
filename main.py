from peewee import SqliteDatabase, Model, CharField, IntegerField
import argparse

# Import the 'review' function from flashcards module
from flashcards.flashcards import create_flashcard, train, list_flashcards, review

db = SqliteDatabase('flashcards.db')

class Flashcard(Model):
    title = CharField()
    question = CharField()
    answer = CharField()
    correct_count = IntegerField(default=0)  # Change CharField to IntegerField
    incorrect_count = IntegerField(default=0)  # Change CharField to IntegerField

    class Meta:
        database = db

db.connect()
db.create_tables([Flashcard])

def create_flashcard(title, question, answer):
    Flashcard.create(title=title, question=question, answer=answer)

def list_flashcards():
    return Flashcard.select()

def main():
    parser = argparse.ArgumentParser(description="Flashcards CLI")
    parser.add_argument('--create', action='store_true', help='Create a new flashcard')
    parser.add_argument('--train', type=int, help='Start a training session with the specified number of cards')
    parser.add_argument('--list', action='store_true', help='List all flashcards')
    parser.add_argument('--review', type=int, help='Review flashcards with the specified number')

    args = parser.parse_args()

    if args.create:
        # Code for creating a flashcard (similar to what you already have)
        pass
    elif args.train:
        train(args.train)
    elif args.list:
        # Code for listing flashcards (similar to what you already have)
        pass
    elif args.review:
        review(args.review)

if __name__ == "__main__":
    main()
