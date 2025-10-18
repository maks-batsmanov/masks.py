import os

from src.decorators import log


def test_log_1(capsys):  # 1й тест

    @log()
    def add(a, b):
        return a + b

    add(1, 9)
    captured = capsys.readouterr()
    assert captured.out == 'add start\nadd ok 10\n'


def test_log_2():  # 2й тест
    if os.path.exists("error_test.txt"):
        os.remove("error_test.txt")

    @log('error_test.txt')
    def add(a, b):
        return a + b

    add(1, 9)
    with open("error_test.txt", "r", encoding="utf-8") as f:
        content = f.read()
    assert content == 'add start\nadd ok 10\n'


def test_log_errors_1(capsys):
    @log()
    def divide(a, b):
        return a / b
    try:
        divide(4, 0)
        assert False
    except ZeroDivisionError:
        pass
    captured = capsys.readouterr()
    assert captured.out == 'divide start\ndivide error: division by zero. Inputs: (4, 0) {}\n'


def test_error_message_in_file():

    if os.path.exists("test_error.log"):
        os.remove("test_error.log")

    @log("test_error.log")
    def divide(a, b):
        return a / b
    try:
        divide(10, 0)
    except ZeroDivisionError:
        pass

    assert os.path.exists("test_error.log"), "Файл логов не создан"

    with open("test_error.log", "r", encoding="utf-8") as f:
        content = f.read()

    assert content == 'divide start\ndivide error: division by zero. Inputs: (10, 0) {}\n'
