# TickTick: A Simple and Smart Reminder App

**TickTick** is a simple and user-friendly reminder app designed to keep you on top of your tasks effortlessly. Whether you need a quick notification or an alarm to alert you, TickTick ensures you never miss anything important.

---
    #### Video Demo:  https://youtu.be/tQHXxj6Xbs8
---

## 🚀 Features

- **Task Scheduling**: Add tasks with a name, time interval, and notification type.
- **Notification Options**:
  - **Desktop Notification**: Subtle reminders via the `pync` library.
  - **Alarm Sound**: Audible alerts using the `pygame` library.
- **Flexible Time Input**: Accepts time in minutes (e.g., `30`) or hours:minutes format (e.g., `1:15`).
- **Simple Interface**: Intuitive design built with **Streamlit** for quick and easy task management.

---

## 📋 How It Works

1. Enter the task name.
2. Specify the time interval (in minutes or hours:minutes format).
3. Select the type of notification:
   - **Notification**: Receive a desktop notification.
   - **Alarm**: Play an alarm sound.
4. Click "Add Task" to schedule your task.
5. TickTick will remind you at the right time!

---

## 🛠️ Installation and Setup

### Prerequisites
- Python 3.9+
- pip package manager

### Installation Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Mrmanticore/TickTick.git
   cd TickTick

Create and Activate a Virtual Environment (optional)

```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
pip install -r requirements.txt
```
pip install -r requirements.txt
```

Run the App
    ```bash
streamlit run project.py

    ```