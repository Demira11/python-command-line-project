
from models import FlashCard

def seed_data():
  
    FlashCard.create(front='Question 1', back='Answer 1')
    FlashCard.create(front='Question 2', back='Answer 2')
  

if __name__ == "__main__":
    seed_data()
