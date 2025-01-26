import pytest
from datetime import datetime, timedelta
from unittest.mock import patch
from project import schedule_task, check_and_alert, add_task, tasks


@pytest.fixture(autouse=True)
def reset_tasks():
    tasks.clear() 

def test_schedule_task():
    task_name = "Test Task"
    time_delta = 1  # 1 second
    notify_type = "Notification"
    
    with patch("threading.Thread.start") as mock_thread:
        schedule_task(task_name, time_delta, notify_type)
    
    # Assert the task is added to the task list
    assert len(tasks) == 1
    assert tasks[0]["task_name"] == task_name
    assert tasks[0]["notify_type"] == notify_type
    assert tasks[0]["status"] == "Scheduled"
    mock_thread.assert_called_once()

def test_check_and_alert_notification():
    task_name = "Notification Task"
    task_time = datetime.now() + timedelta(seconds=1)
    notify_type = "Notification"
    
    with patch("project.Notifier.notify") as mock_notify:
        check_and_alert(task_name, task_time, notify_type)
    
    # Assert notification was triggered
    mock_notify.assert_called_once_with(f"Task: {task_name} is due!", title="Reminder")

def test_add_task():
    with patch("streamlit.error") as mock_error, patch("streamlit.success") as mock_success:
        add_task("Valid Task", "10", "Notification")
    
    # Assert the task was successfully added
    assert len(tasks) == 1
    assert tasks[0]["task_name"] == "Valid Task"
    assert tasks[0]["notify_type"] == "Notification"
    assert tasks[0]["status"] == "Scheduled"
    mock_error.assert_not_called()
    mock_success.assert_called_once_with("Task 'Valid Task' scheduled successfully!")

def test_add_task_invalid_input():
    with patch("streamlit.error") as mock_error:
        add_task("", "", "Notification")  # Missing fields
    
    # Assert an error message was shown
    mock_error.assert_called_once_with("All fields are required!")
    assert len(tasks) == 0  # No task should be added





















