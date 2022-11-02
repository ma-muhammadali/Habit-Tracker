# Create User & Habit Tracker Tables
import sqlite3
import time


def usertablecreation():
    """The purpose of this function is to create Users table for storing Habit Tracker users information."""
    sqliteconn = None

    try:
        # Create a SQL connection to our SQLite database
        sqliteconn = sqlite3.connect('../habit_tracker_db.sqlite3')

        print("Connected to Habit Tracker DB Successfully.")
        dbconn = sqliteconn.cursor()

        command = """CREATE TABLE IF NOT EXISTS 'users'(
                    'Id' integer NOT NULL,
                    'FullName' text NOT NULL,
                    'UserName' text NOT NULL,
                    'Password' text  NOT NULL,
                    'Created_Date' integer NOT NULL,
                    PRIMARY KEY("Id" AUTOINCREMENT)
                )"""

        dbconn.execute(command)
        sqliteconn.commit()
        dbconn.close()

        print("\nUser table created successfully.\n")

    except sqlite3.Error as error:
        print("Failed to Create user table", error)

    except Exception as ex:
        print("Failed to Create user table", ex)

    finally:
        if sqliteconn:
            sqliteconn.close()
        time.sleep(3)


def habittablecreation():
    """The purpose of this function is to create Habit Tracker table for storing Habit Tracker list."""

    sqliteconn = None

    try:
        # Create a SQL connection to our SQLite database
        sqliteconn = sqlite3.connect('../habit_tracker_db.sqlite3')

        print("Connected to Habit Tracker DB Successfully.")
        dbconn = sqliteconn.cursor()

        command = """CREATE TABLE IF NOT EXISTS 'habits_tracker'(
                    'HabitId' integer NOT NULL,
                    'HabitName' text NOT NULL,
                    'Description' text NOT NULL,
                    'Period' text NOT NULL,
                    'Born' integer,
                    'Start_Date' integer NOT NULL,
                    'Due_Date' integer,
                    'Streak' integer,
                    'Max_Streak' integer,
                    'Max_Days' integer,
                    'Break' integer,
                    'HabitStatus' integer,
                    'UserName' text NOT NULL,
                    PRIMARY KEY("HabitId" AUTOINCREMENT)
                )"""

        dbconn.execute(command)
        sqliteconn.commit()
        dbconn.close()

        print("\nHabit Tracker table created successfully.\n")

    except sqlite3.Error as error:
        print("Failed to create Habit Tracker table", error)

    except Exception as ex:
        print("Failed to Create Habit Tracker table", ex)

    finally:
        if sqliteconn:
            sqliteconn.close()
        time.sleep(3)

