# Day 16 - Coffee Machine Using OOP ☕👩‍💻🧱

## 🔁 Refactored Project: Coffee Machine with OOP

Today, I refactored the coffee machine project from Day 15 using **Object-Oriented Programming (OOP)**. The logic is now split into classes that encapsulate data and behavior.

## 🧠 Topics Covered

- 🧱 Object-Oriented Programming (OOP)
- 🏷 Creating and using **classes and objects**
- 🧩 Encapsulation of logic into **methods**
- 🎯 Better structure and reusability
- 📦 Importing classes from separate files
- 🧾 Creating a clean and modular architecture

## 📦 Classes Created

### 1. `MenuItem`  
Represents a single menu item with:
- `name`
- `cost`
- `ingredients`

### 2. `Menu`  
Handles:
- Returning available items
- Finding a menu item by name

### 3. `CoffeeMaker`  
Handles:
- Tracking and reporting resources
- Checking if resources are sufficient
- Making coffee and deducting ingredients

### 4. `MoneyMachine`  
Handles:
- Accepting coins
- Checking if payment is sufficient
- Processing transactions
- Tracking total profit
