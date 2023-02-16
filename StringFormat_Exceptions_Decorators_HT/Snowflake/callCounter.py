calls = {}
def callCounter(func):
    def inner(*args, **kwargs):
        key = str(func)[len('<function '):-len(' at 0x000001D9FD6CEE60>')]
        if key in calls:
            calls[key] += 1
        else:
            calls[key] = 1
        return func(*args, **kwargs)
    return inner


