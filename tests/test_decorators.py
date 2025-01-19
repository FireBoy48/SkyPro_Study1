import pytest

from src.decorators import my_function

with pytest.raises(Exception):
    assert my_function(2) == "my_function error: my_function() missing 1 required positional argument: 'y'. Inputs: (2,), {}"


assert my_function(1, 2) == 3
