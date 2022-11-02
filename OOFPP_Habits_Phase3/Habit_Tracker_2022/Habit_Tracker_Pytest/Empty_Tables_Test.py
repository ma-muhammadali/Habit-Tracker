import sqlite3
import time


def empty_habit_tracker_tables():
    """The purpose of this function is to delete all records from Habit Tracker table for fresh start of
    Habit Tracker Application. It also reset the SQLITE_SEQUENCE to Zero for Habit Tracker table"""

    sqliteconn = None

    try:
        # Create a SQL connection to our SQLite database
        sqliteconn = sqlite3.connect('../habit_tracker_db.sqlite3')

        # print("Connected to Database Successfully.")
        dbconn = sqliteconn.cursor()

        # Delete All Records From Habit Tracker Table
        command = """DELETE FROM habits_tracker"""
        dbconn.execute(command)
        records = dbconn.fetchall()
        lenrecords = len(records)
        print("\nTotal Habits are: ", lenrecords, "\n")
        sqliteconn.commit()

        # Reset SQLITE_SEQUENCE To Zero For Habit Tracker Table
        command = """UPDATE SQLITE_SEQUENCE SET SEQ = 0 WHERE NAME = 'habits_tracker'"""
        dbconn.execute(command)
        sqliteconn.commit()
        dbconn.close()
        time.sleep(2)

    except sqlite3.Error as e:
        print("Failure: ", e)

    except Exception as ex:
        print("Failure: ", ex)

    finally:
        if sqliteconn:
            sqliteconn.close()


def empty_users_tables():
    """The purpose of this function is to delete all records from User table for fresh start of
    Habit Tracker Application. It also reset the SQLITE_SEQUENCE to Zero for User table"""
    sqliteconn = None

    try:
        # Create a SQL connection to our SQLite database
        sqliteconn = sqlite3.connect('../habit_tracker_db.sqlite3')

        # print("Connected to Database Successfully.")
        dbconn = sqliteconn.cursor()

        # Delete All Records From Users Table
        command = """DELETE FROM users"""
        dbconn.execute(command)
        records = dbconn.fetchall()
        lenrecords = len(records)
        print("\nTotal Users are: ", lenrecords, "\n")
        sqliteconn.commit()

        # Reset SQLITE_SEQUENCE To Zero For Users Table
        command = """UPDATE SQLITE_SEQUENCE SET SEQ = 0 WHERE NAME = 'users'"""
        dbconn.execute(command)
        sqliteconn.commit()
        dbconn.close()
        time.sleep(2)

    except sqlite3.Error as e:
        print("Failure: ", e)

    except Exception as ex:
        print("Failure: ", ex)

    finally:
        if sqliteconn:
            sqliteconn.close()


def empty_habit_tracker_tables():
    """The purpose of this function is to delete all records from Habit Tracker table for fresh start of
    Habit Tracker Application. It also reset the SQLITE_SEQUENCE to Zero for Habit Tracker table"""

    sqliteconn = None

    try:
        # Create a SQL connection to our SQLite database
        sqliteconn = sqlite3.connect('../habit_tracker_db.sqlite3')

        # print("Connected to Database Successfully.")
        dbconn = sqliteconn.cursor()

        # Delete All Records From Habit Tracker Table
        command = """DELETE FROM habits_tracker"""
        dbconn.execute(command)
        records = dbconn.fetchall()
        lenrecords = len(records)
        print("\nTotal Habits are: ", lenrecords, "\n")
        sqliteconn.commit()

        # Reset SQLITE_SEQUENCE To Zero For Habit Tracker Table
        command = """UPDATE SQLITE_SEQUENCE SET SEQ = 0 WHERE NAME = 'habits_tracker'"""
        dbconn.execute(command)
        sqliteconn.commit()
        dbconn.close()
        time.sleep(2)

    except sqlite3.Error as e:
        print("Failure: ", e)

    except Exception as ex:
        print("Failure: ", ex)

    finally:
        if sqliteconn:
            sqliteconn.close()


def drop_habit_table():
    """The purpose of this function is to delete all records from User table for fresh start of
    Habit Tracker Application. It also reset the SQLITE_SEQUENCE to Zero for User table"""
    sqliteconn = None

    try:
        # Create a SQL connection to our SQLite database
        sqliteconn = sqlite3.connect('../habit_tracker_db.sqlite3')

        # print("Connected to Database Successfully.")
        dbconn = sqliteconn.cursor()

        # Delete All Records From Users Table
        command = """DROP Table IF EXISTS habits_tracker"""
        dbconn.execute(command)
        print("\nHabit Tracker table dropped successfully.\n")
        sqliteconn.commit()
        dbconn.close()
        time.sleep(2)

    except sqlite3.Error as e:
        print("Failure: ", e)

    except Exception as ex:
        print("Failure: ", ex)

    finally:
        if sqliteconn:
            sqliteconn.close()
