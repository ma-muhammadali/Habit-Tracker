from Convert_Table_Columns_String_Test import Cast_Table_Columns_String
from Min_Max_Display_Conversion_Test import Min_Max_Conversion
from Display_Habits_With_All_Columns_Test import Display_All_Habits_Columns
from Clear_Screen_and_Progress_Bar_Test import clear_screen
from rich.console import Console
from rich.table import Table
import time
import sqlite3


def analyze_your_habits(username):
    choice = ''

    while choice.lower() != 'x':
        print("\n[1] Enter 1 to VIEW ALL TRACKED HABITS")
        print("[2] Enter 2 to VIEW ALL DELETED HABITS")
        print("[3] Enter 3 to VIEW ALL COMPLETED HABITS")
        print("[4] Enter 4 to VIEW ALL DAILY HABITS")
        print("[5] Enter 5 to VIEW ALL WEEKLY HABITS")
        print("[6] Enter 6 to VIEW SMALLEST RUN STREAK DAILY HABIT")
        print("[7] Enter 7 to VIEW SMALLEST RUN STREAK WEEKLY HABIT")
        print("[8] Enter 8 to VIEW SMALLEST RUN STREAK AMONG ALL HABITS")
        print("[9] Enter 9 to VIEW LONGEST RUN STREAK DAILY HABIT")
        print("[10] Enter 10 to VIEW LONGEST RUN STREAK WEEKLY HABIT")
        print("[11] Enter 11 to VIEW LONGEST RUN STREAK AMONG ALL HABITS")
        print("[12] Enter 12 to VIEW LONGEST RUN STREAK GIVEN HABIT")

        print("[X] Enter X to EXIT")

        choice = input("Enter Your Choice: ")

        if choice.lower() == 'x':
            print("Return To Main Menu")

        elif choice == '1':
            display_all_tracked_habits(username)

        elif choice == '2':
            display_all_deleted_habits(username)

        elif choice == '3':
            display_all_completed_habits(username)

        elif choice == '4':
            display_all_daily_habits(username)

        elif choice == '5':
            display_all_weekly_habits(username)

        elif choice == '6':
            display_smallest_streak_daily_habits(username)

        elif choice == '7':
            display_smallest_streak_weekly_habits(username)

        elif choice == '8':
            display_smallest_streak_among_all_habits(username)

        elif choice == '9':
            display_longest_streak_daily_habits(username)

        elif choice == '10':
            display_longest_streak_weekly_habits(username)

        elif choice == '11':
            display_longest_streak_among_all_habits(username)

        elif choice == '12':
            display_longest_streak_given_habit(username)

        else:
            print("Invalid Choice")


def display_all_tracked_habits(username):
    sqliteconn = None

    try:
        # Clear Terminal Screen Before Printing
        clear_screen()

        sqliteconn = sqlite3.connect('../habit_tracker_db.sqlite3')

        # print("Connected to Database Successfully.")
        dbconn = sqliteconn.cursor()

        command = """SELECT HabitName, Description, Period, Born, Start_Date, Due_Date, Streak, Max_Streak, Max_Days, Break, 
        HabitStatus FROM habits_tracker WHERE username = :usr  AND HabitStatus = 1"""
        dbconn.execute(command, {'usr': username})
        records = dbconn.fetchall()
        lenrecords = len(records)

        if lenrecords > 0:
            table_records = []
            choice = '1'

            for row in records:
                table_records.append(Cast_Table_Columns_String(*row))

            print_habit_tracker_table(table_records, choice)

        else:
            print("\nCurrently, There Is No Tracked Habit(s) Available.....")

        sqliteconn.commit()
        sqliteconn.close()

    except sqlite3.Error as e:
        print("Failure: ", e)

    except Exception as ex:
        print("Failure: ", ex)

    finally:
        if sqliteconn:
            sqliteconn.close()


def display_all_deleted_habits(username):
    sqliteconn = None

    try:
        # Clear Terminal Screen Before Printing
        clear_screen()

        sqliteconn = sqlite3.connect('../habit_tracker_db.sqlite3')

        # print("Connected to Database Successfully.")
        dbconn = sqliteconn.cursor()

        command = """SELECT HabitName, Description, Period, Born, Start_Date, Due_Date, Streak, Max_Streak, Max_Days, Break, 
        HabitStatus FROM habits_tracker WHERE username = :usr  AND HabitStatus = 0"""
        dbconn.execute(command, {'usr': username})
        records = dbconn.fetchall()
        lenrecords = len(records)
        # print("Total Habits are: ", lenrecords, "\n")
        # print(records)

        if lenrecords > 0:
            table_records = []
            choice = '2'

            for row in records:
                table_records.append(Cast_Table_Columns_String(*row))

            print_habit_tracker_table(table_records, choice)

        else:
            print("\nCurrently, There Is No Deleted Habit(s) Available.....")

        sqliteconn.commit()
        sqliteconn.close()

    except sqlite3.Error as e:
        print("Failure: ", e)

    except Exception as ex:
        print("Failure: ", ex)

    finally:
        if sqliteconn:
            sqliteconn.close()


def display_all_completed_habits(username):
    sqliteconn = None

    try:
        # Clear Terminal Screen Before Printing
        clear_screen()

        sqliteconn = sqlite3.connect('../habit_tracker_db.sqlite3')

        # print("Connected to Database Successfully.")
        dbconn = sqliteconn.cursor()

        command = """SELECT HabitName, Description, Period, Born, Start_Date, Due_Date, Streak, Max_Streak, Max_Days, Break, 
        HabitStatus FROM habits_tracker WHERE username = :usr  AND HabitStatus = 2"""
        dbconn.execute(command, {'usr': username})
        records = dbconn.fetchall()
        lenrecords = len(records)

        if lenrecords > 0:
            table_records = []
            choice = '3'

            for row in records:
                table_records.append(Cast_Table_Columns_String(*row))

            print_habit_tracker_table(table_records, choice)

        else:
            print("\nCurrently, There Is No Completed Habit(s) Available.....")

        sqliteconn.commit()
        sqliteconn.close()

    except sqlite3.Error as e:
        print("Failure: ", e)

    except Exception as ex:
        print("Failure: ", ex)

    finally:
        if sqliteconn:
            sqliteconn.close()


def display_all_daily_habits(username):
    sqliteconn = None

    try:
        # Clear Terminal Screen Before Printing
        clear_screen()

        sqliteconn = sqlite3.connect('../habit_tracker_db.sqlite3')

        # print("Connected to Database Successfully.")
        dbconn = sqliteconn.cursor()

        command = """SELECT HabitName, Description, Period, Born, Start_Date, Due_Date, Streak, Max_Streak, Max_Days, Break, 
        HabitStatus FROM habits_tracker WHERE username = :usr  AND Period = 'Daily'  AND HabitStatus = 1"""
        dbconn.execute(command, {'usr': username})
        records = dbconn.fetchall()
        lenrecords = len(records)
        # print("Total Habits are: ", lenrecords, "\n")
        # print(records)

        if lenrecords > 0:
            table_records = []
            choice = '4'

            for row in records:
                table_records.append(Cast_Table_Columns_String(*row))

            print_habit_tracker_table(table_records, choice)

        else:
            print("\nCurrently, There Is No Daily Habit(s) Available.....")

        sqliteconn.commit()
        sqliteconn.close()

    except sqlite3.Error as e:
        print("Failure: ", e)

    except Exception as ex:
        print("Failure: ", ex)

    finally:
        if sqliteconn:
            sqliteconn.close()


def display_all_weekly_habits(username):
    sqliteconn = None

    try:
        # Clear Terminal Screen Before Printing
        clear_screen()

        sqliteconn = sqlite3.connect('../habit_tracker_db.sqlite3')

        # print("Connected to Database Successfully.")
        dbconn = sqliteconn.cursor()

        command = """SELECT HabitName, Description, Period, Born, Start_Date, Due_Date, Streak, Max_Streak, Max_Days, Break, 
        HabitStatus FROM habits_tracker WHERE username = :usr  AND Period = 'Weekly' AND HabitStatus = 1"""
        dbconn.execute(command, {'usr': username})
        records = dbconn.fetchall()
        lenrecords = len(records)
        # print("Total Habits are: ", lenrecords, "\n")
        # print(records)

        if lenrecords > 0:
            table_records = []
            choice = '5'

            for row in records:
                table_records.append(Cast_Table_Columns_String(*row))

            print_habit_tracker_table(table_records, choice)

        else:
            print("\nCurrently, There Is No Weekly Habit(s) Available.....")

        sqliteconn.commit()
        sqliteconn.close()

    except sqlite3.Error as e:
        print("Failure: ", e)

    except Exception as ex:
        print("Failure: ", ex)

    finally:
        if sqliteconn:
            sqliteconn.close()


def display_smallest_streak_daily_habits(username):
    sqliteconn = None

    try:
        # Clear Terminal Screen Before Printing
        clear_screen()

        sqliteconn = sqlite3.connect('../habit_tracker_db.sqlite3')

        # print("Connected to Database Successfully.")
        dbconn = sqliteconn.cursor()

        command = """SELECT HabitName, HabitStatus, MIN(Max_Streak) FROM habits_tracker WHERE username = :usr  AND Period = 'Daily' AND 
        HabitStatus = 1 """
        dbconn.execute(command, {'usr': username})
        records = dbconn.fetchall()
        lenrecords = len(records)
        # print("Total Habits are: ", lenrecords, "\n")
        # print(records)

        if lenrecords > 0:
            table_records = []
            choice = '6'

            for row in records:
                table_records.append(Min_Max_Conversion(*row))

            print_habit_tracker_table_min_max_values(table_records, choice)

        else:
            print("\nCurrently, There Is No Daily Habit(s) Available.....")

        sqliteconn.commit()
        sqliteconn.close()

    except sqlite3.Error as e:
        print("Failure: ", e)

    except Exception as ex:
        print("Failure: ", ex)

    finally:
        if sqliteconn:
            sqliteconn.close()


def display_smallest_streak_weekly_habits(username):
    sqliteconn = None

    try:
        # Clear Terminal Screen Before Printing
        clear_screen()

        sqliteconn = sqlite3.connect('../habit_tracker_db.sqlite3')

        # print("Connected to Database Successfully.")
        dbconn = sqliteconn.cursor()

        command = """SELECT HabitName, HabitStatus, MIN(Max_Streak) FROM habits_tracker WHERE username = :usr  AND Period = 'Weekly' AND 
                HabitStatus = 1 """
        dbconn.execute(command, {'usr': username})
        records = dbconn.fetchall()
        lenrecords = len(records)
        # print("Total Habits are: ", lenrecords, "\n")
        # print(records)

        if lenrecords > 0:
            table_records = []
            choice = '7'

            for row in records:
                table_records.append(Min_Max_Conversion(*row))

            print_habit_tracker_table_min_max_values(table_records, choice)

        else:
            print("\nCurrently, There Is No Weekly Habit(s) Available.....")

        sqliteconn.commit()
        sqliteconn.close()

    except sqlite3.Error as e:
        print("Failure: ", e)

    except Exception as ex:
        print("Failure: ", ex)

    finally:
        if sqliteconn:
            sqliteconn.close()


def display_smallest_streak_among_all_habits(username):
    sqliteconn = None

    try:
        # Clear Terminal Screen Before Printing
        clear_screen()

        sqliteconn = sqlite3.connect('../habit_tracker_db.sqlite3')

        # print("Connected to Database Successfully.")
        dbconn = sqliteconn.cursor()

        command = """SELECT HabitName, HabitStatus, MIN(Max_Streak) FROM habits_tracker WHERE username = :usr  AND HabitStatus = 1 """
        dbconn.execute(command, {'usr': username})
        records = dbconn.fetchall()
        lenrecords = len(records)

        if lenrecords > 0:
            table_records = []
            choice = '8'

            for row in records:
                table_records.append(Min_Max_Conversion(*row))

            print_habit_tracker_table_min_max_values(table_records, choice)

        else:
            print("\nCurrently, There Is No Daily/Weekly Habit(s) Available.....")

        sqliteconn.commit()
        sqliteconn.close()

    except sqlite3.Error as e:
        print("Failure: ", e)

    except Exception as ex:
        print("Failure: ", ex)

    finally:
        if sqliteconn:
            sqliteconn.close()


def display_longest_streak_daily_habits(username):
    sqliteconn = None

    try:
        # Clear Terminal Screen Before Printing
        clear_screen()

        sqliteconn = sqlite3.connect('../habit_tracker_db.sqlite3')

        # print("Connected to Database Successfully.")
        dbconn = sqliteconn.cursor()

        command = """SELECT HabitName, HabitStatus, MAX(Max_Streak) FROM habits_tracker WHERE username = :usr  AND Period = 'Daily' AND 
                HabitStatus = 1 """
        dbconn.execute(command, {'usr': username})
        records = dbconn.fetchall()
        lenrecords = len(records)

        if lenrecords > 0:
            table_records = []
            choice = '9'

            for row in records:
                table_records.append(Min_Max_Conversion(*row))

            print_habit_tracker_table_min_max_values(table_records, choice)

        else:
            print("\nCurrently, There Is No Daily Habit(s) Available.....")

        sqliteconn.commit()
        sqliteconn.close()

    except sqlite3.Error as e:
        print("Failure: ", e)

    except Exception as ex:
        print("Failure: ", ex)

    finally:
        if sqliteconn:
            sqliteconn.close()


def display_longest_streak_weekly_habits(username):
    sqliteconn = None

    try:
        # Clear Terminal Screen Before Printing
        clear_screen()

        sqliteconn = sqlite3.connect('../habit_tracker_db.sqlite3')

        # print("Connected to Database Successfully.")
        dbconn = sqliteconn.cursor()

        command = """SELECT HabitName, HabitStatus, MAX(Max_Streak) FROM habits_tracker WHERE username = :usr  AND 
        Period = 'Weekly' AND HabitStatus = 1 """
        dbconn.execute(command, {'usr': username})
        records = dbconn.fetchall()
        lenrecords = len(records)
        # print("Total Habits are: ", lenrecords, "\n")
        # print(records)

        if lenrecords > 0:
            table_records = []
            choice = '10'

            for row in records:
                table_records.append(Min_Max_Conversion(*row))

            print_habit_tracker_table_min_max_values(table_records, choice)

        else:
            print("\nCurrently, There Is No Weekly Habit(s) Available.....")

        sqliteconn.commit()
        sqliteconn.close()

    except sqlite3.Error as e:
        print("Failure: ", e)

    except Exception as ex:
        print("Failure: ", ex)

    finally:
        if sqliteconn:
            sqliteconn.close()


def display_longest_streak_among_all_habits(username):
    sqliteconn = None

    try:
        # Clear Terminal Screen Before Printing
        clear_screen()

        sqliteconn = sqlite3.connect('../habit_tracker_db.sqlite3')

        # print("Connected to Database Successfully.")
        dbconn = sqliteconn.cursor()

        command = """SELECT HabitName, HabitStatus, MAX(Max_Streak) FROM habits_tracker WHERE username = :usr  AND 
        HabitStatus = 1 """
        dbconn.execute(command, {'usr': username})
        records = dbconn.fetchall()
        lenrecords = len(records)
        # print("Total Habits are: ", lenrecords, "\n")
        # print(records)

        if lenrecords > 0:
            table_records = []
            choice = '11'

            for row in records:
                table_records.append(Min_Max_Conversion(*row))

            print_habit_tracker_table_min_max_values(table_records, choice)

        else:
            print("\nCurrently, There Is No Daily/Weekly Habit(s) Available.....")

        sqliteconn.commit()
        sqliteconn.close()

    except sqlite3.Error as e:
        print("Failure: ", e)

    except Exception as ex:
        print("Failure: ", ex)

    finally:
        if sqliteconn:
            sqliteconn.close()


def display_longest_streak_given_habit(habitid, username):
    sqliteconn = None

    try:
        # Clear Terminal Screen Before Printing
        clear_screen()

        sqliteconn = sqlite3.connect('../habit_tracker_db.sqlite3')

        # print("Connected to Database Successfully.")
        dbconn = sqliteconn.cursor()

        command = """SELECT HabitId,HabitName,Description,Period,Born,Start_Date,Due_Date,Streak,Max_Streak,Max_Days,
                            Break,HabitStatus FROM habits_tracker WHERE username = :usr AND HabitStatus = 1"""
        dbconn.execute(command, {'usr': username})
        records = dbconn.fetchall()
        lenrecords = len(records)
        # print("Total Habits are: ", lenrecords, "\n")
        # print(records)

        if lenrecords > 0:
            table_records = []
            user_habits_id_list = []
            choice = '12'

            for row in records:
                user_habits_id_list.append(row[0])
                table_records.append(Display_All_Habits_Columns(*row))
                # print(user_habits_id_list)

            print_habit_tracker_table_all_columns(table_records, choice)

            sqliteconn.commit()

            repeat = True

            while repeat:
                #user_input = input("\nEnter Habit Id To View Its Longest Streak (or Enter -1 to Exit)?: ")
                habit_id = int(habitid)

                if habit_id == -1:
                    print("\nReturn To Main Menu")
                    repeat = False

                else:
                    # habit_exist = False
                    repeat = False

                if habit_id in user_habits_id_list:
                    # print("\nHabit Exists\n")
                    # habit_exist = True

                    command = """SELECT HabitName, HabitStatus, MAX(Max_Streak) FROM habits_tracker WHERE username = 
                    :usr  AND HabitStatus = 1 AND HabitId =:hbt_id """
                    dbconn.execute(command, {'hbt_id': habit_id, 'usr': username})
                    records = dbconn.fetchall()
                    lenrecords = len(records)
                    # print("Total Habits are: ", lenrecords, "\n")
                    # print(records)

                    if lenrecords > 0:
                        table_records = []
                        choice = '12'

                        for row in records:
                            table_records.append(Min_Max_Conversion(*row))

                        print_habit_tracker_table_min_max_values(table_records, choice)

                    else:
                        print("\nCurrently, There Is No Daily/Weekly Habit(s) Available.....")

                    sqliteconn.commit()

                else:
                    print("\nHabit Doesn't Exist")

            sqliteconn.close()

    except sqlite3.Error as e:
        print("Failure: ", e)

    except Exception as ex:
        print("Failure: ", ex)

    finally:
        if sqliteconn:
            sqliteconn.close()


def display_active_habits(username):
    sqliteconn = None

    try:
        # Clear Terminal Screen Before Printing
        clear_screen()

        sqliteconn = sqlite3.connect('../habit_tracker_db.sqlite3')

        # print("Connected to Database Successfully.")
        dbconn = sqliteconn.cursor()

        command = """SELECT HabitId,HabitName,Description,Period,Born,Start_Date,Due_Date,Streak,Max_Streak,Max_Days,
                                    Break,HabitStatus FROM habits_tracker WHERE username = :usr AND HabitStatus = 1"""
        dbconn.execute(command, {'usr': username})
        records = dbconn.fetchall()
        lenrecords = len(records)
        # print("Total Habits are: ", lenrecords, "\n")
        # print(records)

        if lenrecords > 0:
            table_records = []
            choice = '13'

            for row in records:
                table_records.append(Display_All_Habits_Columns(*row))

            print_habit_tracker_table_all_columns(table_records, choice)

        else:
            print("\nCurrently, There Is No Tracked Habit(s) Available.....")

        sqliteconn.commit()
        sqliteconn.close()

    except sqlite3.Error as e:
        print("Failure: ", e)

    except Exception as ex:
        print("Failure: ", ex)

    finally:
        if sqliteconn:
            sqliteconn.close()


def display_completed_habits(username):
    sqliteconn = None

    try:
        # Clear Terminal Screen Before Printing
        clear_screen()

        sqliteconn = sqlite3.connect('../habit_tracker_db.sqlite3')

        # print("Connected to Database Successfully.")
        dbconn = sqliteconn.cursor()

        command = """SELECT HabitId,HabitName,Description,Period,Born,Start_Date,Due_Date,Streak,Max_Streak,Max_Days,
                                    Break,HabitStatus FROM habits_tracker WHERE username = :usr AND HabitStatus = 2"""
        dbconn.execute(command, {'usr': username})
        records = dbconn.fetchall()
        lenrecords = len(records)
        # print("Total Habits are: ", lenrecords, "\n")
        # print(records)

        if lenrecords > 0:
            table_records = []
            choice = '15'

            for row in records:
                table_records.append(Display_All_Habits_Columns(*row))

            print_habit_tracker_table_all_columns(table_records, choice)

        else:
            print("\nCurrently, There Is No Tracked Habit(s) Available.....")

        sqliteconn.commit()
        sqliteconn.close()

    except sqlite3.Error as e:
        print("Failure: ", e)

    except Exception as ex:
        print("Failure: ", ex)

    finally:
        if sqliteconn:
            sqliteconn.close()


def display_deleted_habits(username):
    sqliteconn = None

    try:
        # Clear Terminal Screen Before Printing
        clear_screen()

        sqliteconn = sqlite3.connect('../habit_tracker_db.sqlite3')

        # print("Connected to Database Successfully.")
        dbconn = sqliteconn.cursor()

        command = """SELECT HabitId,HabitName,Description,Period,Born,Start_Date,Due_Date,Streak,Max_Streak,Max_Days,
                                    Break,HabitStatus FROM habits_tracker WHERE username = :usr AND HabitStatus = 0"""
        dbconn.execute(command, {'usr': username})
        records = dbconn.fetchall()
        lenrecords = len(records)
        # print("Total Habits are: ", lenrecords, "\n")
        # print(records)

        if lenrecords > 0:
            table_records = []
            choice = '14'

            for row in records:
                table_records.append(Display_All_Habits_Columns(*row))

            print_habit_tracker_table_all_columns(table_records, choice)

        else:
            print("\nCurrently, There Is No Deleted Habit(s) Available.....")

        sqliteconn.commit()
        sqliteconn.close()

    except sqlite3.Error as e:
        print("Failure: ", e)

    except Exception as ex:
        print("Failure: ", ex)

    finally:
        if sqliteconn:
            sqliteconn.close()


def get_habit_status_color(habitstatus):
    colors = {'✅ ': 'green', '❌ ': 'red', '➠ ': 'blue'}

    if habitstatus in colors:
        return colors[habitstatus]
    return 'white'


def print_habit_tracker_table(tablerecords, choice):
    try:
        # Display Data In Table Form
        if choice == '1':
            table = Table(title="All Tracked Habits", highlight="True", show_header=True, header_style="bold green")

        elif choice == '2':
            table = Table(title="All Deleted Habits", highlight="True", show_header=True, header_style="bold green")

        elif choice == '3':
            table = Table(title="All Completed Habits", highlight="True", show_header=True, header_style="bold green")

        elif choice == '4':
            table = Table(title="All Active Daily Habits", highlight="True", show_header=True,
                          header_style="bold green")

        if choice == '5':
            table = Table(title="All Active Weekly Habits", highlight="True", show_header=True,
                          header_style="bold green")

        table.add_column("Habit Name", justify="center", no_wrap=True)
        table.add_column("Description", justify="left", no_wrap=True)
        table.add_column("Period", justify="left", no_wrap=True)
        table.add_column("Born", justify="center", no_wrap=True)
        table.add_column("Start Date", justify="center", no_wrap=True)
        table.add_column("Due Date", justify="center", no_wrap=True)
        table.add_column("Streak", justify="center")
        table.add_column("Max Streak", justify="center")
        table.add_column("Max Days", justify="center")
        table.add_column("Break", justify="center")
        table.add_column("Habit Status", justify="left")
        # table.add_column("UserName", justify="center", no_wrap=False)

        for row in tablerecords:
            c = get_habit_status_color(row.HabitStatus)
            table.add_row(row.HabitName, row.Description, row.Period, row.Born, row.Start_Date, row.Due_Date,
                          row.Streak, row.Max_Streak, row.Max_Days, row.Break, f'[{c}] {row.HabitStatus}[/{c}]')

        console = Console()
        console.print(table, justify="center")
        print("\nPlease wait.....")
        time.sleep(5)

    except Exception as ex:
        print("Failure: ", ex)


def print_habit_tracker_table_min_max_values(tablerecords, choice):
    try:
        # Display Data In Table Form
        if choice == '6':
            table = Table(title="Smallest Streak Daily Habits", highlight="True", show_header=True,
                          header_style="bold green")
            table.add_column("Habit Name", justify="center", no_wrap=True)
            table.add_column("Smallest Streak", justify="center")

        elif choice == '7':
            table = Table(title="Smallest Streak Weekly Habits", highlight="True", show_header=True,
                          header_style="bold green")
            table.add_column("Habit Name", justify="center", no_wrap=True)
            table.add_column("Smallest Streak", justify="center")

        elif choice == '8':
            table = Table(title="Smallest Streak Among All Habits (Daily or Weekly)", highlight="True",
                          show_header=True, header_style="bold green")
            table.add_column("Habit Name", justify="center", no_wrap=True)
            table.add_column("Smallest Streak", justify="center")

        elif choice == '9':
            table = Table(title="Longest Streak Daily Habits", highlight="True", show_header=True,
                          header_style="bold green")
            table.add_column("Habit Name", justify="center", no_wrap=True)
            table.add_column("Longest Streak", justify="center")

        elif choice == '10':
            table = Table(title="Longest Streak Weekly Habits", highlight="True", show_header=True,
                          header_style="bold green")
            table.add_column("Habit Name", justify="center", no_wrap=True)
            table.add_column("Longest Streak", justify="center")

        elif choice == '11':
            table = Table(title="Longest Streak Among All Habits (Daily or Weekly)", highlight="True", show_header=True,
                          header_style="bold green")
            table.add_column("Habit Name", justify="center", no_wrap=True)
            table.add_column("Longest Streak", justify="center")

        elif choice == '12':
            table = Table(title="Longest Streak Given Habit", highlight="True", show_header=True,
                          header_style="bold green")
            table.add_column("Habit Name", justify="center", no_wrap=True)
            table.add_column("Longest Streak", justify="center")

        table.add_column("Habit Status", justify="left")
        # table.add_column("UserName", justify="center", no_wrap=False)

        for row in tablerecords:
            c = get_habit_status_color(row.HabitStatus)
            table.add_row(row.HabitName, row.StreakValue, f'[{c}] {row.HabitStatus}[/{c}]')

        console = Console()
        console.print(table, justify="center")
        print("\nPlease wait.....")
        time.sleep(5)

    except Exception as ex:
        print("Failure: ", ex)


def print_habit_tracker_table_all_columns(tablerecords, choice):
    try:
        # Display Data In Table Form
        if choice == '12':
            table = Table(title="All Tracked Habits", highlight="True", show_header=True, header_style="bold green")

        elif choice == '13':
            table = Table(title="All Tracked Habits", highlight="True", show_header=True, header_style="bold green")

        elif choice == '14':
            table = Table(title="All Deleted Habits", highlight="True", show_header=True, header_style="bold green")

        elif choice == '15':
            table = Table(title="All Completed Habits", highlight="True", show_header=True, header_style="bold green")

        table.add_column("Habit ID", justify="center", no_wrap=True)
        table.add_column("Habit Name", justify="center", no_wrap=True)
        table.add_column("Description", justify="left", no_wrap=True)
        table.add_column("Period", justify="left", no_wrap=True)
        table.add_column("Born", justify="center", no_wrap=True)
        table.add_column("Start Date", justify="center", no_wrap=True)
        table.add_column("Due Date", justify="center", no_wrap=True)
        table.add_column("Streak", justify="center")
        table.add_column("Max Streak", justify="center")
        table.add_column("Max Days", justify="center")
        table.add_column("Break", justify="center")
        table.add_column("Habit Status", justify="left")
        # table.add_column("UserName", justify="center", no_wrap=False)

        for row in tablerecords:
            c = get_habit_status_color(row.HabitStatus)
            table.add_row(row.HabitId, row.HabitName, row.Description, row.Period, row.Born, row.Start_Date,
                          row.Due_Date,
                          row.Streak, row.Max_Streak, row.Max_Days, row.Break, f'[{c}] {row.HabitStatus}[/{c}]')

        console = Console()
        console.print(table, justify="center")
        print("\nPlease wait.....")
        time.sleep(5)

    except Exception as ex:
        print("Failure: ", ex)
