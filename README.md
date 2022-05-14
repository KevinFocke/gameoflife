# Game Of Life

Library to simulate Conway's Game Of Life.

## General information

This is a project-based learning experience. My main goals for the project:

- Setup Continuous Integration environment for testing

- Practice Test-Driven-Development (Red, Green, Refactor methodology)

- Practice Object-Oriented programming (custom iterator, methods)

## Usage Information

How to install & run:

## Credits

- Project idea from https://robertheaton.com/2018/07/20/project-2-game-of-life/ 

## Dependencies

## Reflection
- Imports can be a pain to work with in Poetry, especially in conjuction with Pytest. Still, the automatic dependency management & consistent dev environment outweigh this negative aspect.
- Continuous integration is great. Initial setup takes time but over the long term it decreases rote work & increases confidence that the code (still) works.
- Pytest fixtures ensure consistency. However, they hide the initialization parameters. This makes it difficult and error-prone to write tests in another python file.

## Other

- Code formatting by Black:
https://black.readthedocs.io/en/stable/
- Linting using Flake8
- Imports sorted using isort
