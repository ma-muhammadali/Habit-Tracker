import sqlite3
import datetime
import time
from datetime import datetime, timedelta


def create_new_habit(habitname, description, period, max_days, max_weeks, username):
    sqliteconn = None

    try:
        sqliteconn = sqlite3.connect('../habit_tracker_db.sqlite3')

        # print("Connected to Database Successfully.")
        dbconn = sqliteconn.cursor()

        command = """SELECT HabitName,Description,Period,Born,Start_Date,Due_Date,Streak,Max_Streak,Break,
        HabitStatus,UserName FROM habits_tracker WHERE username = :usr """
        dbconn.execute(command, {'usr': username})
        records = dbconn.fetchall()
        lenrecords = len(records)
        # print("Total Habits are: ", lenrecords, "\n")
        # print(records)

        user_habits_list = []

        for row in records:
            user_habits_list.append(str(row[0]).lower())

        # print(user_habits_list)

        sqliteconn.commit()
        # dbconn.close()

        repeat = True

        while repeat == True:
            #user_input = input("\nDo You Want To Create New Habit (Y/N)?: ")

            user_input = 'y'

            if user_input.lower() == 'n':
                print("\nReturn To Main Menu")
                repeat = False

            elif user_input.lower() == 'y':
                habit_exist = False
                repeat = False

                #HabitName = input("Enter New Habit Name: ")
                HabitName = str(habitname).strip()
                habitname = habitname.lower()

                if habitname in user_habits_list:
                    print("\nHabit Already Exists...")
                    print("\nNote: If Habit is not visible in Tracked Habits, Please check it in Completed/Deleted Habits....")
                    time.sleep(3)
                    habit_exist = True

                if not habit_exist:
                    #Description = input("Enter Habit Description: ")
                    Description = str(description).strip()
                    Born = datetime.today().date()
                    Start_Date = datetime.today().date()
                    HabitStatus = 1
                    Streak = 0
                    Max_Streak = 0
                    Break = 0
                    Period = ''
                    Due_Date = 0
                    Max_Days = 0

                    repeat_period_type = True

                    while repeat_period_type:
                        #period_type = input("Habit Period - Daily or Weekly (Enter D for Daily & W for Weekly): ")

                        period_type = str(period).lower().strip()

                        if period_type.lower() == 'd':
                            Period = 'Daily'
                            Due_Date = Start_Date + timedelta(days=1)
                            repeat_period_type = False

                            repeat_max_days = True

                            while repeat_max_days:
                                try:
                                    #habit_max_days = input("\nFor how many days do you want to continue this Habit: ")
                                    #habit_max_days = int(habit_max_days)
                                    habit_max_days = int(max_days)

                                    if habit_max_days > 0:
                                        repeat_max_days = False
                                        Max_Days = habit_max_days

                                    else:
                                        print("\nDays should not be less than 1\n")
                                        repeat_max_days = True

                                except Exception as ex:
                                    print("\nInvalid Input\n")
                                    print("Failure: ", ex)


                        elif period_type.lower() == 'w':
                            Period = 'Weekly'
                            Due_Date = Start_Date + timedelta(days=7)
                            repeat_period_type = False

                            repeat_max_weeks = True

                            while repeat_max_weeks:
                                try:
                                    #habit_max_weeks = input("\nFor how many weeks do you want to continue this Habit: ")
                                    #habit_max_weeks = int(habit_max_weeks)
                                    habit_max_weeks = int(max_weeks)

                                    if habit_max_weeks > 0:
                                        Max_Days = 7 * habit_max_weeks
                                        repeat_max_weeks = False

                                    else:
                                        print("\nWeeks should not be less than 1\n")
                                        repeat_max_weeks = True

                                except Exception as ex:
                                    print("\nInvalid Input\n")
                                    print("Failure: ", ex)

                        else:
                            print("Incorrect Habit Period Type....")
                            repeat_period_type = True

                    sqliteconn = sqlite3.connect('../habit_tracker_db.sqlite3')

                    # print("Connected to Database Successfully.")
                    dbconn = sqliteconn.cursor()

                    new_habit = [(HabitName, Description, Period, Born, Start_Date, Due_Date, Streak, Max_Streak, Max_Days, Break,
                                  HabitStatus, username)]
                    dbconn.executemany("INSERT INTO habits_tracker ('HabitName','Description','Period','Born', "
                                       "'Start_Date','Due_Date','Streak','Max_Streak', 'Max_Days', 'Break', 'HabitStatus', "
                                       "'UserName') VALUES (?,?,?,?,?,?,?,?,?,?,?,?)", new_habit)
                    sqliteconn.commit()
                    dbconn.close()
                    print("Habit Created Successfully....")
                    print("Please wait.....")
                    time.sleep(3)

                    from Analyze_Your_Habits_Test import display_all_tracked_habits
                    display_all_tracked_habits(username)

            else:
                print("\nIncorrect Choice...")
                repeat = True

    except sqlite3.Error as e:
        print("Failure: ", e)

    except Exception as ex:
        print("Failure: ", ex)

    finally:
        if sqliteconn:
            sqliteconn.close()
