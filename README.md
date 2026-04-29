# DoEH: Domains of Endless Hunger

![Python](https://img.shields.io/badge/python-3.12-blue)
![uv](https://img.shields.io/badge/package%20manager-uv-purple)
![License](https://img.shields.io/badge/license-MIT-green)

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
* [Project Structure](#project-structure)
* [Development](#development)
* [License](#license)
* [Troubleshooting](#troubleshooting)

---

# Quick Start

If you already have **Python 3.12** and **uv** installed, run:

```bash
git clone https://github.com/slimslk/npc_crawler_client.git
cd npc_crawler_client
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
git clone https://github.com/slimslk/npc_crawler_client.git
cd npc_crawler_client
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

This project is licensed under the **MIT License**.

**What this means:**

* You can use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the project.
* You must include the original copyright notice and license in all copies.
* There are **no restrictions** on commercial or private use.

This makes it perfect for personal open-source projects or sharing with others freely.

Full MIT License text:

```text
MIT License

Copyright (c) 2026 Your Name

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

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
