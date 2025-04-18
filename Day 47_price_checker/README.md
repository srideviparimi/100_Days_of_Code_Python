# 💰 Day 47 - Automatic Price Checker with Email Alert

Today, I created an **Automatic Price Checker** using Python that scrapes product prices from **Amazon**. When the price drops below a target value, it automatically sends an **email alert** using `smtplib`. This project was a great combination of **web scraping** and **email automation**.
## 🛠️ Project: Amazon Price Tracker

### 💡 What I Built
A Python script that:
- Fetches a product’s page on Amazon.
- Extracts the current price using **BeautifulSoup**.
- Compares it to a target price set by the user.
- Sends an email notification if the price is lower than the target.
## 📚 Topics Covered
### 🌐 Web Scraping with BeautifulSoup
- Fetched HTML content of a product page.
- Parsed elements like product name and price using tag selectors and classes.
### 📉 Price Monitoring
- Extracted numeric value from price strings.
- Used conditional logic to check if price is below the target.
### 📧 Email Notification with smtplib
- Logged into an SMTP server (like Gmail).
- Sent an automated email containing product details and the current price.
## 🧠 Key Concepts
- **HTTP Requests**: Used the `requests` module to fetch page data.
- **HTML Parsing**: BeautifulSoup to navigate and extract HTML elements.
- **Automation Trigger**: Conditional statements to trigger email only when price is lower.
- **Email Sending**: Used `smtplib` to securely send an alert with product info and link.
