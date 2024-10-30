# Word Search Game

## Overview

This Word Search Game allows users to find specified words hidden within a grid of letters. The words can be arranged in any direction: horizontally, vertically, or diagonally.

## Features

- Validates the puzzle and word list for correctness.
- Identifies the coordinates of words found in the puzzle.
- Displays the puzzle with found words highlighted in green.

## Getting Started

### Requirements

- Python 3.x

### Installation

1. Clone the repository or download the script.
2. Ensure you have Python installed on your machine.

### Running the Game

To run the game, execute the script using Python. You can also run specific test functions to check the validity of the word list, puzzle, and display functions.

```bash
python wordsearch.py
```

## Test Functions

Several test functions are provided to check the functionality:

- `test_valid_wordlist()`: Tests the word list validation.
- `test_valid_puzzle()`: Tests the puzzle validation.
- `test_basic_display()`: Tests the basic display function of the puzzle.
- `test_get_positions()`: Tests the functionality that finds word positions in the puzzle.
- `test_coloured_display()`: Tests the colored display of the puzzle with found words.
- `test_wordsearch()`: Tests the complete word search functionality.

You can uncomment any test function in the `__main__` section to run it individually.

## Functions

### `wordsearch(puzzle: list, wordlist: list) -> None`
Main function that takes a puzzle and a list of words to search for. Validates input and displays the puzzle with found words.

### `valid_puzzle(puzzle: list) -> bool`
Validates whether the puzzle is a proper rectangular grid of strings.

### `valid_wordlist(wordlist: list) -> bool`
Checks if the provided word list contains only strings.

### `get_positions(puzzle: list, word: str) -> list`
Finds all positions of a word in the puzzle in various orientations.

### `compare_letter(word: str, puzzle_word: list) -> bool`
Compares a word with a list of letters from the puzzle to check for a match.

### `basic_display(grid: list) -> None`
Displays the puzzle in a simple format.

### `coloured_display(grid: list, positions: list) -> None`
Displays the puzzle with found words highlighted in green.

## Example

To test the word search functionality, you can modify the `puzzle1` and `good_wordlist2` variables in the `test_wordsearch()` function:

```python
puzzle1 = ['RUNAROUNDDL', 'EDCITOAHCYV', ...]
good_wordlist2 = ["scalar", "tray", "blew", "sevruc"]
```

## Conclusion

This Word Search Game is a fun way to practice searching for words in a grid. Feel free to modify the puzzle and word list to create your own challenges! Enjoy!
