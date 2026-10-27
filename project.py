from tabulate import tabulate
import csv

class TimeTable:
    DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    START = 8
    END = 17

    def __init__(self):
        self.lessons = {day: {} for day in self.DAYS}

    def __str__(self):
        rows = []
        for h in range(self.START, self.END):
            row = [h]
            for day in self.DAYS:
                if h in self.lessons[day]:
                    row.append(self.lessons[day][h])
                else:
                    row.append("")
            rows.append(row)
        return tabulate(rows, headers=["Hours"] + self.DAYS, tablefmt="grid")



    def add_lesson(self, subject:str , day:str, start_hour:int, end_hour:int):
        if self.validate(day, start_hour, end_hour):
            for h in range(start_hour, end_hour):
                self.lessons[day][h] = subject

    def remove_lesson(self, day:str, start_hour:int, end_hour:int):
        if day not in self.DAYS:
            raise ValueError("Invalid day")
        elif start_hour<self.START or end_hour>self.END or start_hour >= end_hour:
            raise ValueError("Invalid hour(s)")
        else:
            for h in range(start_hour, end_hour):
                if h in self.lessons[day]:
                    del self.lessons[day][h]


    def validate(self, day:str, start_hour:int, end_hour:int):
        if day not in self.DAYS:
            raise ValueError("Invalid day")
        if start_hour<self.START or end_hour>self.END or start_hour >= end_hour:
            raise ValueError("Invalid hour(s)")
        for h in range(start_hour, end_hour):
            if h in self.lessons[day]:
                raise ValueError("A lesson has already been planned for this time")
        return True



def save_timetable(timetable, filename="timetable.csv"):
    if not is_a_filename(filename):
        raise ValueError("Invalid filename")
    else:
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            for day, hours in timetable.lessons.items():
                for hour, subject in hours.items():
                    writer.writerow([day, hour, subject])


def load_timetable(filename="timetable.csv"):
    new_timetable = TimeTable()
    with open(filename, "r", newline="") as file:
        reader = csv.reader(file)
        for line in reader:
            day, hour, subject = line
            new_timetable.add_lesson(subject , day, int(hour), int(hour)+1)
    return new_timetable


def is_a_filename(s:str):
    return s.endswith(".csv")

def ask_hours():
    while True:
        try:
            start = int(input("Start at : "))
            end = int(input("End at : "))
            break
        except ValueError:
            print("Invalid hour")
    return start, end


def main():
    timetable = TimeTable()
    while True :
        print("\n1: Create a timetable")
        print("2: Load a timetable")
        print("3: Save a timetable")
        print("4: Add a lesson")
        print("5: Remove a lesson")
        print("6: Print timetable")
        print("10: Quit\n")

        try:
            choice = int(input("Choice number: "))
        except ValueError:
            print("Invalid choice")
            continue

        if choice == 1:
            timetable = TimeTable()

        elif choice == 2:
            filename = input("Filename: ")
            try:
                timetable = load_timetable(filename)
            except FileNotFoundError:
                print("Invalid filename")
            except ValueError:
                print("Invalid file content")

        elif choice == 3:
            filename = input("Filename: ")
            try:
                save_timetable(timetable, filename)
            except ValueError as e:
                print(e)

        elif choice == 4:
            s = input("Subject: ")
            d = input("Day: ").strip().capitalize()
            start, end = ask_hours()
            try:
                timetable.add_lesson(s, d, start, end)
            except ValueError as e:
                print(e)

        elif choice == 5:
            d = input("Day: ").strip().capitalize()
            start, end = ask_hours()
            try:
                timetable.remove_lesson(d, start, end)
            except ValueError as e:
                print(e)

        elif choice == 6:
            print(timetable)


        elif choice == 10:
            break

        else:
            print("Invalid choice")



if __name__ == "__main__":
    main()

