# Material Property Calculator

A Python desktop application built with **Tkinter** that calculates
three important material properties:

-   Stress
-   Strain
-   Linear Thermal Expansion

This project also includes automated unit testing using **pytest** to
verify calculation accuracy.

------------------------------------------------------------------------

## 📌 Features

### 1️⃣ Stress Calculation

**Formula:**

Stress = Force / Area

-   Input: Force (N), Area (m²)
-   Output: Stress (N/m²)

------------------------------------------------------------------------

### 2️⃣ Strain Calculation

**Formula:**

Strain = (Final Length − Original Length) / Original Length

-   Input: Original Length (m), Final Length (m)
-   Output: Strain (dimensionless)

------------------------------------------------------------------------

### 3️⃣ Linear Thermal Expansion

**Formula:**

ΔL = αLΔT

Where: - α = Coefficient of linear expansion
- L = Original length
- ΔT = Temperature change

-   Input: Length (m), Expansion coefficient (α), Temperature change
    (°C)
-   Output: Change in length (m)

------------------------------------------------------------------------

## 🖥️ Graphical User Interface

The program provides:

-   Clearly labeled input fields
-   A **Calculate** button
-   A **Clear** button
-   Instructional guidance
-   A result display section

The interface is built using Python's built-in `tkinter` library.

------------------------------------------------------------------------

## 🧪 Unit Testing

The project includes test functions for:

-   `calculate_stress()`
-   `cal_strain()`
-   `calculate_thermal_expansion()`

Floating-point results are verified using:

``` python
from pytest import approx
```

### To run tests:

``` bash
pytest
```

or

``` bash
python test_GUI.py
```

------------------------------------------------------------------------

## 🛠️ Installation & Setup

### 1️⃣ Clone the Repository

``` bash
git clone https://github.com/kingsley-byu/wdd131.git
cd wdd131
```

### 2️⃣ Install pytest (if needed)

``` bash
pip install pytest
```

### 3️⃣ Run the Program

``` bash
python GUI.py
```

------------------------------------------------------------------------

## 📂 Project Structure

    wdd131
    │
    ├── GUI.py
    ├── test_GUI.py
    └── README.md

------------------------------------------------------------------------

## ⏱️ Development Log

  Day         Task                                 Time (hours)
  ----------- ------------------------------------ ----------------
  Mon         Planned GUI layout & formulas        2.5
  Tue         Built Tkinter interface              4.0
  Wed         Implemented calculations             3.0
  Thu         Writing test functions & debugging   2.0
  Sat         Writing docstrings & cleanup         2.0
  **Total**                                        **13.5 hours**

------------------------------------------------------------------------

## 🎯 Skills Demonstrated

-   Python function design
-   GUI development with Tkinter
-   Exception handling
-   Unit testing with pytest
-   Floating-point precision handling
-   Code documentation\
-   Basic software project structure

------------------------------------------------------------------------

## 🚀 Future Improvements

-   Add dropdown menu for material selection
-   Add unit conversion (mm ↔ m, °C ↔ K)
-   Improve GUI styling
-   Add input validation feedback
-   Export results to a file

------------------------------------------------------------------------

## 👤 Author

Kingsley osaruyi
GitHub: kingsley-byu
