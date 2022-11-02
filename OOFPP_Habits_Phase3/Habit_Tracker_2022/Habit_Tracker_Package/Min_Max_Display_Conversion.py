class Min_Max_Conversion:
    def __init__(self, HabitName, HabitStatus, StreakValue):
        """The purpose of this function is to convert the values received from table row into string."""
        self.HabitName = str(HabitName).strip()
        self.HabitStatus = str(HabitStatus).strip()
        self.StreakValue = str(StreakValue).strip()

        if self.HabitStatus == '1':  # Active
            self.HabitStatus = '➠ '

        elif self.HabitStatus == '2':  # Completed
            self.HabitStatus = '✅ '

        else:
            self.HabitStatus = '❌ '  # Deleted

    def __repr__(self) -> str:
        return f"({self.HabitName}, {self.HabitStatus}, {self.StreakValue})"
