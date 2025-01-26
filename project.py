import streamlit as st
from datetime import datetime, timedelta
import time
import threading
from pync import Notifier
import pygame

# In-memory storage for tasks
tasks = []

def schedule_task(task_name, time_delta, notify_type):
    """Schedules a task with notification or alarm."""
    task_time = datetime.now() + timedelta(seconds=int(time_delta))
    threading.Thread(target=check_and_alert, args=(task_name, task_time, notify_type)).start()

    # Save the task details
    tasks.append({
        "task_name": task_name,
        "task_time": task_time.strftime("%Y-%m-%d %H:%M:%S"),
        "notify_type": notify_type,
        "status": "Scheduled"
    })

def check_and_alert(task_name, task_time, notify_type):
    """Checks for the task time and alerts based on the type."""
    while datetime.now() < task_time:
        time.sleep(1)

    # Update task status to "Completed"
    for task in tasks:
        if task["task_name"] == task_name and task["task_time"] == task_time.strftime("%Y-%m-%d %H:%M:%S"):
            task["status"] = "Completed"
            break

    if notify_type == "Notification":
        Notifier.notify(f"Task: {task_name} is due!", title="Reminder")
    elif notify_type == "Alarm":
        pygame.mixer.init()
        sound_file = "beep.mp3"  # Replace with your alarm file
        pygame.mixer.music.load(sound_file)
        for _ in range(3):
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                time.sleep(1)

def add_task(task_name, task_time_input, notify_type):
    """Adds a task with time input as minutes or hours:minutes."""
    if not task_name or not task_time_input or not notify_type:
        st.error("All fields are required!")
        return

    try:
        if ":" in task_time_input:  
            hours, minutes = map(int, task_time_input.split(":"))
            time_delta = (hours * 60 + minutes) * 60  
        else:  
            minutes = int(task_time_input)
            time_delta = minutes * 60  

        schedule_task(task_name, time_delta, notify_type)
        st.success(f"Task '{task_name}' scheduled successfully!")
    except ValueError:
        st.error("Time must be in minutes (MM) or hours:minutes (HH:MM) format!")

def view_past_tasks():
    """Displays a list of past and scheduled tasks."""
    if tasks:
        st.subheader("Scheduled and Completed Tasks")
        for task in tasks:
            st.write(
                f"**Task Name**: {task['task_name']}, **Time**: {task['task_time']}, "
                f"**Notification**: {task['notify_type']}, **Status**: {task['status']}"
            )
    else:
        st.info("No tasks have been added yet.")

def main():
    """Main function to run the reminder app using Streamlit."""
    st.title("tik-tik Reminder App")

    # Task creation section
    st.header("Add a New Task")
    task_name = st.text_input("Task Name")
    task_time_input = st.text_input("Time (MM or HH:MM)")
    notify_type = st.selectbox("Notification Type", ["Notification", "Alarm"])

    if st.button("Add Task"):
        add_task(task_name, task_time_input, notify_type)

    # Task viewing section
    st.header("View Scheduled and Completed Tasks")
    if st.button("Refresh Task List"):
        view_past_tasks()
    else:
        view_past_tasks()

if __name__ == "__main__":
    main()
