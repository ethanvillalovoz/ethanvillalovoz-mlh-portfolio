# Personal Portfolio Site

A modern, extensible portfolio website built with Flask. This project showcases my background, experiences, and interests, and demonstrates dynamic web development using Python, Jinja templating, and interactive mapping.

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![Python](https://img.shields.io/badge/python-3.10-blue)
![License](https://img.shields.io/badge/license-MIT-green)

## Features

- About Me section
- Work Experience and Education
- Hobbies with images
- Interactive map of places visited
- Responsive design
- Easy to extend and customize

## Table of Contents

- [Introduction](#introduction)
- [Description](#description)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Technologies Used](#technologies-used)
- [QuickStart](#quickstart)
- [Usage](#usage)
- [Advanced Usage](#advanced-usage)
- [Configuration](#configuration)
- [Folder Structure](#folder-structure)
- [Automated Tests](#automated-tests)
- [Contribution Guidelines](#contribution-guidelines)
- [Issue & Pull Request Templates](#issue--pull-request-templates)
- [Diagrams](#diagrams)
- [SOLID Principles](#solid-principles)
- [Development Log](#development-log)

## Introduction

A personal portfolio site built with Flask. This project showcases my background, experiences, and interests.

## Description

This portfolio site features dynamic sections for About Me, Work Experience, Education, Hobbies, and an interactive map of places I’ve visited. It demonstrates Flask, Jinja templating, and modern web development practices. The site is designed to be easily extensible and contributor-friendly.

## Prerequisites

- Python 3.10+
- pip
- (Optional) [Anaconda](https://www.anaconda.com/products/distribution) for environment management

## Technologies Used

- Flask
- Jinja2
- Leaflet.js
- HTML/CSS

<!-- ## Visuals

![Homepage Screenshot](static/img/homepage_screenshot.png)
![Hobbies Page Screenshot](static/img/hobbies_screenshot.png)
![Map Screenshot](static/img/map_screenshot.png) -->

## QuickStart

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/your-repo.git
    cd your-repo
    ```

2. Create and activate a virtual environment (choose one):

   **Using Conda:**
   ```bash
   conda create -n myenv python=3.10
   conda activate myenv
   ```

   **Using venv:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the Flask app:
    ```bash
    flask run
    ```

5. Open [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your browser.

## Usage

Create a .env file using the example.env template (make a copy using the variables inside of the template)

Start flask development server
```bash
$ export FLASK_ENV=development
$ flask run
```

You should get a response like this in the terminal:
```
❯ flask run
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

You'll now be able to access the website at `localhost:5000` or `127.0.0.1:5000` in the browser! 

*Note: The portfolio site will only work on your local machine while you have it running inside of your terminal. We'll go through how to host it in the cloud in the next few weeks!* 

## Advanced Usage

- Add new hobbies, work experiences, or places by editing `app/data.py`.
- Customize templates in `app/templates/`.
- For more documentation, consider adding a `docs/` folder.

## Configuration

- Copy `.env.example` to `.env` and fill in any required environment variables.
- Example variables:
    ```
    FLASK_ENV=development
    SECRET_KEY=your_secret_key
    ```
- You can add more configuration options as your project grows.

## Folder Structure

```
app/
  __init__.py
  data.py
  templates/
  static/
tests/
README.md
requirements.txt
```

## Automated Tests

To run tests (if available):

```bash
pytest
```

*Note: Automated tests coming soon!*

<!-- ## Roadmap

- [ ] Add blog section
- [ ] Add contact form
- [ ] Improve accessibility
- [ ] Add more automated tests
- [ ] Enhance map features -->

## Contribution Guidelines

Contributions are welcome! To contribute:

- Fork the repository
- Create a new branch for your feature or bugfix
- Open a pull request describing your changes

For more details, see [CONTRIBUTING.md](CONTRIBUTING.md) (coming soon).

Please follow the code of conduct and respect the review process.

## Issue & Pull Request Templates

To help maintain consistency, this project uses GitHub’s issue and pull request templates.

- Bug reports, feature requests, and other issues should use the templates in `.github/ISSUE_TEMPLATE/`.
- Pull requests should use the template in `.github/PULL_REQUEST_TEMPLATE.md`.

If you have suggestions for improving these templates, feel free to open a PR!

## Diagrams

For architecture and workflow diagrams, this project recommends using [Mermaid](https://mermaid-js.github.io/) for easy-to-edit, code-based diagrams.

Example (replace with your own as needed):

```mermaid
flowchart TD
    A[User] -->|Visits| B(Homepage)
    B --> C{Chooses Page}
    C -->|Hobbies| D[Hobbies Page]
    C -->|Map| E[Map Page]
    C -->|About| F[About Page]
```

Add your own diagrams to help explain project structure or user journeys!

## SOLID Principles

This project aims to follow SOLID principles for better maintainability and scalability:

- **Single Responsibility Principle:** Each module or function has one responsibility.
- **Open/Closed Principle:** Code is open for extension but closed for modification.
- **Liskov Substitution Principle:** Components can be replaced with their subtypes without breaking the application.
- **Interface Segregation Principle:** Prefer small, specific interfaces over large, general ones.
- **Dependency Inversion Principle:** Depend on abstractions, not on concrete implementations.

Applying these principles helps keep the codebase clean and easy to contribute to.

## Development Log

See the `docs/` folder for a session-by-session breakdown of project progress.
