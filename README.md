# Habit-Tracker
Command Line Interface (CLI) Based Habit Tracker Application

# Habit Tracker App
## By Muhammad Ali


## Tools & Libraries

- Created with python 3.10.4
- Database with sqlite3


## Features
[1] User can Create New Habits [Two period to choose : Daily or Weekly]<br>
[2] User can Manage Habits [complete task]\
[3] User can Modify, Delete & Restore Habits\
[4] User can Analyze Habits

## Link(github)


## Installation
Please download and install PyCharm IDE using below link<br>
https://www.jetbrains.com/pycharm/


## For Testing
Please install pytest using below command<br>
pip install pytest

## Tested with pytest in 29th October 2022
[1] Assert list date in this test has been set up with specific test date, 29th October 2022<br>
[2] For different date, need to adjust dates following the assert list
[3] Test folder : Habit_Tracker_Pytest (Habit_Tracker_Testing.py)
[4] From command prompt type: pytest -v .\Habit_Tracker_Testing.py

## Tutorial How to Use Habit Tracker 

In order to start Habit Tracker, just go to terminal and execute main.py file. When program starts

Habit Tracker Login Menu will appear. User will be asked to:
		[1] Create New User
		[2] Login

Once user is login, Habit Tracker Main Menu will appear: 

		[1] Enter 1 to CREATE NEW HABIT.
		[2] Enter 2 to MANAGE HABITS (COMPLETE TASKS).
		[3] Enter 3 to MODIFY, DELETE & RESTORE HABIT.
		[4] Enter 4 to ANALYZE YOUR HABITS.
			Choose Option 1 to 4 or Enter 'q' or 'Q' to quit.
      
User can Create Habits, Checkoff Habit Task, Modify, and Analyse habits.

1. Create New Habit
   For Habit creation, user need to input Habit's Title, Description, Period & Max Days. There are 2 Period options (Daily or Weekly)

2. Manage Habit (Complete Task)
   If user complete task/ checkoff the task before the due date, Streak will be added by 1, as well as Max_Streak.
   Start_Date and Due_date will be renewed.
   
   Streak will be increasing if user checkoff the task within period between Start_Date and Due_Date.
   If user didn't checkoff within period, Streak will be reset to zero, but Max_Streak still remain the same, and Break will be added by 1.
   If Streak > Max_Streak, then Max_Streak will be changed become = Streak.
   
   When Max_Streak == Max_Days, habits will be marked as completed automatically.

3. Modify/Delete/Restore Habits :

		[1] Enter 1 to CHANGE HABIT'S TITLE
		[2] Enter 2 to CHANGE HABIT'S DESCRIPTION
		[3] Enter 3 to CHANGE HABIT'S PERIOD TO DAILY
		[4] Enter 4 to CHANGE HABIT'S PERIOD TO WEEKLY
		[5] Enter 5 to CHANGE HABIT'S MAX DAYS
		[6] Enter 6 to DELETE HABIT
		[7] Enter 7 to RESTORE DELETED HABIT
		[8] Enter 8 to RESTORE COMPLETED HABIT
		[X] Enter X to EXIT

   
   If Period change, then Start_Date will be reset to today, and Due_Date will be today + 1 for Daily, and become today + 7 for Weekly.
   Streak, Max_Streak, and Break will remain the same, and will be added or reset according to new Period.
        
4. Analyze Your Habits :

		[1] Enter 1 to VIEW ALL TRACKED HABITS
		[2] Enter 2 to VIEW ALL DELETED HABITS
		[3] Enter 3 to VIEW ALL COMPLETED HABITS
		[4] Enter 4 to VIEW ALL DAILY HABITS
		[5] Enter 5 to VIEW ALL WEEKLY HABITS
		[6] Enter 6 to VIEW SMALLEST RUN STREAK DAILY HABIT
		[7] Enter 7 to VIEW SMALLEST RUN STREAK WEEKLY HABIT
		[8] Enter 8 to VIEW SMALLEST RUN STREAK AMONG ALL HABITS
		[9] Enter 9 to VIEW LONGEST RUN STREAK DAILY HABIT
		[10] Enter 10 to VIEW LONGEST RUN STREAK WEEKLY HABIT
		[11] Enter 11 to VIEW LONGEST RUN STREAK AMONG ALL HABITS
		[12] Enter 12 to VIEW LONGEST RUN STREAK GIVEN HABIT
		[X] Enter X to EXIT.


  User can analyze history using this menu.
  User need to input a given/chosen habit to display the longest streak (Max_Streak) of the choice.
