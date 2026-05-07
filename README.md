# Project Cloak Access 🧙‍♂️

Welcome to **Project Cloak Access**, an educational project that demonstrates the power of Computer Vision using OpenCV. This project implements a virtual "Invisibility Cloak" effect, similar to the one seen in Harry Potter.

## 📚 Project Philosophy

This repository is designed with an educational-first approach. Every module contains **formal definitions** of key Computer Vision and Software Engineering concepts directly within the code.

## 🛠️ Features

- **01_Basics**: A simple, single-script implementation to understand the core logic.
- **02_Intermediate**: Includes a tuning tool with trackbars to calibrate HSV values for any environment.
- **03_Advanced**: A modular, object-oriented version using structured logging and centralized configuration.
- **04_Web_Interface**: A web-based interface built with Flask to stream the invisibility effect to a browser.
    - **Interactive Features**: Real-time background capture via AJAX and video export/download functionality.
- **Utilities**: Custom logger and SQLite database manager for tracking application state and session history.
- **Configuration**: Centralized settings for easy experimentation.

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- A working webcam

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/kunalpatil29th/project-cloak-accesss.git
   cd project-cloak-accesss
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Scripts

- **Basics**:
  ```bash
  python 01_Basics/simple_cloak.py
  ```
- **Intermediate (Tuning)**:
  ```bash
  python 02_Intermediate/cloak_with_tuning.py
  ```
- **Advanced (Modular)**:
  ```bash
  python 03_Advanced/advanced_cloak.py
  ```
- **Web Interface**:
  ```bash
  python 04_Web_Interface/app.py
  ```
  Then open your browser and visit [http://localhost:5000/](http://localhost:5000/)

## 📂 Project Structure

```
project-cloak-accesss/
├── 01_Basics/                  # Simple, single-script implementation
│   └── simple_cloak.py
├── 02_Intermediate/            # With HSV tuning tool
│   └── cloak_with_tuning.py
├── 03_Advanced/                # Modular, object-oriented version
│   └── advanced_cloak.py
├── 04_Web_Interface/           # Flask web application
│   ├── app.py
│   ├── templates/
│   │   ├── index.html
│   │   └── history.html
│   └── static/
│       ├── css/
│       │   └── style.css
│       └── js/
│           └── main.js
├── config/                     # Centralized configuration
│   └── settings.py
├── utils/                      # Utility modules
│   ├── logger.py
│   └── db_manager.py
├── tests/                      # Unit tests
│   └── test_cloak.py
├── docs/                       # Documentation
├── .github/                    # GitHub templates and workflows
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md
│   │   └── feature_request.md
│   ├── workflows/
│   │   └── tests.yml
│   └── PULL_REQUEST_TEMPLATE.md
├── setup.py                    # Package setup
├── requirements.txt            # Dependencies
├── CONTRIBUTING.md             # Contribution guidelines
├── CODE_OF_CONDUCT.md          # Code of conduct
└── README.md                   # This file
```

## 🛠️ Development

### Running Tests

```bash
python -m unittest discover tests -v
```

### Linting and Formatting

```bash
# Format code with Black
black .

# Sort imports with isort
isort .

# Lint with flake8
flake8 .

# Type check with mypy
mypy .
```

## 🔧 Troubleshooting

### Camera Issues
- If your webcam isn't detected, try changing the `CAMERA_ID` in `config/settings.py` (try 0, 1, 2, etc.)
- Ensure no other applications are using your webcam

### Color Detection Issues
- Use the Intermediate version (`02_Intermediate/cloak_with_tuning.py`) to tune HSV values for your environment
- Adjust lighting - make sure your cloak color is well-lit
- The default color is red, but you can change it in the config

### Web Interface Issues
- Make sure you have all dependencies installed (`pip install -r requirements.txt`)
- Check that port 5000 is available on your system

## 🧠 Concepts Covered

- **HSV Color Model**: Hue, Saturation, Value.
- **Image Masking**: Isolating regions of interest.
- **Morphological Operations**: Opening and Dilation for noise reduction.
- **Background Subtraction**: The core technique for the invisibility effect.
- **Modular Programming**: Organized code structure for scalability.
- **Web Development**: Building interfaces with Flask and Jinja2.
- **Relational Databases**: Managing persistent data with SQLite.

## 🤝 Contributing

Contributions are welcome! This project follows a granular commit strategy to maintain a clear history of incremental improvements.

---
*Created for educational purposes by Kunal Patil.*
