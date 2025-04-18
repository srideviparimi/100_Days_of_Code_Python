# 🔐 Day 49 - Automating LinkedIn Job Applications with Selenium

Today, I built a Python script using **Selenium** to automate the process of logging into **LinkedIn** and applying for jobs. This was a great way to deepen my understanding of browser automation by interacting with a real-world web application.

## 🛠️ Project: LinkedIn Auto-Apply Bot

### 💡 What I Built
An automation script that:
- Launches a browser and navigates to the LinkedIn login page.
- Enters login credentials securely.
- Navigates to job listings with the "Easy Apply" filter.
- Automatically applies to jobs by interacting with forms/buttons.

## 📚 Topics Covered

### 🌐 Selenium Automation Recap
- Automating browser tasks using Python and Selenium.
- Logging into secure websites with form handling.

### 🔐 Handling Login Flows
- Using `find_element()` to locate username and password fields.
- Handling login buttons and redirection.

### 💼 Job Application Automation
- Navigating job listings using search filters and URLs.
- Identifying and interacting with "Easy Apply" buttons.
- Handling application popups and multi-step forms.

## 🧠 Key Concepts
- **Secure Web Automation**: Simulating login securely (with environment variables or protected input).
- **Dynamic Element Handling**: Managing elements that load asynchronously or change based on user input.
- **Selenium Waits**: Using `WebDriverWait` and `expected_conditions` to wait for elements to load.
- **Form Interaction**: Filling input fields, selecting dropdowns, and submitting forms programmatically.
