
from peewee import SqliteDatabase, Model, CharField, IntegerField

db = SqliteDatabase('data/flashcards.db')




class FlashCard(Model):
    front = CharField()
    back = CharField()
    correct_answers = IntegerField(default=0)
    incorrect_answers = IntegerField(default=0)

    class Meta:
        database = db

db.connect()
db.create_tables([FlashCard])
