from functools import wraps


def log(filename: str = "") -> callable:
    def decorator(func: callable) -> callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> any:
            """
            Принимает функцию и выводит лог на экран или в файл logs/logfile.txt (Если указан)
            """
            result = None
            try:
                result = func(*args, **kwargs)
            except Exception as ex:
                logs = f"{func.__name__} error: {ex}. Inputs: {args}, {kwargs}"
            else:
                logs = f"{func.__name__} ok"
            finally:
                if filename:
                    with open(filename, "w") as log_file:
                        log_file.write(logs)
                else:
                    print(logs)
            return result

        return wrapper

    return decorator
