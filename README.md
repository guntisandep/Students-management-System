# 🎓 Student Management System

A simple web application for managing student records, built with **Python**, **FastAPI**, **SQLite**, and **Jinja2 templates**. It provides the core CRUD workflow through a browser-based interface.

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Web%20framework-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![SQLite](https://img.shields.io/badge/Database-SQLite-003B57?logo=sqlite&logoColor=white)](https://www.sqlite.org/)

## Table of contents

- [Overview](#overview)
- [Features](#features)
- [Technology stack](#technology-stack)
- [Project structure](#project-structure)
- [Getting started](#getting-started)
- [Usage](#usage)
- [Database](#database)
- [Screenshots](#screenshots)
- [Future improvements](#future-improvements)
- [Author](#author)

## Overview

The Student Management System is a beginner-friendly web project for creating, viewing, editing, and deleting student records. FastAPI handles the application routes, SQLite stores the data, and Jinja2 renders the HTML pages.

## Features

| Feature | Description |
|---|---|
| Create student records | Add student information through a web form. |
| View student records | Browse the student list on the home page. |
| View student details | Open a page with information for an individual student. |
| Update records | Edit an existing student's information. |
| Delete records | Remove a student record. |
| SQLite storage | Persist student data in a local SQLite database. |
| Server-rendered pages | Display dynamic content with HTML and Jinja2 templates. |

## Technology stack

| Technology | Role |
|---|---|
| [Python](https://www.python.org/) | Application programming language |
| [FastAPI](https://fastapi.tiangolo.com/) | Web framework and application routes |
| [SQLite](https://www.sqlite.org/) | Local database |
| [Jinja2](https://jinja.palletsprojects.com/) | HTML template rendering |
| HTML / CSS | Page structure and styling |
| [Uvicorn](https://www.uvicorn.org/) | Development application server |

## Project structure

```text
Students-management-System/
├── main.py                 # FastAPI application and backend logic
├── students.db             # SQLite database (created or used by the app)
└── templates/
    ├── add_student.html    # Form for adding a student
    ├── edit_student.html   # Form for editing a student
    ├── home.html           # Student list / home page
    └── single-std.html     # Individual student details
```

> A virtual environment (`venv/`) may also be present locally. It is not required to be committed to the repository; create your own by following the setup steps below.

## Getting started

### Prerequisites

- Python 3
- `pip`
- Git

### 1. Clone the repository

```bash
git clone https://github.com/guntisandep/Students-management-System.git
cd Students-management-System
```

### 2. Create and activate a virtual environment

**Windows (PowerShell):**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**Windows (Command Prompt):**

```bat
python -m venv venv
venv\Scripts\activate.bat
```

**macOS / Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install fastapi uvicorn jinja2 python-multipart
```

### 4. Start the development server

```bash
uvicorn main:app --reload
```

### 5. Open the application

Visit [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

To stop the server, press `Ctrl+C` in the terminal.

## Usage

Use the pages in the application to add students, browse the list, view individual records, edit details, or delete records. The exact fields and navigation depend on the implementation in `main.py` and the templates.

## Database

Student records are stored in a local SQLite database named `students.db`. SQLite does not require a separate database server. Keep a backup of this file if you need to preserve local records.

## Screenshots

Screenshots can be added here to show the home page, add-student form, student details, and edit form.

<!-- Replace this note with images, for example:
![Student list page](docs/images/student-list.png)
-->

## Future improvements

- Add student search and filtering.
- Add authentication and authorization.
- Improve form validation and error messages.
- Add pagination for larger student lists.
- Improve responsive styling and accessibility.
- Add automated tests and dependency management.

## Author

**Gunti Sandeep** — Python Developer (Fresher)

- GitHub: [@guntisandep](https://github.com/guntisandep)
- Project: [Students-management-System](https://github.com/guntisandep/Students-management-System)

---

⭐ If you find this project useful, consider giving the repository a star or sharing feedback.
