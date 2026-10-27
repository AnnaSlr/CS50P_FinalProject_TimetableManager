# Timetable Manager

#### Video Demo: [Youtube link](https://youtu.be/4DpB-jEmkqc)

## Description

Timetable manager is a command-line application that lets you build a weekly timetable, from Monday to Friday, 8 to 17.
It can display it in the terminal as a grid, save it and load it from a CSV file.


### Features

- Create an empty timetable
- Save to a CSV file
- Load from a CSV file
- Print the timetable
- Add a lesson
- Remove a lesson

### Project architecture

- `project.py`
    - class `TimeTable`: `__init__`, `__str__`, `add_lesson`, `remove_lesson`, `validate`
    - functions: `save_timetable`, `ask_hours`, `is_a_filename`, `load_timetable`
    - `main`: runs an interactive menu
- `test_project.py`: a pytest function for each project.py function
- `requirements.txt`
- `timetable_test.csv`: example file

### Project deep description

- `project.py`
    - class `TimeTable`:
        - constants:
            - DAYS:  list of str, Monday to Friday
            - START: int, start hour of the day
            - END:   int, end hour of the day
        - `__init__(self)`: initialize self.lessons to {"Monday": {}, "Tuesday":{}, ...}
        - `__str__(self)`: returns timetable as a grid
        - `add_lesson(self, subject:str , day:str, start_hour:int, end_hour:int)`: first calls validate to check if the lesson can be added, then, for each hour between start_hour and end_hour, self.lessons[day] is updated.
        - `remove_lesson(self, day:str, start_hour:int, end_hour:int)`: first it verifies if the input data are allowed (or raises a ValueError) then for each hour between start_hour and end_hour, it updates self.lessons by deleting self.lessons[day][hour]
        - `validate(self, day:str, start_hour:int, end_hour:int)`: this function called by add_lesson returns True or raises an Error. It validates that day, start_hour and end_hour are allowed in the timetable (end_hour cannot be greater than END,  end_hour must be greater than start_hour, ...) but also, it checks any overlapping in the timetable.
    - `save_timetable(timetable, filename="timetable.csv")`: saves the timetable in a CSV file
    - `load_timetable(filename="timetable.csv")`: from a CSV file, creates a new timetable
    - `is_a_filename(s:str)`: checks if the filename ends with '.csv' and returns a boolean.
    - `ask_hours()`: a 'while True' loop to return two integers.
    - `main()`: runs an interactive menu with choice to access all needed functionality to manage your timetable.



### Design choices

**timetable structure:** The object `TimeTable` has an attribute `self.lessons` which is a dictionary of dictionaries `{day: {hour: subject}}`. At initialization `self.lessons == {"Monday": {}, "Tuesday": {}, ...}`. By using days/hours as keys, it makes overlap detection easier as well as the printing. A lesson from 8 to 10 is stored in the dictionary with keys 8 and 9 but not 10. The end hour is excluded.

**`save_timetable` and `load_timetable` use CSV file:** It is simpler to write and read one line per day/hour (Monday,8,Maths) and build a new timetable (when load_timetable) with the function add_lesson.

**`__str__` uses tabulate:** The function loops over the hours then days to build the grid top to bottom. Each row is one hour. The library format the grid.

**Error management:** Errors are raised through the different functions (useful to test it with pytest), and all of them are caught in the main function.




### How to use it

```
pip install -r requirements.txt
python project.py
```
Then choose an option from the menu. The menu can be quit with the option: 10.

For tests:
```
pytest test_project.py
```

