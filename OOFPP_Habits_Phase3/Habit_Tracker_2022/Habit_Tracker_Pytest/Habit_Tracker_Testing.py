import sqlite3
import time
import datetime
from datetime import datetime, timedelta
from rich.console import Console
from Create_User_And_Login_Test import create_user, login
from Empty_Tables_Test import empty_users_tables, empty_habit_tracker_tables, drop_habit_table
from Tables_Creation_Test import usertablecreation, habittablecreation
from Predefined_Habits_Test import loadpredefinedhabits
from Create_New_Habit_Test import create_new_habit
from Manage_Habits_Test import checked_off_habit
from Complete_Max_Days_And_Reset_Overdue_Habits_Test import complete_max_days_and_reset_overdue_habits


# Test Case 1: Create User & Habit Tables Creation
def test_table_creations():
    sqliteconn = None
    try:
        console = Console()
        print("\n")
        console.print(f'[green]**************************************************[/green]')
        console.print(f'[green]Test Case 1: User & Habit Tables Creation[/green]')
        console.print(f'[green]**************************************************[/green]')
        time.sleep(3)
        usertablecreation()
        habittablecreation()

        # Create a SQL connection to our SQLite database
        sqliteconn = sqlite3.connect('../habit_tracker_db.sqlite3')
        dbconn = sqliteconn.cursor()

        # Check If User Table Created Successfully.
        command = """SELECT EXISTS(SELECT 1 FROM sqlite_master WHERE type = "table" AND name = "users")"""
        dbconn.execute(command)
        records = dbconn.fetchall()
        sqliteconn.commit()
        user_table_exist = 0

        for row in records:
            user_table_exist = row[0]

        assert user_table_exist == 1, "User table not created"  # 0: Table doesn't exist. 1: Table exist

        # Check If Habit Tracker Table Created Successfully.
        command = """SELECT EXISTS(SELECT 1 FROM sqlite_master WHERE type = "table" AND name = "habits_tracker")"""
        dbconn.execute(command)
        records = dbconn.fetchall()
        sqliteconn.commit()
        habit_table_exist = 0

        for row in records:
            habit_table_exist = row[0]

        assert habit_table_exist == 1, "Habit Tracker table not created"  # 0: Table doesn't exist. 1: Table exist

    except Exception as ex:
        print("\nFailure: ", ex)
        print("\nPlease Wait....\n")
        time.sleep(3)

    finally:
        if sqliteconn:
            sqliteconn.close()


# Test Case 2: Empty User & Habit Tables
def test_empty_tables():
    sqliteconn = None

    try:
        console = Console()
        print("\n")
        console.print(f'[green]**************************************************[/green]')
        console.print(f'[green]Test Case 2: Empty User & Habit Tables[/green]')
        console.print(f'[green]**************************************************[/green]')
        time.sleep(3)
        empty_users_tables()
        empty_habit_tracker_tables()

        # Create a SQL connection to our SQLite database
        sqliteconn = sqlite3.connect('../habit_tracker_db.sqlite3')
        dbconn = sqliteconn.cursor()

        # Check If User Table Is Empty.
        command = """SELECT * FROM users"""
        dbconn.execute(command)
        records = dbconn.fetchall()
        userlenrecords = len(records)
        sqliteconn.commit()

        assert userlenrecords == 0, "User table must be empty"

        # Check If Habit Tracker Table Is Empty.
        command = """SELECT * FROM habits_tracker"""
        dbconn.execute(command)
        records = dbconn.fetchall()
        habitlenrecords = len(records)
        sqliteconn.close()

        assert habitlenrecords == 0, "Habit Tracker table must be empty"

    except Exception as ex:
        print("\nFailure: ", ex)
        print("\nPlease Wait....\n")
        time.sleep(3)

    finally:
        if sqliteconn:
            sqliteconn.close()


# Test Case 3: Create User
def test_create_user():
    sqliteconn = None

    try:
        console = Console()
        print("\n")
        console.print(f'[green]**************************************************[/green]')
        console.print(f'[green]Test Case 3: Create User[/green]')
        console.print(f'[green]**************************************************[/green]')
        time.sleep(3)
        fullname = "Muhammad Ali"
        username = "mali1225"
        password = "kaaba786"
        create_user(fullname, username, password)

        # Create a SQL connection to our SQLite database
        sqliteconn = sqlite3.connect('../habit_tracker_db.sqlite3')
        dbconn = sqliteconn.cursor()

        # Check If User is created or not.
        command = """SELECT * FROM users WHERE username = :usr AND password = :pass"""
        dbconn.execute(command, {'usr': username, 'pass': password})
        records = dbconn.fetchall()
        usercreatedlenrecords = len(records)
        sqliteconn.close()

        assert usercreatedlenrecords == 1, "User is not created"

    except Exception as ex:
        print("\nFailure: ", ex)
        print("\nPlease Wait....\n")
        time.sleep(3)

    finally:
        if sqliteconn:
            sqliteconn.close()


# Test Case 4: Login User
def test_user_login():
    sqliteconn = None

    try:
        console = Console()
        print("\n")
        console.print(f'[green]**************************************************[/green]')
        console.print(f'[green]Test Case 4: Login User[/green]')
        console.print(f'[green]**************************************************[/green]')
        time.sleep(3)
        username = "mali1225"
        password = "kaaba786"
        login(username, password)

        # Create a SQL connection to our SQLite database
        sqliteconn = sqlite3.connect('../habit_tracker_db.sqlite3')
        dbconn = sqliteconn.cursor()

        # Check If User is created or not.
        command = """SELECT * FROM users WHERE username = :usr AND password = :pass"""
        dbconn.execute(command, {'usr': username, 'pass': password})
        records = dbconn.fetchall()
        userloginlenrecords = len(records)
        sqliteconn.close()

        assert userloginlenrecords == 1, "Username & Password is incorrect."

    except Exception as ex:
        print("\nFailure: ", ex)
        print("\nPlease Wait....\n")
        time.sleep(3)

    finally:
        if sqliteconn:
            sqliteconn.close()


# Test Case 5: Display User's Predefined Habits
def test_load_predefined_habits():
    sqliteconn = None

    try:
        console = Console()
        print("\n")
        console.print(f'[green]**************************************************[/green]')
        console.print(f'[green]Test Case 5: Display Users Predefined Habits[/green]')
        console.print(f'[green]**************************************************[/green]')
        time.sleep(3)
        username = "mali1225"
        loadpredefinedhabits(username)

        # Create a SQL connection to our SQLite database
        sqliteconn = sqlite3.connect('../habit_tracker_db.sqlite3')
        dbconn = sqliteconn.cursor()

        # Check If Habit exists or not.
        command = """SELECT * FROM habits_tracker WHERE username = :usr"""
        dbconn.execute(command, {'usr': username})
        records = dbconn.fetchall()
        userpredefinedhabitcount = len(records)

        assert userpredefinedhabitcount > 0, "User doesn't have any habit(s)."

    except Exception as ex:
        print("\nFailure: ", ex)
        print("\nPlease Wait....\n")
        time.sleep(3)

    finally:
        if sqliteconn:
            sqliteconn.close()


# Test Case 6: Create New Habit
def test_create_new_habits():
    sqliteconn = None

    try:
        console = Console()
        print("\n")
        console.print(f'[green]**************************************************[/green]')
        console.print(f'[green]Test Case 6.a: Create New Daily Habit[/green]')
        console.print(f'[green]**************************************************[/green]')
        time.sleep(3)
        username = "mali1225"
        HabitName = "Eat Vegetable"
        Description = "Eat Tomato, Onion"
        Period = "d"
        Max_Days = 10  # If Habit Period is d: Daily. Please Set Max_Days = (Number >= 1) AND  Max_Weeks = 0
        Max_Weeks = 0  # If Habit Period is w: Weekly. Please Set Max_Days = 0 AND  Max_Weeks = (Number >= 1)
        create_new_habit(HabitName, Description, Period, Max_Days, Max_Weeks, username)

        # Create a SQL connection to our SQLite database
        sqliteconn = sqlite3.connect('../habit_tracker_db.sqlite3')
        dbconn = sqliteconn.cursor()

        # Check If Daily Habit exists or not.
        command = """SELECT * FROM habits_tracker WHERE username = :usr AND HabitName = :hbt_name"""
        dbconn.execute(command, {'usr': username, 'hbt_name': HabitName})
        records = dbconn.fetchall()
        createdailyhabitcount = len(records)

        assert createdailyhabitcount > 0, "Daily Habit not created."

        print("\n")
        console.print(f'[green]**************************************************[/green]')
        console.print(f'[green]Test Case 6.b: Create New Weekly Habit[/green]')
        console.print(f'[green]**************************************************[/green]')
        time.sleep(3)
        username = "mali1225"
        HabitName = "Enjoy Life"
        Description = "Watch Movie, Fun with Friends"
        Period = "w"
        Max_Days = 0  # If Habit Period is d: Daily. Please Set Max_Days = (Number >= 1) AND  Max_Weeks = 0
        Max_Weeks = 2  # If Habit Period is w: Weekly. Please Set Max_Days = 0 AND  Max_Weeks = (Number >= 1)
        create_new_habit(HabitName, Description, Period, Max_Days, Max_Weeks, username)

        # Check If Weekly Habit exists or not.
        command = """SELECT * FROM habits_tracker WHERE username = :usr AND HabitName = :hbt_name"""
        dbconn.execute(command, {'usr': username, 'hbt_name': HabitName})
        records = dbconn.fetchall()
        sqliteconn.close()
        createweeklyhabitcount = len(records)

        assert createweeklyhabitcount > 0, "Weekly Habit not created."


    except Exception as ex:
        print("\nFailure: ", ex)
        print("\nPlease Wait....\n")
        time.sleep(3)

    finally:
        if sqliteconn:
            sqliteconn.close()


# Test Case 7: Manage Habits (Complete Task)
def test_manage_habits():
    sqliteconn = None

    try:
        console = Console()
        print("\n")
        console.print(f'[green]**************************************************[/green]')
        console.print(f'[green]Test Case 7.a: Manage Habits (Complete Daily Task)[/green]')
        console.print(f'[green]**************************************************[/green]')
        time.sleep(3)
        username = "mali1225"
        habib_id = 4  # Check Off Daily Habit (4, 6)
        checked_off_habit(habib_id, username)

        # Today's Date
        current_date = datetime.today().date()
        #print("Today: ", current_date)

        # Yesterday's Date
        previous_date = current_date - timedelta(days=1)
        #print("Yesterday: ", previous_date)

        # Tomorrow's Date
        next_start_date_daily = current_date + timedelta(days=1)
        next_due_date_daily = current_date + timedelta(days=2)
        #print("Tomorrow: ", next_date_daily)

        next_start_date_weekly = current_date + timedelta(days=7)
        next_due_date_weekly = current_date + timedelta(days=14)
        #print("Tomorrow: ", next_date_weekly)

        # Create a SQL connection to our SQLite database
        sqliteconn = sqlite3.connect('../habit_tracker_db.sqlite3')
        dbconn = sqliteconn.cursor()

        # Check If Daily Habit Checked Off or not.
        command = """SELECT HabitId,HabitName,Period,Start_Date,Due_Date,Streak,Max_Streak FROM habits_tracker WHERE username = :usr AND HabitId = :hbt_id"""
        dbconn.execute(command, {'usr': username, 'hbt_id': habib_id})
        records = dbconn.fetchall()
        sqliteconn.commit()

        dailyhabit = [(4, 'Play Sports', 'Daily', str(next_start_date_daily), str(next_due_date_daily), 1, 1)]

        assert list(records) == dailyhabit, "Daily Habit not checked off." #[(4, 'Play Sports', 'Daily', '2022-10-28', '2022-10-29', 1, 1)], "Daily Habit not checked off."


        print("\n")
        console.print(f'[green]***************************************************[/green]')
        console.print(f'[green]Test Case 7.b: Manage Habits (Complete Weekly Task)[/green]')
        console.print(f'[green]***************************************************[/green]')
        time.sleep(3)
        username = "mali1225"
        habib_id = 10  # Check Off Weekly Habit ()
        checked_off_habit(habib_id, username)

        # Check If Daily Habit Checked Off or not.
        command = """SELECT HabitId,HabitName,Period,Start_Date,Due_Date,Streak,Max_Streak FROM habits_tracker WHERE username = :usr AND HabitId = :hbt_id"""
        dbconn.execute(command, {'usr': username, 'hbt_id': habib_id})
        records = dbconn.fetchall()
        sqliteconn.commit()

        weeklyhabit = [(10, 'Enjoy Life', 'Weekly', str(next_start_date_weekly), str(next_due_date_weekly), 1, 1)]
        print(records)
        print(weeklyhabit)

        assert list(
            records) == weeklyhabit, "Weekly Habit not checked off."  # [(4, 'Play Sports', 'Daily', '2022-10-28', '2022-10-29', 1, 1)], "Daily Habit not checked off."

    except Exception as ex:
        print("\nFailure: ", ex)
        print("\nPlease Wait....\n")
        time.sleep(3)

    finally:
        if sqliteconn:
            sqliteconn.close()


# Test Case 8: Modify, Delete & Restore Habits
def test_modify_delete_restore_habits():
    sqliteconn = None
    try:

        # Create a SQL connection to our SQLite database
        sqliteconn = sqlite3.connect('../habit_tracker_db.sqlite3')
        dbconn = sqliteconn.cursor()

        console = Console()
        print("\n")
        console.print(f'[green]**************************************************[/green]')
        console.print(f'[green]Test Case 8: Modify, Delete & Restore Habits[/green]')
        console.print(f'[green]**************************************************[/green]')
        time.sleep(1)

        # ============================================================================================
        # ============================================================================================

        console = Console()
        print("\n")
        console.print(f'[green]**************************************************[/green]')
        console.print(f'[green]Test Case 8.a: Change Habit Title[/green]')
        console.print(f'[green]**************************************************[/green]')
        time.sleep(3)
        username = "mali1225"
        habib_id = 4  # Change title of Habit Id = 4, Habit Title = Play Sports (4, 6)
        habit_title = "Sports"

        from Modify_Delete_Restore_Habits_Test import change_habit_title
        change_habit_title(habib_id, habit_title, username)

        from Analyze_Your_Habits_Test import display_active_habits
        display_active_habits(username)

        # Check If Habit Title Changed
        command = """SELECT HabitId,HabitName FROM habits_tracker WHERE username = :usr AND HabitId = :hbt_id AND HabitStatus = 1"""
        dbconn.execute(command, {'usr': username, 'hbt_id': habib_id})
        records = dbconn.fetchall()
        sqliteconn.commit()

        habittitle = [(4, habit_title)]

        assert list(records) == habittitle, "Habit title not changed."

        # ============================================================================================
        # ============================================================================================

        console = Console()
        print("\n")
        print("\n")
        console.print(f'[green]**************************************************[/green]')
        console.print(f'[green]Test Case 8.b: Change Habit Description[/green]')
        console.print(f'[green]**************************************************[/green]')
        time.sleep(3)
        username = "mali1225"
        habib_id = 5  # Change description of Habit Id = 5, Habit Description = Clean House on Weekend
        habit_description = "House Keeping"

        from Modify_Delete_Restore_Habits_Test import change_habit_description
        change_habit_description(habib_id, habit_description, username)

        from Analyze_Your_Habits_Test import display_active_habits
        display_active_habits(username)

        # Check If Habit Description Changed
        command = """SELECT HabitId,Description FROM habits_tracker WHERE username = :usr AND HabitId = :hbt_id AND HabitStatus = 1"""
        dbconn.execute(command, {'usr': username, 'hbt_id': habib_id})
        records = dbconn.fetchall()
        sqliteconn.commit()

        habitdesc = [(5, habit_description)]

        assert list(records) == habitdesc, "Habit Description not changed."

        # ============================================================================================
        # ============================================================================================

        console = Console()
        print("\n")
        print("\n")
        console.print(f'[green]**************************************************[/green]')
        console.print(f'[green]Test Case 8.c: Change Habit Period To Daily[/green]')
        console.print(f'[green]**************************************************[/green]')
        time.sleep(3)
        username = "mali1225"
        habib_id = 7  # Change Habit Period = 'Daily' of Habit Id = 7

        from Modify_Delete_Restore_Habits_Test import change_habit_period_to_daily
        change_habit_period_to_daily(habib_id, username)

        from Analyze_Your_Habits_Test import display_active_habits
        display_active_habits(username)

        # Check If Habit Period Changed To Daily From Weekly
        command = """SELECT HabitId,Period FROM habits_tracker WHERE username = :usr AND HabitId = :hbt_id AND HabitStatus = 1"""
        dbconn.execute(command, {'usr': username, 'hbt_id': habib_id})
        records = dbconn.fetchall()
        sqliteconn.commit()

        habitperiod = [(7, 'Daily')]

        assert list(records) == habitperiod, "Habit Period not changed."

        # ============================================================================================
        # ============================================================================================

        console = Console()
        print("\n")
        print("\n")
        console.print(f'[green]**************************************************[/green]')
        console.print(f'[green]Test Case 8.d: Change Habit Period To Weekly[/green]')
        console.print(f'[green]**************************************************[/green]')
        time.sleep(3)
        username = "mali1225"
        habib_id = 4  # Change Habit Period = 'Weekly' of Habit Id = 4

        from Modify_Delete_Restore_Habits_Test import change_habit_period_to_weekly
        change_habit_period_to_weekly(habib_id, username)

        from Analyze_Your_Habits_Test import display_active_habits
        display_active_habits(username)

        # Check If Habit Period Changed To Weekly From Daily
        command = """SELECT HabitId,Period FROM habits_tracker WHERE username = :usr AND HabitId = :hbt_id AND HabitStatus = 1"""
        dbconn.execute(command, {'usr': username, 'hbt_id': habib_id})
        records = dbconn.fetchall()
        sqliteconn.commit()

        habitperiod = [(4, 'Weekly')]

        assert list(records) == habitperiod, "Habit Period not changed."

        # ============================================================================================
        # ============================================================================================

        console = Console()
        print("\n")
        print("\n")
        console.print(f'[green]**************************************************[/green]')
        console.print(f'[green]Test Case 8.e: Change Habit Max Days[/green]')
        console.print(f'[green]**************************************************[/green]')
        time.sleep(3)
        username = "mali1225"
        habib_id = 8  # Change Habit Max Days = 12 of Habit Id = 8
        max_days = 12

        from Modify_Delete_Restore_Habits_Test import change_habit_max_days
        change_habit_max_days(habib_id, max_days, username)

        from Analyze_Your_Habits_Test import display_active_habits
        display_active_habits(username)

        # Check If Habit Period Changed To Weekly From Daily
        command = """SELECT HabitId,Max_Days FROM habits_tracker WHERE username = :usr AND HabitId = :hbt_id AND HabitStatus = 1"""
        dbconn.execute(command, {'usr': username, 'hbt_id': habib_id})
        records = dbconn.fetchall()
        sqliteconn.commit()

        habitmaxdays = [(8, 12)]

        assert list(records) == habitmaxdays, "Habit Max Day not changed."

        # ============================================================================================
        # ============================================================================================

        console = Console()
        print("\n")
        print("\n")
        console.print(f'[green]**************************************************[/green]')
        console.print(f'[green]Test Case 8.f: Delete Habit[/green]')
        console.print(f'[green]**************************************************[/green]')
        time.sleep(3)

        # *******************************************************************************
        # *******************************************************************************

        username = "mali1225"
        habib_id = 6  # Delete Habit Id = 6

        from Modify_Delete_Restore_Habits_Test import delete_habit
        delete_habit(habib_id, username)

        from Analyze_Your_Habits_Test import display_active_habits
        display_active_habits(username)

        # Check If Habit Id = 6 Deleted
        command = """SELECT * FROM habits_tracker WHERE username = :usr AND HabitId = :hbt_id AND HabitStatus = 1"""
        dbconn.execute(command, {'usr': username, 'hbt_id': habib_id})
        records = dbconn.fetchall()
        lenrecords = len(records)
        sqliteconn.commit()

        assert lenrecords == 0, "Habit not deleted."

        # *******************************************************************************
        # *******************************************************************************

        username = "mali1225"
        habib_id = 8  # Delete Habit Id = 8

        from Modify_Delete_Restore_Habits_Test import delete_habit
        delete_habit(habib_id, username)

        from Analyze_Your_Habits_Test import display_active_habits
        display_active_habits(username)

        # Check If Habit Id = 8 Deleted
        command = """SELECT * FROM habits_tracker WHERE username = :usr AND HabitId = :hbt_id AND HabitStatus = 1"""
        dbconn.execute(command, {'usr': username, 'hbt_id': habib_id})
        records = dbconn.fetchall()
        lenrecords = len(records)
        sqliteconn.commit()

        assert lenrecords == 0, "Habit not deleted."

        # *******************************************************************************
        # *******************************************************************************

        username = "mali1225"
        habib_id = 9  # Delete Habit Id = 9

        from Modify_Delete_Restore_Habits_Test import delete_habit
        delete_habit(habib_id, username)

        from Analyze_Your_Habits_Test import display_active_habits
        display_active_habits(username)

        # Check If Habit Id = 8 Deleted
        command = """SELECT * FROM habits_tracker WHERE username = :usr AND HabitId = :hbt_id AND HabitStatus = 1"""
        dbconn.execute(command, {'usr': username, 'hbt_id': habib_id})
        records = dbconn.fetchall()
        lenrecords = len(records)
        sqliteconn.commit()

        assert lenrecords == 0, "Habit not deleted."

        # ============================================================================================
        # ============================================================================================

        console = Console()
        print("\n")
        print("\n")
        console.print(f'[green]**************************************************[/green]')
        console.print(f'[green]Test Case 8.g: Restore Deleted Habit[/green]')
        console.print(f'[green]**************************************************[/green]')
        time.sleep(3)

        username = "mali1225"
        habib_id = 9  # Restore Habit Id = 9

        from Modify_Delete_Restore_Habits_Test import restore_deleted_habit
        restore_deleted_habit(habib_id, username)

        from Analyze_Your_Habits_Test import display_deleted_habits
        display_deleted_habits(username)

        from Analyze_Your_Habits_Test import display_active_habits
        display_active_habits(username)

        # Check If Habit Id = 9 Restored
        command = """SELECT * FROM habits_tracker WHERE username = :usr AND HabitId = :hbt_id AND HabitStatus = 1"""
        dbconn.execute(command, {'usr': username, 'hbt_id': habib_id})
        records = dbconn.fetchall()
        lenrecords = len(records)
        sqliteconn.commit()

        assert lenrecords == 1, "Habit not restored."

        # ============================================================================================
        # ============================================================================================

    except Exception as ex:
        print("\nFailure: ", ex)
        print("\nPlease Wait....\n")
        time.sleep(3)

    finally:
        if sqliteconn:
            sqliteconn.close()


# Test Case 9: Restore Completed Habit
def test_restore_completed_habits():
    sqliteconn = None

    try:
        console = Console()
        print("\n")
        console.print(f'[green]**************************************************[/green]')
        console.print(f'[green]Test Case 9: Restore Completed Habit[/green]')
        console.print(f'[green]**************************************************[/green]')
        time.sleep(3)
        username = "mali1225"
        habib_id = 2  # Restore Completed Habit

        from Modify_Delete_Restore_Habits_Test import restore_completed_habit
        restore_completed_habit(habib_id, username)

        from Analyze_Your_Habits_Test import display_all_completed_habits
        display_all_completed_habits(username)

        # Create a SQL connection to our SQLite database
        sqliteconn = sqlite3.connect('../habit_tracker_db.sqlite3')
        dbconn = sqliteconn.cursor()

        # Check If Habit Id = 2 Move From Completed to Active
        command = """SELECT * FROM habits_tracker WHERE username = :usr AND HabitId = :hbt_id AND HabitStatus = 1"""
        dbconn.execute(command, {'usr': username, 'hbt_id': habib_id})
        records = dbconn.fetchall()
        lenrecords = len(records)
        sqliteconn.commit()
        sqliteconn.close()

        assert lenrecords == 1, "Habit not moved to Active from Completed."

    except Exception as ex:
        print("\nFailure: ", ex)
        print("\nPlease Wait....\n")
        time.sleep(3)

    finally:
        if sqliteconn:
            sqliteconn.close()


# Test Case 10: Auto Reset Over Due Habits & Mark Habit as Completed When (Max_Streak = Max_Days)
def test_auto_overdue_and_complete_habits():
    sqliteconn = None

    try:
        console = Console()
        print("\n")
        console.print(
            f'[green]***********************************************************************************************[/green]')
        console.print(
            f'[green]Test Case 10: Auto Reset Over Due Habits & Mark Habit as Completed When (Max_Streak = Max_Days)[/green]')
        console.print(
            f'[green]***********************************************************************************************[/green]')
        time.sleep(3)
        username = "mali1225"
        habib_id = 2  # Mark Habit Id 2 as Completed
        complete_max_days_and_reset_overdue_habits(username)

        from Analyze_Your_Habits_Test import display_active_habits
        display_active_habits(username)

        from Analyze_Your_Habits_Test import display_all_completed_habits
        display_all_completed_habits(username)

        # Create a SQL connection to our SQLite database
        sqliteconn = sqlite3.connect('../habit_tracker_db.sqlite3')
        dbconn = sqliteconn.cursor()

        # Check If Habit Id = 2 marked as Completed
        command = """SELECT * FROM habits_tracker WHERE username = :usr AND HabitId = :hbt_id AND HabitStatus = 2"""
        dbconn.execute(command, {'usr': username, 'hbt_id': habib_id})
        records = dbconn.fetchall()
        lenrecords = len(records)
        sqliteconn.commit()
        #sqliteconn.close()

        assert lenrecords == 1, "Habit not Completed."

        habib_id = 1  # Reset Habit Id 1 over due date

        # Check If Habit Id = 1 has reset
        command = """SELECT * FROM habits_tracker WHERE username = :usr AND HabitId = :hbt_id AND HabitStatus = 1 AND Break > 0 AND Streak = 0 AND Max_Streak = 0"""
        dbconn.execute(command, {'usr': username, 'hbt_id': habib_id})
        records = dbconn.fetchall()
        lenrecords = len(records)
        sqliteconn.commit()
        # sqliteconn.close()

        assert lenrecords == 1, "Habit not Reset."

    except Exception as ex:
        print("\nFailure: ", ex)
        print("\nPlease Wait....\n")
        time.sleep(3)

    finally:
        if sqliteconn:
            sqliteconn.close()


# Test Case 11: Analyze Habits
def test_analyze_your_habits():
    try:
        console = Console()
        print("\n")
        console.print(f'[green]**************************************************[/green]')
        console.print(f'[green]Test Case 11.a: Display All Tracked Habits[/green]')
        console.print(f'[green]**************************************************[/green]')
        time.sleep(3)
        username = "mali1225"

        from Analyze_Your_Habits_Test import display_all_tracked_habits
        display_all_tracked_habits(username)

        # ============================================================================================
        # ============================================================================================

        console = Console()
        print("\n")
        console.print(f'[green]**************************************************[/green]')
        console.print(f'[green]Test Case 11.b: Display All Deleted Habits[/green]')
        console.print(f'[green]**************************************************[/green]')
        time.sleep(3)
        username = "mali1225"

        from Analyze_Your_Habits_Test import display_all_deleted_habits
        display_all_deleted_habits(username)

        # ============================================================================================
        # ============================================================================================

        console = Console()
        print("\n")
        console.print(f'[green]**************************************************[/green]')
        console.print(f'[green]Test Case 11.b: Display All Completed Habits[/green]')
        console.print(f'[green]**************************************************[/green]')
        time.sleep(3)
        username = "mali1225"

        from Analyze_Your_Habits_Test import display_all_completed_habits
        display_all_completed_habits(username)

        # ============================================================================================
        # ============================================================================================

        console = Console()
        print("\n")
        console.print(f'[green]**************************************************[/green]')
        console.print(f'[green]Test Case 11.c: Display All Daily Habits[/green]')
        console.print(f'[green]**************************************************[/green]')
        time.sleep(3)
        username = "mali1225"

        from Analyze_Your_Habits_Test import display_all_daily_habits
        display_all_daily_habits(username)

        # ============================================================================================
        # ============================================================================================

        console = Console()
        print("\n")
        console.print(f'[green]**************************************************[/green]')
        console.print(f'[green]Test Case 11.d: Display All Weekly Habits[/green]')
        console.print(f'[green]**************************************************[/green]')
        time.sleep(3)
        username = "mali1225"

        from Analyze_Your_Habits_Test import display_all_weekly_habits
        display_all_weekly_habits(username)

        # ============================================================================================
        # ============================================================================================

        console = Console()
        print("\n")
        console.print(f'[green]****************************************************[/green]')
        console.print(f'[green]Test Case 11.e: Display Smallest Streak Daily Habits[/green]')
        console.print(f'[green]****************************************************[/green]')
        time.sleep(3)
        username = "mali1225"

        from Analyze_Your_Habits_Test import display_smallest_streak_daily_habits
        display_smallest_streak_daily_habits(username)

        # ============================================================================================
        # ============================================================================================

        console = Console()
        print("\n")
        console.print(f'[green]*****************************************************[/green]')
        console.print(f'[green]Test Case 11.f: Display Smallest Streak Weekly Habits[/green]')
        console.print(f'[green]*****************************************************[/green]')
        time.sleep(3)
        username = "mali1225"

        from Analyze_Your_Habits_Test import display_smallest_streak_weekly_habits
        display_smallest_streak_weekly_habits(username)

        # ============================================================================================
        # ============================================================================================

        console = Console()
        print("\n")
        console.print(f'[green]********************************************************[/green]')
        console.print(f'[green]Test Case 11.g: Display Smallest Streak Among All Habits[/green]')
        console.print(f'[green]********************************************************[/green]')
        time.sleep(3)
        username = "mali1225"

        from Analyze_Your_Habits_Test import display_smallest_streak_among_all_habits
        display_smallest_streak_among_all_habits(username)

        # ============================================================================================
        # ============================================================================================

        console = Console()
        print("\n")
        console.print(f'[green]***************************************************[/green]')
        console.print(f'[green]Test Case 11.h: Display Longest Streak Daily Habits[/green]')
        console.print(f'[green]***************************************************[/green]')
        time.sleep(3)
        username = "mali1225"

        from Analyze_Your_Habits_Test import display_longest_streak_daily_habits
        display_longest_streak_daily_habits(username)

        # ============================================================================================
        # ============================================================================================

        console = Console()
        print("\n")
        console.print(f'[green]****************************************************[/green]')
        console.print(f'[green]Test Case 11.i: Display Longest Streak Weekly Habits[/green]')
        console.print(f'[green]****************************************************[/green]')
        time.sleep(3)
        username = "mali1225"

        from Analyze_Your_Habits_Test import display_longest_streak_weekly_habits
        display_longest_streak_weekly_habits(username)

        # ============================================================================================
        # ============================================================================================

        console = Console()
        print("\n")
        console.print(f'[green]*******************************************************[/green]')
        console.print(f'[green]Test Case 11.j: Display Longest Streak Among All Habits[/green]')
        console.print(f'[green]*******************************************************[/green]')
        time.sleep(3)
        username = "mali1225"

        from Analyze_Your_Habits_Test import display_longest_streak_among_all_habits
        display_longest_streak_among_all_habits(username)

        # ============================================================================================
        # ============================================================================================

        console = Console()
        print("\n")
        console.print(f'[green]*******************************************************[/green]')
        console.print(f'[green]Test Case 11.k: Display Longest Streak Given Habits[/green]')
        console.print(f'[green]*******************************************************[/green]')
        time.sleep(3)
        username = "mali1225"
        habit_id = 10

        from Analyze_Your_Habits_Test import display_longest_streak_given_habit
        display_longest_streak_given_habit(habit_id, username)

        # ============================================================================================
        # ============================================================================================

    except Exception as ex:
        print("\nFailure: ", ex)
        print("\nPlease Wait....\n")
        time.sleep(3)

# Print Habit Tracker
def print_habit_tracker():
    console = Console()

    console.print(f'[green]██╗  ██╗ █████╗ ██████╗ ██╗████████╗    ████████╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗[/green]')
    console.print(f'[green]██║  ██║██╔══██╗██╔══██╗██║╚══██╔══╝    ╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗[/green]')
    console.print(f'[green]███████║███████║██████╔╝██║   ██║          ██║   ██████╔╝███████║██║     █████╔╝ █████╗  ██████╔╝[/green]')
    console.print(f'[green]██╔══██║██╔══██║██╔══██╗██║   ██║          ██║   ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗[/green]')
    console.print(f'[green]██║  ██║██║  ██║██████╔╝██║   ██║          ██║   ██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║[/green]')
    console.print(f'[green]╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝   ╚═╝          ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝[/green]')


# Call All Test Cases - Main

#repeat = True
#while repeat:
    #try:
        #print_habit_tracker()
        #test_table_creations()
        #test_empty_tables()
        #test_create_user()
        #test_user_login()
        #test_load_predefined_habits()
        #test_create_new_habits()
        #test_manage_habits()
        #test_modify_delete_restore_habits()
        #test_auto_overdue_and_complete_habits()
        #test_restore_completed_habits()
        #test_analyze_your_habits()
        #repeat = False


    #except Exception as ex:
        #print("Failure: ", ex)
