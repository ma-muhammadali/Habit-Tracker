"""Habit Tracker"""

import time
import threading
import sys


class HabitsTracker:
    """Habits class"""

    def __init__(self):
        print("\n")

    def displaypredefinedhabits(self, username):
        """Display Predefined Habits"""
        from Habit_Tracker_Package import Predefined_Habits
        Predefined_Habits.loadpredefinedhabits(username)

    def createnewhabit(self, username):
        """"User Create New Habits"""
        from Habit_Tracker_Package import Create_New_Habit
        Create_New_Habit.create_new_habit(username)

    def managehabits(self, username):
        """User Manage Habits (Complete Tasks)"""
        from Habit_Tracker_Package import Manage_Habits
        Manage_Habits.checked_off_habit(username)

    def modifydeletehabits(self, username):
        """Modify, Delete & Restore Habits"""
        from Habit_Tracker_Package import Modify_Delete_Restore_Habits
        Modify_Delete_Restore_Habits.modify_delete_habits(username)

    def analyzehabits(self, username):
        """Analyze Your Habits"""
        from Habit_Tracker_Package import Analyze_Your_Habits
        Analyze_Your_Habits.analyze_your_habits(username)

    def displayalltrackedhabits(self, username):
        """Display All Tracked Habits"""
        from Habit_Tracker_Package import Analyze_Your_Habits
        Analyze_Your_Habits.display_all_tracked_habits(username)


def habit_tracker_main(fullname, username, islogin):
    """The purpose of Habit Tracker Main is to display Welcome message along with User's Full Name & Username.
     After that it call Habit Tracker Main Menu"""
    try:
        while islogin == True:
            from rich.console import Console
            console = Console()
            print("\n" * 1)

            console.print(f'[blue]============================================[/blue]')
            console.print(f'[blue]   WELCOME:  {fullname}  ( {username} )     [/blue]')
            console.print(f'[blue]============================================[/blue]')

            time.sleep(5)
            habit_tracker_menu(username)

    except Exception as ex:
        print("Failure: ", ex)


def background_task(user_name):
    """The purpose of Background Task function is start separate thread to calculate Complete_Max_Days_And_Reset_Overdue_Habits."""
    try:

        from Habit_Tracker_Package import Complete_Max_Days_And_Reset_Overdue_Habits

        while True:
            Complete_Max_Days_And_Reset_Overdue_Habits.complete_max_days_and_reset_overdue_habits(user_name)

    except Exception as ex:
        print("Failre: ", ex)


def habit_tracker_menu(user_name):
    """The purpose of Habit Tracker Menu function is display Habit Tracker Menu and start separate thread for background task: Complete_Max_Days_And_Reset_Overdue_Habits"""
    try:
        th = threading.Thread(target=background_task, args=(user_name,))
        th.daemon = True
        th.start()

        habit_obj = HabitsTracker()

        choice = ''
        # Keep looping until user input 'Q' or 'q' (Quit).
        while choice.lower() != 'q':

            # Load Predefined Habits Of LoggedIn User
            habit_obj.displaypredefinedhabits(user_name)

            print("\n*********************************************")
            print("\tHabit Tracker Main Menu")
            print("*********************************************\n")

            print("\n[1] Enter 1 to CREATE NEW HABIT.")
            print("[2] Enter 2 to MANAGE HABITS (COMPLETE TASKS).")
            print("[3] Enter 3 to MODIFY, DELETE & RESTORE HABIT.")
            print("[4] Enter 4 to ANALYZE YOUR HABITS.")
            print("Choose Option 1 to 4 or Enter 'q' or 'Q' to quit.")

            # Asking user to input his/her choice.
            choice = input("\nPLEASE ENTER YOUR CHOICE :  ")

            # If choice = 1 than call Create new habits.
            if choice == '1':  # Create new habits
                # Call Create New Habit Function To Create New Habit
                habit_obj.createnewhabit(user_name)
                time.sleep(1)  # sleep 1 secs
                print("\nRETURN TO HABIT TRACKER MAIN MENU\n")

            # If choice = 2 than call Manage habits.
            elif choice == '2':  # Manage Habits (Complete Tasks)
                # Call Manage Habits Function To Check Off Tasks
                habit_obj.managehabits(user_name)
                time.sleep(1)  # sleep 1 sec
                print("\nRETURN TO HABIT TRACKER MAIN MENU\n")

            # If choice = 3 than call Modify, Delete & Restore habits.
            elif choice == '3':  # Modify, Delete & Restore Habits
                # Call Manage Habits Function To Check Off Tasks
                habit_obj.modifydeletehabits(user_name)
                time.sleep(1)  # sleep 1 sec
                print("\nRETURN TO HABIT TRACKER MAIN MENU\n")

            # If choice = 4 than call Analyze habits.
            elif choice == '4':  # Analyze Your Habits
                # Call Manage Habits Function To Check Off Tasks
                habit_obj.analyzehabits(user_name)
                time.sleep(1)  # sleep 1 sec
                print("\nRETURN TO HABIT TRACKER MAIN MENU\n")

            # If choice = 'q' than exit Habit Tracker application.
            elif str(choice.lower()) == 'q':
                print("\nHABIT TRACKER IS CLOSING NOW....\n")
                habit_obj = None
                time.sleep(3)  # sleep 1 sec
                sys.exit()

            # If choice is not one of above than display error message.
            else:
                print("\nINCORRECT OPTION. PLEASE ENTER CORRECT OPTION.\n")

    except Exception as ex:
        print("Failure: ", ex)
