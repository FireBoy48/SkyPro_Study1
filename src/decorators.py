from config import PATH_TO_LOG
from functools import wraps

def log(filename: str = "") -> callable:
    def decorator(func: callable) -> callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> any:
            '''
            Принимает функцию и выводит лог на экран или в файл logs/logfile.txt (Если указан)
            '''
            try:
                result = func(*args, **kwargs)
                logs = f"{func.__name__} ok"
            except TypeError as ex:
                logs = f"{func.__name__} error: {ex}. Inputs: {args}, {kwargs}"
            if filename:
                with open(filename, "w") as log_file:
                    log_file.write(logs)
            else:
                print(logs)
            return result

        return wrapper

    return decorator


@log()
def my_function(x: int, y: int) -> int:
    '''
    Складывает 2 числа
    :param x: число 1
    :param y: число 2
    :return: сумма 2 чисел
    '''
    return x + y
