# Game Of Life

Simulates Conway's Game Of Life. Interact using a GUI.

## General information

This is a project-based learning experience. My main goals for the project:

- Setup Continuous Integration environment

- Practice Test-Driven-Development (Red, Green, Refactor methodology)

- Practice Object-Oriented programming.

- Create a GUI & automate GUI testing
https://wiki.python.org/moin/PyQt/GUI_Testing
https://github.com/pytest-dev/pytest-qt/#pytest-qt
https://martinfowler.com/eaaDev/uiArchs.html
 
 - Modelling diagrams

- Make program self-excecutable (Frozen python binaries)

## Usage Information

How to install & run:

## Credits

- Project idea from https://robertheaton.com/2018/07/20/project-2-game-of-life/ 
- Object structure inspired by https://robertheaton.com/2019/11/30/pfab2-how-to-structure-your-programs/ 
- Multi-platform auto release tutorial by https://data-dive.com/multi-os-deployment-in-cloud-using-pyinstaller-and-github-actions (didn't work, but got me started on the right track)

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
