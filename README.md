# Numbers Evaille

## Description

This program is written to solve the Numbers Evaille problem:

Given a pack of cards with unique numbers and a required goal card from the pack. The cards are categorized into ranks. Find 4 cards of whose ranks differ from each other and the goal number card's rank, such that the sum of the 4 cards is equal to the goal card's number.

## Status

- __The algorithm is not ready, currently the program just imports and prints cards' info.__
- Solving for extra cards is currently unavailable.
- The input file can only contain a rank per card. For cards with alternative ranks, you need to create a new input file.

## Folder structure:

The project folder contains these files:

- _card.py_: Python file defining class Card
- _deck.py_: Python file defining class Deck
- _solution.py_: Python solution file
- _input.txt_: Input file, currently only contains 107 first cards and their primary ranks
- _README.md_: Instruction file
- _.gitignore_: Git's config file to ignore unnecessary files while releasing the project

## Preparation

- Install [Git](https://git-scm.com/download/win)
- Install [Python 3](https://www.python.org/downloads/release/python-3100/)

## How to use

- You need to install Python version 3.x on your machine, or have a python compiler in your IDE (Visual Studio, Pycharm,...).
- In your terminal, clone this repo:
    ```
    git clone https://github.com/lonhattan007/numbers_evaille.git
    ```
    or: 
    ```
    git clone git@github.com:lonhattan007/numbers_evaille.git
    ```
    The second method requires an SSH key every time you pull from or push to the repo.
- Open your terminal. On Windows, press `Ctrl + R`, then type `cmd` and press `Enter`.
- Move into this folder:
    ```
    cd numbers_evaille
    ```
- In your terminal, move into this folder and run:
    - Windows: 
    ```
    python solution.py input.txt
    ```
    - Linux or Mac: 
    ```python3 solution.py input.txt```
- Or you can run the program in your IDE, make sure to config `input.txt` as an argument.
- To get updates, move in to `numbers_evaille` folder and run:
    ```
    git pull
    ```
- __DON'T__ push to the repo directly. Ask the author first.

## How it works

To be added.
