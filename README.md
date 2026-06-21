# Python API Test Framework

![CI](https://github.com/HSC-git-space/python-api-test-framework/actions/workflows/ci.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.11-blue)
![pytest](https://img.shields.io/badge/tested%20with-pytest-orange)

This is my first Python-based API test automation framework, built after completing five Java automation frameworks — Selenium, REST Assured, Cucumber, JMeter, and Playwright. The goal was to understand how familiar automation concepts translate into Python's ecosystem and to build something structured.

The framework runs against JSONPlaceholder (https://jsonplaceholder.typicode.com), a free public REST API that simulates a real backend with users, posts, and comments. No authentication or local server setup is required, which made it a practical choice for focusing on framework architecture rather than environment configuration.

## Why I Built This

I come from a Java automation background. This repo is the start of a deliberate Python track alongside that Java foundation.

Python is the dominant language across AI and ML tooling, making it an important skill for the direction I want to pursue. My longer term goal is AI Quality Engineering — testing LLM outputs, prompt regression, hallucination detection. This repo is the first step in building that track, starting with API testing fundamentals before moving into data-driven and AI testing frameworks.

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.11 | Core language |
| pytest | Test runner — Python's equivalent of TestNG |
| requests | HTTP client — lightweight, mature, widely adopted in Python API testing |
| Pydantic | Response schema validation — Python's equivalent of POJOs with built-in validation |
| jsonschema | JSON schema validation |
| pytest-html | HTML test reporting |
| allure-pytest | Allure reporting integration |
| GitHub Actions | CI pipeline — runs on every push to master |

## Framework Features

- CRUD API automation across Users and Posts resources
- Shared BaseClient with reusable HTTP session
- Endpoint abstraction layer per resource
- Pydantic response validation with nested model support
- JSON schema validation
- Shared pytest fixtures via conftest.py
- Smoke, regression, and negative test markers
- HTML reporting via pytest-html
- Allure reporting integration
- GitHub Actions CI on every push to master

## Why requests

The requests library is lightweight, mature, and widely adopted in Python API testing. It integrates naturally with pytest fixtures and provides a clean interface for managing sessions, headers, and timeouts. It was the straightforward choice  well documented, no unnecessary abstraction, and the closest Python equivalent to what REST Assured provides in Java.

## Architecture

    python-api-test-framework/
    |
    +-- api/
    |   +-- base_client.py     # Core HTTP client — session, headers, timeout
    |   +-- endpoints.py       # Endpoint definitions per resource
    |
    +-- models/
    |   +-- user_model.py      # Pydantic schema for User resource
    |   +-- post_model.py      # Pydantic schema for Post resource
    |
    +-- tests/
    |   +-- test_users.py      # CRUD tests for Users API
    |   +-- test_posts.py      # CRUD tests for Posts API
    |   +-- test_negative.py   # Negative and edge case tests
    |
    +-- config/
    |   +-- config.py          # Base URL, headers, timeout config
    |
    +-- conftest.py            # Shared pytest fixtures
    +-- pytest.ini             # pytest configuration and markers
    +-- requirements.txt       # Project dependencies

## Framework Execution Flow

    Tests
      |
    Fixtures (conftest.py)
      |
    Endpoint Classes (endpoints.py)
      |
    BaseClient (base_client.py)
      |
    requests Session
      |
    JSONPlaceholder API
      |
    Response
      |
    Pydantic Validation
      |
    Assertions

Each layer has a single responsibility. Tests do not know how HTTP calls are made. The base client does not know what endpoints exist. Models do not know what tests are asserting. This separation makes the framework easier to extend and easier to debug when something breaks.

## Design Decisions

**Why a base client?**
I did not want to repeat base URL, headers, and timeout in every test. BaseClient sets those once and every endpoint class inherits from it. Same reasoning as SpecBuilder in REST Assured  configure once, reuse everywhere. If the base URL changes, one file changes.

**Why Pydantic?**
In Java I used POJOs to map API responses. Pydantic does the same but also validates field types automatically. If the API returns a string where an integer is expected, Pydantic throws before my assertion even runs. This provides stronger validation guarantees than a plain POJO.

**Why conftest.py at root?**
Fixtures defined here are available to every test file without imports. pytest picks them up by convention. Equivalent of a shared BeforeClass setup in TestNG but scoped to the entire test session.

**Why markers?**
Not every test needs to run every time. Smoke tests run fast and catch big breaks. Regression runs the full suite. Negative tests verify error handling separately. Markers let me run the right subset without touching code.

**Why session scope on fixtures?**
Creating a new HTTP client for every single test is wasteful. Session scope means one client is created at the start of the test run and shared across all tests. Faster execution, less setup noise.

## Testing Strategy

Each test validates one or more of the following:

- HTTP status code — correct response code for the operation
- Response payload — expected fields present in the response body
- Response schema — Pydantic model validates field types and structure
- Field values — specific assertions where the value matters
- CRUD coverage — create, read, update, delete per resource
- Negative scenarios — 404 handling, empty payloads, missing fields

## Quick Start

    git clone https://github.com/HSC-git-space/python-api-test-framework.git
    cd python-api-test-framework

    python -m venv .venv
    .venv\Scripts\Activate.ps1

    pip install -r requirements.txt

    pytest

## Running Tests

    # Run all tests
    pytest

    # Run smoke tests only
    pytest -m smoke

    # Run regression tests only
    pytest -m regression

    # Run negative tests only
    pytest -m negative

    # Run with HTML report
    pytest --html=reports/report.html

## CI Pipeline

Every push to master triggers a GitHub Actions workflow running inside a clean Ubuntu environment with Python 3.11. The workflow installs dependencies, executes the full pytest suite, and uploads the HTML report as a build artifact. Running inside a clean environment on every push confirms the framework is not dependent on local machine state and that any dependency or configuration issue is caught before it reaches the main branch.

## Framework Statistics

- 14 automated tests
- 3 test modules
- Full CRUD coverage across Users and Posts
- Negative test suite covering 404, empty payload, and missing fields
- HTML report generated on every run
- CI pipeline running on GitHub Actions

## Test Coverage

| Test File | Tests | Coverage |
|-----------|-------|---------|
| test_users.py | 5 | GET all, GET by ID, POST, PUT, DELETE |
| test_posts.py | 5 | GET all, GET by ID, POST, PUT, DELETE |
| test_negative.py | 4 | 404 handling, empty payload, missing fields |

## Report

Screenshot of pytest-html report to be added here.

The HTML report is also available as a build artifact in the GitHub Actions tab after every run.

## Known Limitations and What is Next

This framework covers the fundamentals. A few things I would improve in a production context:

- No authentication layer. JSONPlaceholder does not require it but real APIs do. Next iteration will add Bearer token and Basic auth support in BaseClient.
- Tests run sequentially. pytest-xdist would handle parallel execution.
- Negative test coverage is basic. A real suite would cover rate limiting, malformed JSON, auth failures, and timeout scenarios.
- No environment switching. config.py hardcodes one base URL. A proper setup would support dev, staging, and prod via environment variables.

These are deliberate next steps, not oversights.
