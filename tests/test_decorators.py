from pathlib import Path

from config import ROOT_DIR
from src.decorators import log

TEST_PATH_TO_LOG = Path(ROOT_DIR, "logs", "test_log.txt")


def test_log_print(capsys):
    @log()
    def new_function(x, y):
        return x - y

    new_function(3, 1)
    right = capsys.readouterr()
    assert right.out == "new_function ok\n"

    new_function(2)
    wrong = capsys.readouterr()
    assert (
        wrong.out
        == "new_function error: test_log_print.<locals>.new_function() missing 1 required positional argument: 'y'. Inputs: (2,), {}\n"
    )


def test_log_file(capsys):
    @log(TEST_PATH_TO_LOG)
    def new_function(x, y):
        return x - y

    new_function(3, 1)
    with open(TEST_PATH_TO_LOG, "r") as logs:
        assert logs.read() == "new_function ok"

    new_function(2)
    with open(TEST_PATH_TO_LOG, "r") as logs:
        assert (
            logs.read()
            == "new_function error: test_log_file.<locals>.new_function() missing 1 required positional argument: 'y'. Inputs: (2,), {}"
        )
    TEST_PATH_TO_LOG.unlink()
