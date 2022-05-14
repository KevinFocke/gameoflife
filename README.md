# Game Of Life

Library to simulate Conway's Game Of Life.

## General information

This was a project-based learning experience. My main goals for the project:

- Setup Continuous Integration environment for testing

- Practice Test-Driven-Development (Red, Green, Refactor methodology)

- Practice Object-Oriented programming (custom iterator, methods)

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
    
Run python file

    python src/gameoflife/main.py



## Credits

- Project idea from https://robertheaton.com/2018/07/20/project-2-game-of-life/ 

## Dependencies
Found in pyproject.toml

## Reflection
- Imports can be a pain to work with in Poetry, especially in conjuction with Pytest. Still, the automatic dependency management & consistent dev environment outweigh this negative aspect.
- Continuous integration is great. Initial setup takes time but over the long term it decreases rote work & increases confidence that the code (still) works.
- Pytest fixtures ensure consistency. However, they hide the initialization parameters. This makes it difficult and error-prone to write tests based on another python file.


## Other

- Code formatting by Black:
https://black.readthedocs.io/en/stable/
- Linting using Flake8
- Imports sorted using isort
