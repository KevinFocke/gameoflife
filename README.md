# Game Of Life

Simulates Conway's Game Of Life.

## General information

This was a project-based learning experience. My main goals for the project:

- Setup Continuous Integration environment for testing

- Practice Test-Driven-Development (Red, Green, Refactor methodology)

- Practice Object-Oriented programming (custom iterator, methods)

- Create rudimentary interactive command line interface

## Usage Information

How to install & run:

Install poetry package manager

    https://python-poetry.org/docs/#installation

Clone respository

    git clone https://github.com/KevinFocke/gameoflife.git

Navigate to cloned repository

    cd gameoflife

Install project dependencies

    poetry install

Use virtual environment

    poetry shell

Run python file via CLI

    python src/gameoflife/main.py

## Note regarding the Command Line Interface
The current command line interface (CLI) is a minimum viable product and does not support providing state. However, the Board class instantiator does support this.

The program's architecture has presentation seperation—a Good Thing. Unfortunately, the logic layer & presentation layer cannot be quickly connected because the CLI library (click) does not natively support using a list as an argument. This is sensible behaviour; CLI arguments should not be too long.

Instead, the Board state should be provided via a file argument. I've already practiced this in the SudokuSolver project and decided to focus on other learning opportunities. The interested reader can implement a file argument in Click:

https://click.palletsprojects.com/en/8.1.x/arguments/#file-arguments

## Credits

- Project idea from https://robertheaton.com/2018/07/20/project-2-game-of-life/ 

## Dependencies
Found in pyproject.toml

## Reflection
- Imports can be a pain to work with in Poetry, especially in conjuction with Pytest. Still, the automatic dependency management & consistent dev environment outweigh this negative aspect.
- Continuous integration is great. Initial setup takes time but over the long term it decreases rote work & increases confidence that the code (still) works.
- Pytest fixtures ensure consistency. However, they hide the initialization parameters. This makes it difficult and error-prone to write tests based on another python file.
- Using a GUI via bash script causes issues because there is no window attached to the terminal. I am still looking for a good cross-platform solution to this problem.


## Other

- Code formatting by Black (line-length 88):
https://black.readthedocs.io/en/stable/
- Linting using Flake8
- Imports sorted using isort
