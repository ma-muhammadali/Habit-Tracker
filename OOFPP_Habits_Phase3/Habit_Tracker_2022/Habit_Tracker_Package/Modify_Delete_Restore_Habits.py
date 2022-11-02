import sqlite3
import datetime
from datetime import datetime, timedelta
import time


def modify_delete_habits(username):
    """The purpose of this function is to display Modify, Delete & Restore menu.."""
    choice = ''

    while choice.lower() != 'x':

        print("\n*********************************************")
        print("\tModify, Delete & Restore Habit Menu")
        print("*********************************************\n")

        print("[1] Enter 1 to CHANGE HABIT'S TITLE")
        print("[2] Enter 2 to CHANGE HABIT'S DESCRIPTION")
        print("[3] Enter 3 to CHANGE HABIT'S PERIOD TO DAILY")
        print("[4] Enter 4 to CHANGE HABIT'S PERIOD TO WEEKLY")
        print("[5] Enter 5 to CHANGE HABIT'S MAX DAYS")
        print("[6] Enter 6 to DELETE HABIT")
        print("[7] Enter 7 to RESTORE DELETED HABIT")
        print("[8] Enter 8 to RESTORE COMPLETED HABIT")
        print("[X] Enter X to EXIT")

        choice = input("Enter Your Choice: ")

        if choice.lower() == 'x':
            print("Return To Main Menu")

        elif choice == '1':
            change_habit_title(username)

        elif choice == '2':
            change_habit_description(username)

        elif choice == '3':
            change_habit_period_to_daily(username)

        elif choice == '4':
            change_habit_period_to_weekly(username)

        elif choice == '5':
            change_habit_max_days(username)

        elif choice == '6':
            delete_habit(username)

        elif choice == '7':
            restore_deleted_habit(username)

        elif choice == '8':
            restore_completed_habit(username)

        else:
            print("Invalid Choice")


def change_habit_title(username):
    """The purpose of this function is to change the habit name. It takes the habit id from user and change its title."""
    sqliteconn = None

    try:
        repeat = True
        while repeat:
            try:

                sqliteconn = sqlite3.connect('../habit_tracker_db.sqlite3')

                # print("Connected to Database Successfully.")
                dbconn = sqliteconn.cursor()

                command = """SELECT HabitId,HabitName,Description,Period,Born,Start_Date,Due_Date,Streak,Max_Streak,
                        Break,HabitStatus,UserName FROM habits_tracker WHERE username = :usr AND HabitStatus = 1"""
                dbconn.execute(command, {'usr': username})
                records = dbconn.fetchall()
                lenrecords = len(records)
                sqliteconn.commit()
                # print("Total Habits are: ", lenrecords, "\n")
                # print(records)

                if lenrecords > 0:
                    from Habit_Tracker_Package import Analyze_Your_Habits
                    Analyze_Your_Habits.display_active_habits(username)
                    user_habits_id_list = []

                    for row in records:
                        user_habits_id_list.append(row[0])

                    user_input = input("\nEnter Habit Id To Change Its Title (or Enter -1 to Exit)?: ")
                    habit_id = int(user_input)

                    if habit_id == -1:
                        print("\nReturn To Main Menu")
                        repeat = False

                    else:
                        repeat = True

                        if habit_id in user_habits_id_list:

                            new_habit_title = ''
                            repeat_habit_name = True

                            while repeat_habit_name:
                                new_habit_title = input("Please Enter New Habit Name: ")
                                new_habit_title = str(new_habit_title).strip()

                                if new_habit_title == '':
                                    print("Habit name can not be empty")
                                    repeat_habit_name = True

                                else:
                                    repeat_habit_name = False

                            command = """Update habits_tracker SET HabitName =:hbt_title WHERE HabitId = :hbt_id"""
                            dbconn.execute(command, {'hbt_id': habit_id, 'hbt_title': new_habit_title.title()})
                            sqliteconn.commit()
                            sqliteconn.close()

                        else:
                            print("\n#####################")
                            print("Habit Doesn't Exist")
                            print("#####################\n")
                            time.sleep(3)

                else:
                    print("\n#########################################")
                    print("There is No Tracked Habit(s) Available....")
                    print("#########################################\n")
                    repeat = False
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
        #print("Finally Block: Change Habit's Title")
        if sqliteconn:
            sqliteconn.close()


def change_habit_description(username):
    """The purpose of this function is to change the habit description. It takes the habit id from user and change its description."""
    sqliteconn = None

    try:
        repeat = True
        while repeat:
            try:

                sqliteconn = sqlite3.connect('../habit_tracker_db.sqlite3')

                # print("Connected to Database Successfully.")
                dbconn = sqliteconn.cursor()

                command = """SELECT HabitId,HabitName,Description,Period,Born,Start_Date,Due_Date,Streak,Max_Streak,
                        Break,HabitStatus,UserName FROM habits_tracker WHERE username = :usr AND HabitStatus = 1"""
                dbconn.execute(command, {'usr': username})
                records = dbconn.fetchall()
                lenrecords = len(records)
                sqliteconn.commit()
                # print("Total Habits are: ", lenrecords, "\n")
                # print(records)

                if lenrecords > 0:
                    from Habit_Tracker_Package import Analyze_Your_Habits
                    Analyze_Your_Habits.display_active_habits(username)
                    user_habits_id_list = []

                    for row in records:
                        user_habits_id_list.append(row[0])

                    user_input = input("\nEnter Habit Id To Change Its DESCRIPTION (or Enter -1 to Exit)?: ")
                    habit_id = int(user_input)

                    if habit_id == -1:
                        print("\nReturn To Main Menu")
                        repeat = False

                    else:
                        repeat = True

                        if habit_id in user_habits_id_list:

                            new_habit_description = ''
                            repeat_habit_desc = True

                            while repeat_habit_desc:
                                new_habit_description = input("Please Enter New Description: ")
                                new_habit_description = str(new_habit_description).strip()

                                if new_habit_description == '':
                                    print("Habit description can not be empty")
                                    repeat_habit_desc = True

                                else:
                                    repeat_habit_desc = False

                            command = """Update habits_tracker SET Description =:hbt_desc WHERE HabitId = :hbt_id"""
                            dbconn.execute(command, {'hbt_id': habit_id, 'hbt_desc': new_habit_description.title()})

                            sqliteconn.commit()
                            sqliteconn.close()

                        else:
                            print("\n#####################")
                            print("Habit Doesn't Exist")
                            print("#####################\n")
                            time.sleep(3)

                else:
                    print("\n#########################################")
                    print("There is No Tracked Habit(s) Available....")
                    print("#########################################\n")
                    repeat = False
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


def change_habit_period_to_daily(username):
    """The purpose of this function is to change the habit period. It takes the habit id from user and change its period to daily."""
    sqliteconn = None

    try:
        repeat = True
        while repeat:
            try:

                sqliteconn = sqlite3.connect('../habit_tracker_db.sqlite3')

                # print("Connected to Database Successfully.")
                dbconn = sqliteconn.cursor()

                command = """SELECT HabitId,HabitName,Description,Period,Born,Start_Date,Due_Date,Streak,Max_Streak,
                        Break,HabitStatus,UserName FROM habits_tracker WHERE username = :usr AND HabitStatus = 1"""
                dbconn.execute(command, {'usr': username})
                records = dbconn.fetchall()
                lenrecords = len(records)
                sqliteconn.commit()
                # print("Total Habits are: ", lenrecords, "\n")
                # print(records)

                if lenrecords > 0:
                    from Habit_Tracker_Package import Analyze_Your_Habits
                    Analyze_Your_Habits.display_active_habits(username)
                    user_habits_id_list = []

                    for row in records:
                        user_habits_id_list.append(row[0])

                    user_input = input("\nEnter Habit Id To Change Its Period To Daily (or Enter -1 to Exit)?: ")
                    habit_id = int(user_input)

                    if habit_id == -1:
                        print("\nReturn To Main Menu")
                        repeat = False

                    else:
                        repeat = True

                        if habit_id in user_habits_id_list:

                            command = """Update habits_tracker SET Period = 'Daily', Due_Date = DATE(Start_Date, 
                            '+1 day') WHERE HabitId = :hbt_id AND Period = 'Weekly' """
                            dbconn.execute(command, {'hbt_id': habit_id})

                            sqliteconn.commit()
                            sqliteconn.close()

                        else:
                            print("\n#####################")
                            print("Habit Doesn't Exist")
                            print("#####################\n")
                            time.sleep(3)

                else:
                    print("\n#########################################")
                    print("There is No Tracked Habit(s) Available....")
                    print("#########################################\n")
                    repeat = False
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


def change_habit_period_to_weekly(username):
    """The purpose of this function is to change the habit period. It takes the habit id from user and change its period to weekly."""
    sqliteconn = None

    try:
        repeat = True
        while repeat:
            try:

                sqliteconn = sqlite3.connect('../habit_tracker_db.sqlite3')

                # print("Connected to Database Successfully.")
                dbconn = sqliteconn.cursor()

                command = """SELECT HabitId,HabitName,Description,Period,Born,Start_Date,Due_Date,Streak,Max_Streak,
                        Break,HabitStatus,UserName FROM habits_tracker WHERE username = :usr AND HabitStatus = 1"""
                dbconn.execute(command, {'usr': username})
                records = dbconn.fetchall()
                lenrecords = len(records)
                sqliteconn.commit()
                # print("Total Habits are: ", lenrecords, "\n")
                # print(records)

                if lenrecords > 0:
                    from Habit_Tracker_Package import Analyze_Your_Habits
                    Analyze_Your_Habits.display_active_habits(username)
                    user_habits_id_list = []

                    for row in records:
                        user_habits_id_list.append(row[0])

                    user_input = input("\nEnter Habit Id To Change Its Period To Weekly (or Enter -1 to Exit)?: ")
                    habit_id = int(user_input)

                    if habit_id == -1:
                        print("\nReturn To Main Menu")
                        repeat = False

                    else:
                        repeat = True

                        if habit_id in user_habits_id_list:

                            command = """Update habits_tracker SET Period = 'Weekly', Due_Date = DATE(Start_Date, 
                            '+7 day') WHERE HabitId = :hbt_id AND Period = 'Daily' """
                            dbconn.execute(command, {'hbt_id': habit_id})

                            sqliteconn.commit()
                            sqliteconn.close()

                        else:
                            print("\n#####################")
                            print("Habit Doesn't Exist")
                            print("#####################\n")
                            time.sleep(3)

                else:
                    print("\n#########################################")
                    print("There is No Tracked Habit(s) Available....")
                    print("#########################################\n")
                    repeat = False
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


def change_habit_max_days(username):
    """The purpose of this function is to change the habit max days. It takes the habit id from user and change its max days."""
    sqliteconn = None

    try:
        repeat = True
        while repeat:
            try:

                sqliteconn = sqlite3.connect('../habit_tracker_db.sqlite3')

                # print("Connected to Database Successfully.")
                dbconn = sqliteconn.cursor()

                command = """SELECT HabitId,HabitName,Description,Period,Born,Start_Date,Due_Date,Streak,Max_Streak,
                        Break,HabitStatus,UserName FROM habits_tracker WHERE username = :usr AND HabitStatus = 1"""
                dbconn.execute(command, {'usr': username})
                records = dbconn.fetchall()
                lenrecords = len(records)
                sqliteconn.commit()
                # print("Total Habits are: ", lenrecords, "\n")
                # print(records)

                if lenrecords > 0:
                    from Habit_Tracker_Package import Analyze_Your_Habits
                    Analyze_Your_Habits.display_active_habits(username)
                    user_habits_id_list = []

                    for row in records:
                        user_habits_id_list.append(row[0])

                    user_input = input("\nEnter Habit Id To Change Its Max Days (or Enter -1 to Exit)?: ")
                    habit_id = int(user_input)

                    if habit_id == -1:
                        print("\nReturn To Main Menu")
                        repeat = False

                    else:
                        repeat = True

                        if habit_id in user_habits_id_list:

                            new_habit_max_days = ''
                            repeat_habit_max_days = True

                            while repeat_habit_max_days:
                                new_habit_max_days = input("Please Enter New Habit Max Days: ")
                                new_habit_max_days = str(new_habit_max_days).strip()
                                new_habit_max_days = int(new_habit_max_days)

                                if new_habit_max_days <= 0:
                                    print("Habit Max Days must be 1 or more....")
                                    repeat_habit_max_days = True

                                else:
                                    repeat_habit_max_days = False

                            command = """Update habits_tracker SET Max_Days =:maxdays WHERE HabitId = :hbt_id"""
                            dbconn.execute(command, {'hbt_id': habit_id, 'maxdays': new_habit_max_days})
                            sqliteconn.commit()
                            sqliteconn.close()

                        else:
                            print("\n#####################")
                            print("Habit Doesn't Exist")
                            print("#####################\n")
                            time.sleep(3)

                else:
                    print("\n#########################################")
                    print("There is No Tracked Habit(s) Available....")
                    print("#########################################\n")
                    repeat = False
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
        print("Finally Block: Change Habit's Title")
        if sqliteconn:
            sqliteconn.close()


def delete_habit(username):
    """The purpose of this function is to delete the habit. It takes the habit id from user and delete it (soft delete, change status to 0) from table."""
    sqliteconn = None

    try:
        repeat = True
        while repeat:
            try:

                sqliteconn = sqlite3.connect('../habit_tracker_db.sqlite3')

                # print("Connected to Database Successfully.")
                dbconn = sqliteconn.cursor()

                command = """SELECT HabitId,HabitName,Description,Period,Born,Start_Date,Due_Date,Streak,Max_Streak,
                        Break,HabitStatus,UserName FROM habits_tracker WHERE username = :usr AND HabitStatus = 1"""
                dbconn.execute(command, {'usr': username})
                records = dbconn.fetchall()
                lenrecords = len(records)
                sqliteconn.commit()
                # print("Total Habits are: ", lenrecords, "\n")
                # print(records)

                if lenrecords > 0:
                    from Habit_Tracker_Package import Analyze_Your_Habits
                    Analyze_Your_Habits.display_active_habits(username)
                    user_habits_id_list = []

                    for row in records:
                        user_habits_id_list.append(row[0])

                    user_input = input("\nEnter Habit Id To Delete (or Enter -1 to Exit)?: ")
                    habit_id = int(user_input)

                    if habit_id == -1:
                        print("\nReturn To Main Menu")
                        repeat = False

                    else:
                        repeat = True

                        if habit_id in user_habits_id_list:

                            command = """Update habits_tracker SET HabitStatus = 0 WHERE HabitId = :hbt_id"""
                            dbconn.execute(command, {'hbt_id': habit_id})

                            sqliteconn.commit()
                            sqliteconn.close()

                            from Habit_Tracker_Package import Analyze_Your_Habits
                            Analyze_Your_Habits.display_deleted_habits(username)

                        else:
                            print("\n#####################")
                            print("Habit Doesn't Exist")
                            print("#####################\n")
                            time.sleep(3)

                else:
                    print("\n#########################################")
                    print("There is No Tracked Habit(s) Available....")
                    print("#########################################\n")
                    repeat = False
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


def restore_deleted_habit(username):
    """The purpose of this function is to restore deleted habit. It takes the habit id from user and restore it from deleted habits."""
    sqliteconn = None

    try:
        repeat = True
        while repeat:

            try:
                sqliteconn = sqlite3.connect('../habit_tracker_db.sqlite3')

                # print("Connected to Database Successfully.")
                dbconn = sqliteconn.cursor()

                command = """SELECT HabitId,HabitName,Description,Period,Born,Start_Date,Due_Date,Streak,Max_Streak,
                        Break,HabitStatus,UserName FROM habits_tracker WHERE username = :usr AND HabitStatus = 0"""
                dbconn.execute(command, {'usr': username})
                records = dbconn.fetchall()
                lenrecords = len(records)
                sqliteconn.commit()
                # print("Total Habits are: ", lenrecords, "\n")
                # print(records)

                if lenrecords > 0:
                    from Habit_Tracker_Package import Analyze_Your_Habits
                    Analyze_Your_Habits.display_deleted_habits(username)

                    user_habits_id_list = []

                    for row in records:
                        user_habits_id_list.append(row[0])

                    user_input = input("\nEnter Habit Id To Restore It (or Enter -1 to Exit)?: ")
                    habit_id = int(user_input)

                    if habit_id == -1:
                        print("\nReturn To Main Menu")
                        repeat = False

                    else:
                        repeat = True

                        if habit_id in user_habits_id_list:

                            Born = datetime.today().date()
                            Start_Date = datetime.today().date()
                            Due_Date_Daily = Start_Date + timedelta(days=1)
                            Due_Date_Weekly = Start_Date + timedelta(days=7)

                            command = """Update habits_tracker SET HabitStatus = 1, Streak = 0, Max_Streak = 0, Max_Days = 0 ,Break = 
                            0, Due_Date = :due_dt , Born = :brn, Start_Date = :strt_dt  WHERE HabitId = :hbt_id AND 
                            Period = 'Daily' """
                            dbconn.execute(command, {'hbt_id': habit_id, 'brn': Born, 'strt_dt': Start_Date,
                                                     'due_dt': Due_Date_Daily})
                            sqliteconn.commit()

                            command = """Update habits_tracker SET HabitStatus = 1, Streak = 0, Max_Streak = 0, Max_Days = 0 ,Break = 
                            0, Due_Date = :due_dt , Born = :brn, Start_Date = :strt_dt  WHERE HabitId = :hbt_id AND 
                            Period = 'Weekly' """
                            dbconn.execute(command, {'hbt_id': habit_id, 'brn': Born, 'strt_dt': Start_Date,
                                                     'due_dt': Due_Date_Weekly})

                            sqliteconn.commit()

                            sqliteconn.close()

                            from Habit_Tracker_Package import Analyze_Your_Habits
                            Analyze_Your_Habits.display_active_habits(username)

                        else:
                            print("\n#####################")
                            print("Habit Doesn't Exist")
                            print("#####################\n")
                            time.sleep(3)

                else:
                    print("\n#########################################")
                    print("There is No Deleted Habit(s) Available....")
                    print("#########################################\n")
                    repeat = False
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


def restore_completed_habit(username):
    """The purpose of this function is to restore completed habit. It takes the habit id from user and restore it from completed habits."""
    sqliteconn = None

    try:
        repeat = True
        while repeat:

            try:
                sqliteconn = sqlite3.connect('../habit_tracker_db.sqlite3')

                # print("Connected to Database Successfully.")
                dbconn = sqliteconn.cursor()

                command = """SELECT HabitId,HabitName,Description,Period,Born,Start_Date,Due_Date,Streak,Max_Streak,
                        Break,HabitStatus,UserName FROM habits_tracker WHERE username = :usr AND HabitStatus = 2"""
                dbconn.execute(command, {'usr': username})
                records = dbconn.fetchall()
                lenrecords = len(records)
                sqliteconn.commit()
                # print("Total Habits are: ", lenrecords, "\n")
                # print(records)

                if lenrecords > 0:
                    from Habit_Tracker_Package import Analyze_Your_Habits
                    Analyze_Your_Habits.display_completed_habits(username)

                    user_habits_id_list = []

                    for row in records:
                        user_habits_id_list.append(row[0])

                    user_input = input("\nEnter Habit Id To Restore It (or Enter -1 to Exit)?: ")
                    habit_id = int(user_input)

                    if habit_id == -1:
                        print("\nReturn To Main Menu")
                        repeat = False

                    else:
                        repeat = True

                        if habit_id in user_habits_id_list:

                            Born = datetime.today().date()
                            Start_Date = datetime.today().date()
                            Due_Date_Daily = Start_Date + timedelta(days=1)
                            Due_Date_Weekly = Start_Date + timedelta(days=7)
                            update_executed = 0

                            command = """Update habits_tracker SET HabitStatus = 1, Streak = 0, Max_Streak = 0, Max_Days = 0 ,Break = 
                            0, Due_Date = :due_dt , Born = :brn, Start_Date = :strt_dt  WHERE HabitId = :hbt_id AND 
                            Period = 'Daily' """
                            dbconn.execute(command, {'hbt_id': habit_id, 'brn': Born, 'strt_dt': Start_Date,
                                                     'due_dt': Due_Date_Daily})
                            update_executed = update_executed + 1

                            sqliteconn.commit()

                            command = """Update habits_tracker SET HabitStatus = 1, Streak = 0, Max_Streak = 0, Max_Days = 0 ,Break = 
                            0, Due_Date = :due_dt , Born = :brn, Start_Date = :strt_dt  WHERE HabitId = :hbt_id AND 
                            Period = 'Weekly' """
                            dbconn.execute(command, {'hbt_id': habit_id, 'brn': Born, 'strt_dt': Start_Date,
                                                     'due_dt': Due_Date_Weekly})
                            update_executed = update_executed + 1

                            sqliteconn.commit()
                            sqliteconn.close()

                            if update_executed > 0:
                                print("\nHabit Has Been Restored From Completed Habits...\n")
                                time.sleep(3)

                            from Habit_Tracker_Package import Analyze_Your_Habits
                            Analyze_Your_Habits.display_active_habits(username)

                        else:
                            print("\n#####################")
                            print("Habit Doesn't Exist")
                            print("#####################\n")
                            time.sleep(3)

                else:
                    print("\n#########################################")
                    print("There is No Completed Habit(s) Available....")
                    print("#########################################\n")
                    repeat = False
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
