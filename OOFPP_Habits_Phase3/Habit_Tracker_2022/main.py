import time
import Habit_Tracker_Main
import datetime
from rich.console import Console
import main


def login_menu():
    """The purpose of login menu function is to display Habit Tracker Login Menu and ask input from user. [1]. Create User &
    [2]. Login"""
    print("\n" * 2)
    print_habit_tracker()

    time.sleep(2)
    print("\n" * 2)

    console = Console()

    console.print(f'[red]***************************************[/red]')
    console.print(f'[red]**     Habit Tracker Login Menu     ***[/red]')
    console.print(f'[red]***************************************[/red]')

    choice = input("\n[1] Create New User\n[2] Login\nEnter Your Choice (or Press 'q' or 'Q' to Exit): ")

    if choice == '1':
        create_user()
        login_menu()

    elif choice == '2':
        login()

    elif str(choice.lower()) == 'q':
        print("\nHabit Tracker is Closing Now.........")
        exit(0)

    else:
        print("\nPlease Enter Correct Option.\n")


def create_user():
    """The purpose of create user function is to create new user for Habit Tracker application.
    It takes user Full Name, Desired UserName and Password. Once user is created successfully,
    8 predefined habits has been added to user's habit tracker list"""
    import sqlite3
    sqliteconn = None

    try:

        # Create a SQL connection to our SQLite database
        sqliteconn = sqlite3.connect('../habit_tracker_db.sqlite3')
        # print("Connected to Database Successfully.")
        dbconn = sqliteconn.cursor()

        command = """SELECT * FROM users"""
        dbconn.execute(command)
        records = dbconn.fetchall()
        # print("Total users are:  ")
        lenrecords = len(records)
        # print(lenrecords)

        fullname = ''
        username = ''
        password = ''
        createddate = datetime.datetime.today()

        full_name_repeat = True

        while full_name_repeat:
            fullname = input("\nEnter Your Full Name: ")
            fullname = fullname.strip()

            if fullname == '':
                print("\nFull Name can not be empty")
                full_name_repeat = True

            else:
                full_name_repeat = False

                user_name_repeat = True

                while user_name_repeat:

                    username = input("\nEnter Your Desired User Name: ")
                    username = username.strip()

                    if username == '':
                        print("\nUser Name can not be empty")
                        user_name_repeat = True

                    else:
                        username = username.lower()
                        user_name_repeat = False

                        password_repeat = True

                        while password_repeat:
                            password = input("\nEnter Your Password: ")
                            password = password.strip()

                            if password == '':
                                print("\nPassword can not be empty")
                                password_repeat = True

                            else:
                                password_repeat = False

        ### This piece of code is use to check if username already exist or not.

        dbconn = sqliteconn.cursor()
        command = """SELECT DISTINCT UserName FROM users WHERE username = :usr"""
        dbconn.execute(command, {'usr': username})
        records = dbconn.fetchall()
        lenrecords = len(records)
        # print(lenrecords)
        # print(records)

        if lenrecords != 0:
            print("\nUsername already taken. Please choose different username\n")
            dbconn.close()
            create_user()

        # new_user = [(userid, fullname, username, password, createdDate)]
        new_user = [(fullname, username, password, createddate)]

        dbconn.executemany("INSERT INTO users ('FullName','UserName','Password','Created_Date') VALUES (?,?,?,?)",
                           new_user)
        print("\nUser ", fullname, " (", username, " ) Created Successfully.")
        time.sleep(3)

        sqliteconn.commit()
        sqliteconn.close()

        from Habit_Tracker_Package import Predefined_Habits
        Predefined_Habits.insertpredefinedhabits(username)

    except sqlite3.Error as error:
        print("Failure: ", error)

    except Exception as ex:
        print("Failure: ", ex)

    finally:
        if sqliteconn:
            sqliteconn.close()


full_name = ""
user_name = ""
is_login = False


def login():
    """The purpose of login function is login user into Habit Tracker.
    It takes username and password from user and check whether it exist or not.
    If user exist, it will log in into Habit Tracker and habit tracker list will be displayed.
    If user doesn't exist, then user will get an error message"""

    try:
        import sqlite3

        # Create a SQL connection to our SQLite database
        sqliteconn = sqlite3.connect('../habit_tracker_db.sqlite3')

        # print("Connected to Database Successfully.")
        dbconn = sqliteconn.cursor()

        username_repeat = True

        username = ''
        password = ''

        while username_repeat:
            username = input("\nEnter Your User Name: ")
            username = username.strip()

            if username == '':
                print("\nUser Name can not be empty")
                username_repeat = True

            else:
                username = username.lower()
                username_repeat = False
                password_repeat = True

                command = """SELECT DISTINCT UserName FROM users WHERE username = :usr"""
                dbconn.execute(command, {'usr': username})
                userrecords = dbconn.fetchall()
                lenrecords = len(userrecords)
                # print(lenrecords)
                # print(records)

                if lenrecords != 0:
                    while password_repeat:
                        password = input("\nEnter Your Password: ")
                        password = password.strip()

                        if password == '':
                            print("\nPassword can not be empty")
                            password_repeat = True

                        else:
                            password_repeat = False

                    command = """SELECT * FROM users WHERE username = :usr AND password = :pass"""
                    dbconn.execute(command, {'usr': username, 'pass': password})
                    records = dbconn.fetchall()
                    lenrecords = len(records)

                    if lenrecords != 0:
                        for row in records:
                            main.full_name = str(row[1])
                            main.user_name = str(row[2])
                            main.is_login = True

                    else:
                        print("\nIncorrect Password\n")
                        time.sleep(2)

                else:
                    print("\nUsername doesn't exist\n")

    except sqlite3.Error as e:
        print("Failure: ", e)

    except Exception as ex:
        print("Failure: ", ex)

    finally:
        if sqliteconn:
            sqliteconn.close()

        if is_login:
            Habit_Tracker_Main.habit_tracker_main(full_name, user_name, is_login)


def tablescreation():
    """The purpose of Table Creation function is create User & Habit Tracker table in sqlite3 database."""
    from Habit_Tracker_Package import Tables_Creation
    Tables_Creation.usertablecreation()
    Tables_Creation.habittablecreation()


def empty_habit_tracker_table():
    """The purpose of Empty Habit Tracker Table function is delete all records from Habit Tracker table."""
    from Habit_Tracker_Package import Empty_Tables
    # Empty_Tables.drop_habit_table()
    Empty_Tables.empty_habit_tracker_tables()


def empty_users_table():
    """The purpose of Empty User Table function is delete all records from Users table."""
    from Habit_Tracker_Package import Empty_Tables
    Empty_Tables.empty_users_tables()


def print_habit_tracker():
    """The purpose of Print Habit Tracker is to display below Habit Tracker text"""

    console = Console()
    console.print(
        f'[green]██╗  ██╗ █████╗ ██████╗ ██╗████████╗    ████████╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗[/green]')
    console.print(
        f'[green]██║  ██║██╔══██╗██╔══██╗██║╚══██╔══╝    ╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗[/green]')
    console.print(
        f'[green]███████║███████║██████╔╝██║   ██║          ██║   ██████╔╝███████║██║     █████╔╝ █████╗  ██████╔╝[/green]')
    console.print(
        f'[green]██╔══██║██╔══██║██╔══██╗██║   ██║          ██║   ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗[/green]')
    console.print(
        f'[green]██║  ██║██║  ██║██████╔╝██║   ██║          ██║   ██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║[/green]')
    console.print(
        f'[green]╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝   ╚═╝          ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝[/green]')


while not main.is_login:
    login_menu()
