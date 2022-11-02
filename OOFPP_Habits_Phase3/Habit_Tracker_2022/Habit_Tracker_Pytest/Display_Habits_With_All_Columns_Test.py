class Display_All_Habits_Columns:
    def __init__(self, HabitId, HabitName, Description, Period, Born, Start_Date, Due_Date, Streak, Max_Streak, Max_Days, Break, HabitStatus):
        self.HabitId = str(HabitId).strip()
        self.HabitName = str(HabitName).strip()
        self.Description = str(Description).strip()
        self.Period = str(Period).strip()
        self.Born = str(Born).strip()
        self.Start_Date = str(Start_Date).strip()
        self.Due_Date = str(Due_Date).strip()
        self.Streak = str(Streak).strip()
        self.Max_Streak = str(Max_Streak).strip()
        self.Max_Days = str(Max_Days).strip()
        self.Break = str(Break).strip()
        self.HabitStatus = str(HabitStatus).strip()

        if self.HabitStatus == '1':  # Active
            self.HabitStatus = '➠ '

        elif self.HabitStatus == '2':  # Completed
            self.HabitStatus = '✅ '

        else:
            self.HabitStatus = '❌ '  # Deleted

    def __repr__(self) -> str:
        return f"({self.HabitId}, {self.HabitName}, {self.Description}, {self.Period}, {self.Born}, {self.Start_Date}, {self.Due_Date}, {self.Streak}, {self.Max_Streak}, {self.Max_Days}, {self.Break}, {self.HabitStatus}) "
