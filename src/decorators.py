
def log(filename=None):
    def wrapper(func):
        def inner(*args, **kwargs):
            result = None
            try:
                if filename is None:
                    print(f"{func.__name__} start")
                    result = func(*args, **kwargs)

                else:
                    message1 = f"{func.__name__} start"
                    with open(filename, 'a', encoding='utf-8') as f:
                        f.write(message1 + '\n')
                    result = func(*args, **kwargs)

            except Exception as e:
                if filename is None:
                    print(f"{func.__name__} error: {e}. Inputs: {args} {kwargs}")
                else:
                    message2 = f"{func.__name__} error: {e}. Inputs: {args} {kwargs}"
                    with open(filename, 'a', encoding='utf-8') as f:
                        f.write(message2 + '\n')
                raise

            else:
                if filename is None:
                    print(f"{func.__name__} ok {result}")
                else:
                    message3 = f"{func.__name__} ok {result}"
                    with open(filename, 'a', encoding='utf-8') as f:
                        f.write(message3 + '\n')
            return result
        return inner
    return wrapper
