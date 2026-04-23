# Project Cloak Access 🧙‍♂️

Welcome to **Project Cloak Access**, an educational project that demonstrates the power of Computer Vision using OpenCV. This project implements a virtual "Invisibility Cloak" effect, similar to the one seen in Harry Potter.

## 📚 Project Philosophy

This repository is designed with an educational-first approach. Every module contains **formal definitions** of key Computer Vision and Software Engineering concepts directly within the code.

## 🛠️ Features

- **01_Basics**: A simple, single-script implementation to understand the core logic.
- **02_Intermediate**: Includes a tuning tool with trackbars to calibrate HSV values for any environment.
- **03_Advanced**: A modular, object-oriented version using structured logging and centralized configuration.
- **04_Web_Interface**: A web-based interface built with Flask to stream the invisibility effect to a browser.
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
