# import habit_tracker_menu
import time
import datetime
import sqlite3
from rich.console import Console

def login_menu():
    print("\n" * 2)
    print_habit_tracker()

    time.sleep(2)
    print("\n" * 2)

    console = Console()

    console.print(f'[red]***************************************[/red]')
    console.print(f'[red]**     Habit Tracker Login Menu     ***[/red]')
    console.print(f'[red]***************************************[/red]')

    choice = input("\n1. Create New User\n2. Login\nEnter Your Choice (or Press 'q' or 'Q' to Exit): ")

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


def create_user(fullname, username, password):
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

        createddate = datetime.datetime.today()

        full_name_repeat = True

        while full_name_repeat:
            # fullname = input("\nEnter Your Full Name: ")
            fullname = fullname.strip()

            if fullname == '':
                print("\nFull Name can not be empty")
                full_name_repeat = True

            else:
                full_name_repeat = False

                user_name_repeat = True

                while user_name_repeat:

                    # username = input("\nEnter Your Desired User Name: ")
                    username = username.strip()

                    if username == '':
                        print("\nUser Name can not be empty")
                        user_name_repeat = True

                    else:
                        username = username.lower()
                        user_name_repeat = False

                        password_repeat = True

                        while password_repeat:
                            # password = input("\nEnter Your Password: ")
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
            # create_user()

        # new_user = [(userid, fullname, username, password, createdDate)]
        new_user = [(fullname, username, password, createddate)]

        dbconn.executemany("INSERT INTO users ('FullName','UserName','Password','Created_Date') VALUES (?,?,?,?)",
                           new_user)
        print("\nUser ", fullname, " (", username, " ) Created Successfully.")
        time.sleep(3)

        sqliteconn.commit()
        sqliteconn.close()

        from Predefined_Habits_Test import insertpredefinedhabits
        insertpredefinedhabits(username)

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


def login(username, password):
    try:
        # Create a SQL connection to our SQLite database
        sqliteconn = sqlite3.connect('../habit_tracker_db.sqlite3')

        # print("Connected to Database Successfully.")
        dbconn = sqliteconn.cursor()

        username_repeat = True

        while username_repeat:
            # username = input("\nEnter Your User Name: ")
            username = username.strip()

            if username == '':
                print("\nUser Name can not be empty")
                username_repeat = True

            else:
                username = username.lower()
                username_repeat = False
                password_repeat = True

                while password_repeat:
                    # password = input("\nEnter Your Password: ")
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
                full_name = str(row[1])
                user_name = str(row[2])
                # is_login = True

            print("Name: ", full_name, " ( ", user_name, " ) Login Successfully.")

        else:
            print("\nIncorrect Username & Password\n")
            time.sleep(2)

    except sqlite3.Error as e:
        print("Failure: ", e)

    except Exception as ex:
        print("Failure: ", ex)

    finally:
        if sqliteconn:
            sqliteconn.close()


def tablescreation():
    from Habit_Tracker_Package import Tables_Creation
    Tables_Creation.usertablecreation()
    Tables_Creation.habittablecreation()


def empty_habit_tracker_table():
    from Empty_Tables_Test import empty_habit_tracker_tables
    empty_habit_tracker_tables()


def empty_users_table():
    from Empty_Tables_Test import empty_users_tables
    empty_users_tables()


def print_habit_tracker():
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

# while not main.is_login:
# print_habit_tracker()
# print_habit_tracker2()
# login_menu()
# predefined()
# empty_users_table()
# empty_habit_tracker_table()
# tablescreation()
# main.is_login = True
