# OPTIMIZATION-MODEL

COMPANY : CODTECH IT SOLUTIONS

NAME : HRIDYA MOHANAN

INTERN ID : CTO4DF2524

DOMAIN : DATA SCIENCE

DURATION : 4 WEEKS

MENTOR : NEELA SANTOSH

# 🧮 Optimization Model Project - Linear Programming with PuLP

This project demonstrates how to solve a real-world business optimization problem using *Linear Programming (LP)* with the PuLP library in Python.

---

## 🎯 Objective

To determine the optimal number of two products to manufacture in order to *maximize total profit*, subject to resource constraints such as machine time and labor.

---

## 📌 Problem Statement

A company produces two products: *Product A* and *Product B*.

- Each unit of *Product A* requires:
  - 2 hours of machine time
  - 1 hour of labor
- Each unit of *Product B* requires:
  - 1 hour of machine time
  - 1 hour of labor

Available Resources:
- Maximum *100 machine hours*
- Maximum *80 labor hours*

Profit:
- ₹20 per unit of Product A  
- ₹60 per unit of Product B

🔎 *Goal*: Maximize profit without exceeding available resources.

---

## 🛠 Tools Used

- Python 3.x
- pulp==3.2.1 – Linear Programming in Python

---

## 📁 Project Structure

| File                   | Description                                           |
|------------------------|-------------------------------------------------------|
| optimization_model.py| Python script that builds and solves the LP problem  |
| requirements.txt     | Required Python packages                              |
| README.md            | Project overview and instructions (this file)         |

---

## 🧠 LP Formulation

*Decision Variables:*
- Let x = units of Product A  
- Let y = units of Product B
