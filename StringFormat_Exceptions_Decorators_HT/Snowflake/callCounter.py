calls = {}
def callCounter(func):
    def inner(*args, **kwargs):
        if func.__name__ in calls:
            calls[func.__name__] += 1
        else:
            calls[func.__name__] = 1
        return func(*args, **kwargs)

    return inner


