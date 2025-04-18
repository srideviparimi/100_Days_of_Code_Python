# 🔥 Day 50 - Automating Tinder Profile Likes with Selenium

Today, I used **Selenium** to build an automation script that likes 100 profiles on **Tinder**. This project pushed me to work with more dynamic and interactive web pages, handle popups, and simulate real user behavior in a swipe-based app.
## 🛠️ Project: Tinder Auto-Liker Bot

### 💡 What I Built
An automation tool that:
- Launches a browser and logs into Tinder (via Facebook or phone number login).
- Handles initial popups (location, notifications, cookies).
- Clicks the “Like” button on profiles.
- Repeats the process until 100 profiles are liked.
## 📚 Topics Covered

### 🌐 Tinder Automation with Selenium
- Navigated through login screens and allowed permissions/popups.
- Used Selenium to identify and click the like button reliably.
- Implemented a counter to limit the action to 100 profiles.
### 🛑 Handling Popups & Interruptions
- Dismissed location access and notification prompts.
- Skipped matches or other modal popups during the automation flow.
### ♻️ Looping & Delays
- Repeated the like action using a loop.
- Included timed delays to mimic human behavior and reduce the risk of being flagged.
## 🧠 Key Concepts

- **Browser Popups**: Handled cookie banners, modals, and permission requests.
- **Element Identification**: Located the like button using class names, XPath, or button roles.
- **Looping Logic**: Used a loop to repeat the action exactly 100 times.
- **Waits & Delays**: Used `WebDriverWait`, `time.sleep()` to wait for elements and avoid detection.
