import os
import time
from rich.progress import Progress


def clear_screen():
    """The purpose of this function is to clear output screen (terminal screen)."""
    # os.system("cls")
    print("\n" * 1)
    time.sleep(1)


# Display Progress Bar when habit tracker loads
with Progress() as progress:
    try:
        clear_screen()
        task1 = progress.add_task("[green]Please Wait! Habit Tracker Is Loading...", total=1000)

        while not progress.finished:
            progress.update(task1, advance=3.5)
            time.sleep(0.02)

    except Exception as ex:
        print("Failure: ", ex)
