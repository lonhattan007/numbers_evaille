# Numbers Evaille

## Description

This folder contains files to solve the Numbers Evaille problem:

Given a pack of cards with unique numbers and a required goal card from the pack. The cards are categorized into ranks. Find 4 cards of whose ranks differ from each other and the goal number card's rank, such that the sum of the 4 cards is equal to the goal card's number.

## Folder structure:

- _card.py_: Python file defining class Card
- _deck.py_: Python file defining class Deck
- _solution.py_: Python solution file
- _input.txt_: Input file, currently only contains 107 first cards and their primary ranks
- _README.md_: Instruction file

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

## Status

- __The algorithm is not ready, currently the program just imports and prints cards' info.__
- Solving for extra cards is currently unavailable.
- The input file can only contain a rank per card. For cards with alternative ranks, you need to create a new input file.
