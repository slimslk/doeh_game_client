# DoEH: Domains of Endless Hunger

![Python](https://img.shields.io/badge/python-3.12-blue)
![uv](https://img.shields.io/badge/package%20manager-uv-purple)

## Project Description

This project is a client for a **pseudo-turn-based online roguelike game**, where every action is limited by a specific time. The goal at the current stage of the game is simple: **survive as long as possible**.

### Game Mechanics

- Every tick, the player loses **1 unit of hunger**. Once hunger reaches zero, **health points start to decrease**.
- Players can **collect and use various items** to get different effects.
- You can **attack other players**, and upon death, **all items drop from the player**.

The client allows players to connect seamlessly to the game and experience the strategic survival mechanics in real time. Each decision counts, making every tick a matter of life and death.

---

# Table of Contents

* [Quick Start](#quick-start)
* [Requirements](#requirements)
* [Installation](#installation)
* [Running the Application](#running-the-application)
* [Development](#development)
* [License](#license)
* [Troubleshooting](#troubleshooting)

---

# Quick Start

If you already have **Python 3.12** and **uv** installed, run:

```bash
git clone git@github.com:slimslk/doeh_game_client.git
cd doeh_game_client
uv sync
uv run main.py
```

---

# Requirements

* Python **3.12**
* **uv** package manager

---

# Installation

Follow these steps if you are running the project on a clean machine.

## 1. Install Python 3.12

Download Python from the official website:

https://www.python.org/downloads/

Run the installer and **enable "Add Python to PATH"** during installation.

Verify the installation:

```bash
python --version
```

Expected output:

```bash
Python 3.12.x
```

---

## 2. Install uv

Install `uv` using pip:

```bash
pip install uv
```

Verify installation:

```bash
uv --version
```

---

## 3. Clone the Repository

```bash
git clone https://github.com/slimslk/doeh_game_client.git
cd doeh_game_client
```

---

## 4. Install Project Dependencies

Create the virtual environment and install dependencies:

```bash
uv sync
```

This command will:

* create a virtual environment
* install dependencies from `pyproject.toml`
* prepare the project environment

---

# Running the Application

Start the application:

```bash
uv run main.py
```

Replace `main.py` with the correct entry point if your project uses a different file.


---

# Development

Run the project during development:

```bash
uv run main.py
```

If dependencies were updated in `pyproject.toml`, run:

```bash
uv sync
```

---

# License

**Copyright © 2024-2026 Dmytro Kuzavkov (slimslk). All rights reserved.**

This software and its associated files are **proprietary** and confidential. 
Unauthorized copying, distribution, or modification of this code, via any medium, is strictly prohibited. 

The source code is provided on GitHub for **portfolio review and educational purposes only**. 
If you wish to use any part of this project for commercial purposes or public distribution, please contact the author at d.kuzavkov@gmail.com.

---

# Troubleshooting

## Python version issues

Check Python version:

```bash
python --version
```

The project requires **Python 3.12**.

---

## uv command not found

Install `uv`:

```bash
pip install uv
```

Restart the terminal if necessary.
