# E-Commerce QA Automation Testing

## Project Overview

This project automates functional testing of an e-commerce website using Python, Selenium WebDriver, and Pytest. It tests important user workflows, including login, shopping cart operations, and checkout validation.

The project uses [SauceDemo](https://www.saucedemo.com/) as the practice website.

## Technologies Used

- Python
- Selenium WebDriver
- Pytest
- pytest-html
- Google Chrome
- Git and GitHub

## Test Scenarios

### Login Testing
- Verify login with valid credentials.
- Verify login with invalid credentials.
- Verify validation for empty login fields.

### Shopping Cart Testing
- Verify that a product can be added to the cart.
- Verify that a product can be removed from the cart.

### Checkout Testing
- Verify checkout with valid customer details.
- Verify validation when the first name is empty.
- Verify validation when the last name is empty.
- Verify validation when the postal code is empty.

## Project Structure

```text
codingmart-qa-automation/
├── conftest.py
├── tests/
│   ├── test_login.py
│   ├── test_cart.py
│   └── test_checkout.py
├── reports/
│   └── report.html
└── README.md
```

## Setup and Installation

1. Install Python and Google Chrome.
2. Clone or download this repository.
3. Open a terminal in the project directory.
4. Create and activate a virtual environment if needed.
5. Install the required packages:

```bash
python -m pip install selenium pytest pytest-html
```

## Run the Tests

Run all automated tests:

```bash
python -m pytest -v
```

Run a specific test file:

```bash
python -m pytest tests/test_login.py -v
```

## Generate an HTML Test Report

Run the tests and generate a self-contained HTML report:

```bash
python -m pytest -v --html=reports/report.html --self-contained-html
```

Open `reports/report.html` in a web browser to view the test results.

## Current Test Coverage

The initial suite contains nine test cases covering login, cart operations, and checkout validation.

## Learning Objectives

- Automate browser interactions using Selenium.
- Write and execute test cases using Pytest.
- Use explicit waits to handle dynamic page elements.
- Validate application behavior using assertions.
- Generate HTML test reports.

## Disclaimer

This is a learning and portfolio project performed on a public practice website. It is not an official test suite for SauceDemo.