# Conduit Project

This repository contains automated tests for the RealWorld "Conduit" app hosted at https://conduit.bondaracademy.com/.

Both UI tests (using Selenium) and API tests (using the requests library) are written and executed using Pytest.

Tests are organized under tests/ui/ for Selenium-based UI tests and tests/api/ for API tests.

## Setup Instructions

```bash
git clone https://github.com/sara-tech/conduit-project
cd conduit-project
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
pip install -r requirements.txt


