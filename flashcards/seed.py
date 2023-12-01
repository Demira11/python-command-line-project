
from flashcards.models import FlashCard

def seed_data():
    # Create sample flashcards
    FlashCard.create(title='Card 1', question='Question 1', answer='Answer 1')
    FlashCard.create(title='Card 2', question='Question 2', answer='Answer 2')
    FlashCard.create(title='Card 3', question='Question 3', answer='Answer 3')

if __name__ == '__main__':
    seed_data()
