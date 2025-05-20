# ✅ Day 37 - Advanced Authentication & Habit Tracker using Pixela API

Today, I explored **advanced authentication methods** in APIs using custom headers and the Python `requests` module. As a practical project, I built a **Habit Tracker** using the **Pixela API**, which allows users to track daily progress via beautifully visualized graphs.

## 🛠️ Project: Habit Tracker with Pixela API

### 💡 What I Built
A Python script that:
- Authenticates securely with Pixela using token-based headers.
- Creates a user account, graph, and pixel for daily habit tracking.
- Allows modification or deletion of habit entries.
## 📚 Topics Covered
### 🔐 Advanced API Authentication
- Used headers instead of basic auth or query parameters.
- Stored and used a secure token for API calls.
### 🌐 Interacting with Pixela API
- Created user accounts and graphs using POST requests.
- Added, updated, and deleted habit data (pixels) with PUT and DELETE requests.
### 📊 Habit Tracker Logic
- Tracked any recurring habit (e.g., studying, exercise, coding).
- Used formatted dates and input values to send correct data to Pixela.
## 🧠 Key Concepts
- **Custom Headers**: Authentication using custom headers (like `X-USER-TOKEN`) instead of passwords.
- **RESTful API Usage**: Applied various HTTP methods — POST, PUT, GET, DELETE.
- **Modular Code**: Split functionality into reusable functions for clarity.
- **Data Formatting**: Handled date formatting (`YYYYMMDD`) for API requests.
