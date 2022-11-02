import sqlite3
import datetime
import time
from datetime import datetime, timedelta
from Habit_Tracker_Package.Convert_Table_Columns_String import Cast_Table_Columns_String
from rich.console import Console
from rich.table import Table


def insertpredefinedhabits(usr_name):
    """The purpose of this function is to insert predefined habits to habit tracker list when new user is created."""
    sqliteconn = None

    try:
        sqliteconn = sqlite3.connect('../habit_tracker_db.sqlite3')
        dbconn = sqliteconn.cursor()

        # Today's Date
        current_date = datetime.today().date()
        #print("Today: ", current_date)

        # Yesterday's Date
        previous_date = current_date - timedelta(days=1)
        previous2_date = current_date - timedelta(days=2)
        #print("Yesterday: ", previous_date)

        # Tomorrow's Date
        next_date_daily = current_date + timedelta(days=1)
        #print("Tomorrow: ", next_date_daily)

        next_date_weekly = current_date + timedelta(days=7)
        #print("Tomorrow: ", next_date_weekly)

        habits = [('Drink Water', 'Drink 2 Liters of Water', 'Daily', current_date, current_date, next_date_daily, 0, 0, 0, 0, 1, usr_name),
                  ('Offer Prayer', 'Offer Prayer 5 Time a Day', 'Daily', current_date, current_date, next_date_daily, 0, 0, 0, 0, 1, usr_name),
                  ('No Sugar', 'Take No Sugar', 'Daily', current_date, current_date, next_date_daily, 0, 0, 0, 0, 1, usr_name),
                  ('Play Sports', 'Play Cricket Daily', 'Daily', current_date, current_date, next_date_daily, 0, 0, 0, 0, 1, usr_name),
                  ('Cleaning', 'Clean House on Weekend', 'Weekly', current_date, current_date, next_date_weekly, 0, 0, 0, 0, 1, usr_name),
                  ('Eat Fruit', 'Eat 1 Apple Daily', 'Daily', current_date, current_date, next_date_daily, 0, 0, 0, 0, 1, usr_name),
                  ('Community Work', 'Help others', 'Weekly', current_date, current_date, next_date_weekly, 0, 0, 0, 0, 1,usr_name),
                  ('Teeth Brush', 'Do Teeth Burshing 2 Times a Day', 'Daily', current_date, current_date, next_date_daily, 0, 0, 0, 0, 1, usr_name)
                  ]

        habits2 = [('Drink Water', 'Drink 2 Liters of Water', 'Daily', previous2_date, previous2_date, previous_date, 1, 1,
                   2, 0, 1, usr_name),
                  ('Offer Prayer', 'Offer Prayer 5 Time a Day', 'Daily', previous_date, previous_date, previous_date, 2,
                   2, 2, 0, 1, usr_name),
                  ('No Sugar', 'Take No Sugar', 'Daily', current_date, current_date, next_date_daily, 0, 0, 0, 0, 1,
                   usr_name),
                  (
                  'Play Sports', 'Play Cricket Daily', 'Daily', current_date, current_date, next_date_daily, 0, 0, 0, 0,
                  1, usr_name),
                  (
                  'Cleaning', 'Clean House on Weekend', 'Weekly', current_date, current_date, next_date_weekly, 10, 10, 0,
                  0, 1, usr_name),
                  (
                  'Eat Fruit', 'Eat 1 Apple Daily', 'Daily', current_date, current_date, next_date_daily, 0, 0, 0, 0, 1,
                  usr_name),
                  ('Community Work', 'Help others', 'Weekly', current_date, current_date, next_date_weekly, 0, 0, 0, 0,
                   1, usr_name),
                  ('Teeth Brush', 'Do Teeth Burshing 2 Times a Day', 'Daily', current_date, current_date,
                   next_date_daily, 0, 0, 0, 0, 1, usr_name)
                  ]

        dbconn.executemany(
            "INSERT INTO habits_tracker ('HabitName','Description','Period','Born','Start_Date','Due_Date','Streak',"
            "'Max_Streak', 'Max_Days', 'Break', 'HabitStatus', 'UserName') VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
            habits2)
        sqliteconn.commit()
        print("8 Predefined Habits Has Been Added To ( ", usr_name, " ) Tracker....")
        time.sleep(3)

        dbconn.close()

    except sqlite3.Error as e:
        print("Failure: ", e)

    except Exception as ex:
        print("Failure: ", ex)

    finally:
        if sqliteconn:
            sqliteconn.close()


def loadpredefinedhabits(username):
    """The purpose of this function is to display the predefined habits to user when user login into habit tracker. It also displays the progress bar before displaying habit tracker list."""
    sqliteconn = None

    try:
        from Habit_Tracker_Package import Clear_Screen_and_Progress_Bar
        Clear_Screen_and_Progress_Bar.Progress()

        sqliteconn = sqlite3.connect('../habit_tracker_db.sqlite3')

        # print("Connected to Database Successfully.")
        dbconn = sqliteconn.cursor()

        command = """SELECT HabitName, Description, Period, Born, Start_Date, Due_Date, Streak, Max_Streak, Max_Days, 
        Break, HabitStatus FROM habits_tracker WHERE username = :usr AND HabitStatus = 1 """
        dbconn.execute(command, {'usr': username})
        records = dbconn.fetchall()
        lenrecords = len(records)

        if lenrecords > 0:
            table_records = []

            for row in records:
                table_records.append(Cast_Table_Columns_String(*row))

            # Display Data In Table Form
            table = Table(title="All Predefined Habits", highlight="True", show_header=True, header_style="bold green")
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

            def get_habit_status_color(habitstatus):
                COLORS = {'✅ ': 'green', '❌ ': 'red', '➠ ': 'blue'}
                if habitstatus in COLORS:
                    return COLORS[habitstatus]
                return 'white'

            for row in table_records:
                c = get_habit_status_color(row.HabitStatus)
                table.add_row(row.HabitName, row.Description, row.Period, row.Born, row.Start_Date, row.Due_Date,
                              row.Streak, row.Max_Streak, row.Max_Days, row.Break, f'[{c}] {row.HabitStatus}[/{c}]')

            console = Console()
            console.print(table, justify="center")
            time.sleep(3)

        else:
            print("Currently, There Is No Predefined Habit(s) Available.....")
            time.sleep(2)

        sqliteconn.commit()
        dbconn.close()

    except sqlite3.Error as e:
        print("Failure: ", e)

    except Exception as ex:
        print("Failure: ", ex)

    finally:
        if sqliteconn:
            sqliteconn.close()
