import ctypes
import datetime
import sys
from datetime import timedelta
import sqlite3
import time
import threading


def display_complete_habit__alert():
    thread = threading.Thread(target=alert_habit_completed)
    thread.daemon = True
    thread.start()


def display_over_due_habit_alert():
    thread = threading.Thread(target=alert_overdue_habits_reset)
    thread.daemon = True
    thread.start()


def alert_habit_completed():
    ctypes.windll.user32.MessageBoxW(0, "Your Habit Has Been Completed\n", "ALERT", 0)


def alert_overdue_habits_reset():
    ctypes.windll.user32.MessageBoxW(0, "Your Over Due Habits Has Been Reset\n", "ALERT", 0)


def complete_max_days_and_reset_overdue_habits(username):
    try:
        #time.sleep(5)
        sqliteconn = None

        repeat = True

        while repeat:

            display_overdue_habit_count = 0

            current_date = datetime.date.today()
            # print(current_date)

            newduedatedaily = current_date + timedelta(days=1)
            # print(newduedatedaily)

            newduedateweekly = current_date + timedelta(days=7)
            # print(newduedateweekly)

            # print("Complete Max Days Habits ", username)

            sqliteconn = sqlite3.connect('../habit_tracker_db.sqlite3')

            # print("Connected to Database Successfully.")
            dbconn = sqliteconn.cursor()

            # When Max_Streak = Max_Days & Max_Streak != 0 & HabitStatus = 1 (Active), Set HabitStatus = 2 (Completed)
            command = """Update habits_tracker SET HabitStatus = 2 WHERE HabitStatus = 1 AND Max_Streak != 0 AND Max_Streak = Max_Days"""
            dbconn.execute(command)
            sqliteconn.commit()
            if dbconn.rowcount > 0:
                display_complete_habit__alert()

            # When Due_Date < Current_Date & HabitStatus = 1 (Active), Set Break = Break + 1
            command = """Update habits_tracker SET Break = Break + 1 WHERE HabitStatus = 1 AND Due_Date < :current_dt"""
            dbconn.execute(command, {'current_dt': current_date})
            sqliteconn.commit()
            if dbconn.rowcount > 0:
                display_overdue_habit_count = display_overdue_habit_count + 1
            # print(dbconn.rowcount, "record(s) affected")

            # When Break & HabitStatus = 1 (Active), Set Streak & Max_Streak = 0 (Reset)
            command = """Update habits_tracker SET Streak = 0, Max_Streak = 0 WHERE HabitStatus = 1 AND Due_Date < :current_dt"""
            dbconn.execute(command, {'current_dt': current_date})
            sqliteconn.commit()
            if dbconn.rowcount > 0:
                display_overdue_habit_count = display_overdue_habit_count + 1
            # print(dbconn.rowcount, "record(s) affected")

            # When Break & HabitStatus = 1 (Active), Set New Start Date (Start_Date = Current_Date)
            command = """Update habits_tracker SET Start_Date = :current_dt WHERE HabitStatus = 1 AND Due_Date < :current_dt"""
            dbconn.execute(command, {'current_dt': current_date})
            sqliteconn.commit()
            if dbconn.rowcount > 0:
                display_overdue_habit_count = display_overdue_habit_count + 1
            # print(dbconn.rowcount, "record(s) affected")

            # When Break & HabitStatus = 1 (Active), Set New Due Date (Due_Date = New Due Date Daily) For Daily Period Habit
            command = """Update habits_tracker SET Due_Date = :newduedt WHERE HabitStatus = 1 AND Period = 'Daily' AND Due_Date < :current_dt"""
            dbconn.execute(command, {'newduedt': newduedatedaily, 'current_dt': current_date})
            sqliteconn.commit()
            if dbconn.rowcount > 0:
                display_overdue_habit_count = display_overdue_habit_count + 1
            # print(dbconn.rowcount, "record(s) affected")

            # When Break & HabitStatus = 1 (Active), Set New Due Date (Due_Date = New Due Date Weekly) For Weekly Period Habit
            command = """Update habits_tracker SET Due_Date = :newduedt WHERE HabitStatus = 1 AND Period = 'Weekly' AND Due_Date < :current_dt"""
            dbconn.execute(command, {'newduedt': newduedateweekly, 'current_dt': current_date})
            sqliteconn.commit()
            if dbconn.rowcount > 0:
                display_overdue_habit_count = display_overdue_habit_count + 1
            # print(dbconn.rowcount, "record(s) affected")

            if display_overdue_habit_count > 0:
                display_over_due_habit_alert()

            sqliteconn.close()
            time.sleep(2)
            repeat = False

    except sqlite3.Error as e:
        print("Failure: ", e)

    except Exception as ex:
        print("Failure: ", ex)

    finally:
        # print("Finally Block: Change Habit's Title")
        if sqliteconn:
            sqliteconn.close()
