import pytest
from project import ask_hours, is_a_filename, load_timetable, save_timetable, TimeTable



def test_ask_hours(monkeypatch):
    answers = iter(['10', '12'])
    monkeypatch.setattr('builtins.input', lambda _: next(answers))
    assert ask_hours() == (10, 12)

    answers = iter(['aa','10', 'a', '12', '14']) # each non-digit restart the loop start+end
    monkeypatch.setattr('builtins.input', lambda _: next(answers))
    assert ask_hours() == (12, 14)


def test_is_a_filename():
    assert is_a_filename("timetable.csv") == True
    assert is_a_filename("timetable") == False
    assert is_a_filename("timetable.svc") == False


def test_save_timetable(tmp_path):
    t1 = TimeTable()
    t1.add_lesson("Test", "Monday", 8, 9)
    file = tmp_path / "t1.csv"
    save_timetable(t1, str(file))
    assert file.read_text().strip() == "Monday,8,Test"
    with pytest.raises(ValueError):
        save_timetable(t1, str(tmp_path / "notafilename"))


def test_load_timetable(tmp_path):
    t1 = TimeTable()
    t1.add_lesson('Maths', 'Monday', 8, 10)
    file = str(tmp_path / "t1.csv")
    save_timetable(t1, file)
    t2 = load_timetable(file)
    assert t1.lessons == t2.lessons
    with pytest.raises(FileNotFoundError):
        load_timetable(str(tmp_path / "notafile.csv"))




def test_timetable_add_lesson():
    t1 = TimeTable()
    t1.add_lesson("Maths", "Monday", 8, 10)
    assert t1.lessons["Monday"] == {8: "Maths", 9: "Maths"}
    with pytest.raises(ValueError):
        t1.add_lesson("Sport", "Monday", 9, 12)


def test_timetable_remove_lesson():
    t1 = TimeTable()
    t1.add_lesson("Maths", "Monday", 8, 10)
    t1.remove_lesson("Monday", 8, 9)
    assert t1.lessons["Monday"] == {9: "Maths"}


def test_timetable_validate():
    t1 = TimeTable()
    assert t1.validate("Monday", 8, 12) == True
    with pytest.raises(ValueError):
        t1.validate("X", 9, 12)
    with pytest.raises(ValueError):
        t1.validate("Monday", 12, 9)
    with pytest.raises(ValueError):
        t1.validate("Monday", 7, 12)
    with pytest.raises(ValueError):
        t1.validate("Monday", 9, 20)
    t1.add_lesson("XX", "Monday", 8, 12)
    with pytest.raises(ValueError):
        t1.validate("Monday", 8, 9)

