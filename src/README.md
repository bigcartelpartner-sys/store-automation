# Store Automation

Daily automation for store validation, research, and outreach.

## Features

- Validate stores
- Find contact information
- Conduct customer research
- Generate personalized messages
- Send messages via email

## Setup

1. Clone the repository
2. Create virtual environment: `python -m venv venv`
3. Activate it: `venv\Scripts\activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Run: `python -m src.main`

## Project Structure

store-automation/
├── .github/
│   └── workflows/
├── src/
│   ├── main.py
│   ├── validator.py
│   ├── contact_finder.py
│   ├── research.py
│   ├── message_generator.py
│   └── delivery.py
├── config/
├── logs/
└── requirements.txt

## Usage

The automation runs daily via GitHub Actions or locally with:

python -m src.main

## License

MIT