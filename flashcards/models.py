from peewee import SqliteDatabase, Model, CharField, IntegerField

db = SqliteDatabase('flashcards.db')

class FlashCard(Model):
    title = CharField()
    question = CharField()
    answer = CharField()
    correct_count = IntegerField(default=0)

    class Meta:
        database = db
