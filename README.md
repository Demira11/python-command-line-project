# python-command-line-project

This is a command line application built with Python and PeeWee for managing flashcards.

## Features

- Create new flashcards
- Set up training sessions
- Review flashcards with front and back content
- Keep track of correct and incorrect answers for each flashcard

## Project Structure

Python-Command-Line-Application/
|-- venv/
|-- flashcards/
| |-- init.py
| |-- models.py
| |-- seed.py
| |-- main.py
|-- README.md

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/Python-Command-Line-Application.git
   ```

2. Set up a virtual environment and install dependencies:

   ```bash
   cd Python-Command-Line-Application
   python -m venv venv
   source venv/bin/activate   # For Linux/Mac
   pip install -r requirements.txt
   ```

3. Run the seed script to initialize the database:

   ```bash
   python flashcards/seed.py
   ```

## Usage

- To create a new flashcard:

  ```bash
  python flashcards/main.py --create
  ```

- To start a training session:

  ```bash
  # Add instructions for training session if implemented
  ```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or fixes.
