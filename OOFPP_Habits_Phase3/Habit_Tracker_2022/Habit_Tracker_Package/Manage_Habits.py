import sqlite3
import datetime
import time
from datetime import datetime, timedelta


def checked_off_habit(username):
    """The purpose of this function is to check-off habit task. It takes input from user as a habit id anc complete the task."""
    sqliteconn = None

    try:
        repeat = True

        while repeat:
            try:
                from Habit_Tracker_Package import Analyze_Your_Habits
                Analyze_Your_Habits.display_active_habits(username)

                # Today's Date
                current_date = datetime.today().date()

                # Yesterday's Date
                previous_date = current_date - timedelta(days=1)

                # Tomorrow's Date
                next_date = current_date + timedelta(days=1)

                sqliteconn = sqlite3.connect('../habit_tracker_db.sqlite3')

                dbconn = sqliteconn.cursor()

                command = """SELECT HabitId,HabitName,Description,Period,Born,Start_Date,Due_Date,Streak,Max_Streak,
                                            Break,HabitStatus FROM habits_tracker WHERE username = :usr AND HabitStatus = 1"""
                dbconn.execute(command, {'usr': username})
                records = dbconn.fetchall()
                lenrecords = len(records)

                if lenrecords > 0:
                    user_habits_id_list = []

                    for row in records:
                        user_habits_id_list.append(row[0])

                    sqliteconn.commit()

                user_input = input("\nEnter Habit Id To Check Off (or Enter -1 to Exit)?: ")
                habit_id = int(user_input)

                if habit_id == -1:
                    print("\nReturn To Main Menu")
                    repeat = False

                else:
                    repeat = True

                    task_complete_count = 0

                    if habit_id in user_habits_id_list:

                        # Increment Streak to Streak + 1
                        command = """Update habits_tracker SET Streak = Streak + 1 WHERE HabitStatus = 1 AND HabitId = :hbt_id AND 
                        Start_Date <=:start_dt AND Due_Date > :due_dt """
                        dbconn.execute(command, {'hbt_id': habit_id, 'start_dt': current_date, 'due_dt': previous_date})

                        if dbconn.rowcount > 0:
                            task_complete_count = task_complete_count + 1
                        sqliteconn.commit()

                        # Update Max_Streak = Streak If The Value Of Max_Streak Is Less Than Streak (Max_Streak <Streak)
                        command = """Update habits_tracker SET Max_Streak = Streak WHERE HabitStatus = 1 AND HabitId = :hbt_id AND 
                        Max_Streak < Streak """
                        dbconn.execute(command, {'hbt_id': habit_id})
                        if dbconn.rowcount > 0:
                            task_complete_count = task_complete_count + 1
                        sqliteconn.commit()

                        # Update Start_Date To Due_Date
                        command = """Update habits_tracker SET Start_Date = Due_Date WHERE HabitStatus = 1 AND HabitId = :hbt_id AND 
                        Start_Date <:start_dt AND Due_Date > :due_dt """
                        dbconn.execute(command, {'hbt_id': habit_id, 'start_dt': next_date, 'due_dt': previous_date})
                        if dbconn.rowcount > 0:
                            task_complete_count = task_complete_count + 1
                        sqliteconn.commit()

                        # Set Due_Date To New Updated Date

                        # Habit Period = Daily
                        new_due_date = current_date + timedelta(days=2)
                        command = """Update habits_tracker SET Due_Date =:new_due_dt WHERE HabitStatus = 1 AND HabitId = :hbt_id AND 
                        Due_Date = Due_Date AND Period = 'Daily' AND Due_Date > :due_dt """
                        dbconn.execute(command,
                                       {'hbt_id': habit_id, 'new_due_dt': new_due_date, 'due_dt': previous_date})
                        if dbconn.rowcount > 0:
                            task_complete_count = task_complete_count + 1
                        sqliteconn.commit()

                        # Habit Period = Weekly
                        new_due_date = current_date + timedelta(days=14)
                        command = """Update habits_tracker SET Due_Date =:new_due_dt WHERE HabitStatus = 1 AND HabitId = :hbt_id AND 
                        Due_Date = Due_Date AND Period = 'Weekly' AND Due_Date > :due_dt """
                        dbconn.execute(command,
                                       {'hbt_id': habit_id, 'new_due_dt': new_due_date, 'due_dt': previous_date})
                        if dbconn.rowcount > 0:
                            task_complete_count = task_complete_count + 1
                        sqliteconn.commit()

                        dbconn.close()
                        if task_complete_count > 0:
                            print("\nHabit Checked-Off Successfully....")
                        time.sleep(3)

                    else:
                        print("\nHabit Doesn't Exist\n")
                        time.sleep(3)

                sqliteconn.close()

            except sqlite3.Error as e:
                print("Failure: ", e)

            except ValueError as ve:
                print("Invalid Input", ve)

            except Exception as ex:
                print("Failure: ", ex)

    except sqlite3.Error as e:
        print("Failure: ", e)

    except Exception as ex:
        print("Failure: ", ex)

    finally:
        if sqliteconn:
            sqliteconn.close()

