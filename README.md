# ohtuvarasto

[![CI](https://github.com/kiiamantyla/ohtuvarasto/actions/workflows/main.yml/badge.svg)](https://github.com/kiiamantyla/ohtuvarasto/actions/workflows/main.yml)

[![codecov](https://codecov.io/github/kiiamantyla/ohtuvarasto/graph/badge.svg?token=QW8WBWKVJH)](https://codecov.io/github/kiiamantyla/ohtuvarasto)

## Description

A web-based warehouse management application built with Flask. Manage multiple warehouses and their products through a simple web interface.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/kiiamantyla/ohtuvarasto.git
   cd ohtuvarasto
   ```

2. Install dependencies using Poetry:
   ```bash
   poetry install
   ```

   Or using pip:
   ```bash
   pip install flask
   ```

## Running the Application

1. Navigate to the src directory:
   ```bash
   cd src
   ```

2. Run the Flask application:
   ```bash
   python app.py
   ```

3. Open your browser and go to:
   ```
   http://127.0.0.1:5000
   ```

## Running Tests

```bash
python -m pytest src/tests/
```

## Features

- Create, edit, and delete warehouses
- Add, edit, and delete products within warehouses
- View all warehouses and their products
- Simple and clean web interface
