# GreenMiles: Eco-Commute Carbon Tracker 🌍

A purposeful Python command-line tool designed to quantify the environmental impact of daily transportation choices.

## 📌 The Problem
While most people are aware that driving contributes to carbon emissions, the data is often abstract. It is difficult for an individual to visualize how much $CO_2$ they actually save by choosing to bike, walk, or take the bus over a single week. This lack of tangible data makes it harder to stay motivated toward sustainable habits.

## 🚀 The Solution
**GreenMiles** bridges this gap by providing a simple, interactive interface to:
1. Log daily trips and transport modes.
2. Calculate real-time $CO_2$ emissions based on global averages.
3. Compare choices against a "Gas Car Baseline" to show total carbon prevented (savings).
4. Generate a formatted summary report for the session.

## 🛠️ Course Concepts Applied
This project was developed for the **Python Essentials** course and demonstrates mastery of:
* **Data Structures:** Utilizing Dictionaries for emission factors and a List of Dictionaries for session history.
* **Input Validation:** Implementing `try/except` blocks and `while` loops to ensure robust user data entry.
* **Modular Programming:** Organizing logic into distinct, reusable functions (e.g., `calculate_co2`, `get_valid_mode`).
* **String Formatting:** Using f-strings and alignment modifiers to create a clean, tabular CLI report.

## 💻 Installation & Usage

### Prerequisites
* Python 3.x installed on your machine.

### Running the Program
1. Clone this repository or download the `eco_commute.py` file.
2. Open your terminal or command prompt.
3. Navigate to the folder and run:
   ```bash
   python eco_commute.py
