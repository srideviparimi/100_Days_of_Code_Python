# Day 13 - Debugging 🐞🔍

## 🧠 Topics Covered
- 💻 Using Debuggers in IDEs (e.g., VS Code or PyCharm)
- 🐛 Common Types of Bugs:
  - Syntax errors
  - Indentation errors
  - Logic errors
  - Runtime exceptions
- 🔎 Using `print()` statements for debugging
- 🛠️ Strategies to fix bugs
- 🔁 Walking through code step-by-step

## 🔧 Debugging Techniques

### 1. 🐍 Using a Debugger
- Set breakpoints to **pause execution**.
- Step through lines one by one.
- Inspect variable values live.
- Identify where things go wrong before reaching the crash.

### 2. 🖨 Using `print()` Statements
- Temporarily add `print()` to check values and flow of execution.
- Use clear labels:
  ```python
  print(f"Checking value of x: {x}")
  print("Loop entered!")
### 3. 💭 Common Bugs & Fixes
Off-by-one errors in loops
Incorrect indentation
Wrong comparison operators (e.g., = vs ==)
Uninitialized variables
Mutating variables in unexpected ways
