# flashcards.py
from peewee import SqliteDatabase, Model, CharField

db = SqliteDatabase('flashcards.db')

class Flashcard(Model):
    title = CharField()
    question = CharField()
    answer = CharField()

    class Meta:
        database = db

db.connect()
db.create_tables([Flashcard])

def create_flashcard(title, question, answer):
    Flashcard.create(title=title, question=question, answer=answer)

def list_flashcards():
    return Flashcard.select()

def train():
    flashcards = Flashcard.select()
    for flashcard in flashcards:
        print("Title:", flashcard.title)
        print("Question:", flashcard.question)
        input("Press Enter to see the answer...")
        print("Answer:", flashcard.answer)
        input("Press Enter for the next flashcard...")

# Additional functions if any
