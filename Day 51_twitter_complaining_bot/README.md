# 🐦 Day 51 - Twitter Complaining Bot (Internet Speed Test)

Today, I built a **Twitter Complaining Bot** using Python and Selenium that automatically checks my internet speed and posts a tweet (on X) if the speed is lower than what's promised. This project involved organizing the code using Python **classes**, and combining real-time data fetching with browser automation.
## 🛠️ Project: Internet Speed Complaint Bot

### 💡 What I Built
A Python script that:
- Initializes a Selenium web driver using a class.
- Checks current internet download and upload speed using an online speed test tool.
- Compares the actual speed to the promised one.
- Logs into Twitter (X) and posts a complaint tweet if the speed is below expectations.
## 📚 Topics Covered

### ⚙️ Python OOP with Classes
- Encapsulated the bot logic inside a class with methods for each task.
- Used constructor `__init__()` to initialize the driver and variables.
### 🌐 Internet Speed Check
- Automated visiting a speed test website.
- Extracted download and upload speed using Selenium.
### 🐦 Twitter (X) Automation
- Logged into X using Selenium.
- Composed and posted a tweet with the speed difference.
## 🧠 Key Concepts

- **Class-Based Structure**: Organized the script using Python classes for better readability and reuse.
- **Selenium WebDriver**: Used to navigate both the speed test and Twitter/X.
- **Web Scraping + Automation**: Combined scraping live speed test data and automating a tweet.
