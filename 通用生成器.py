def repeater(value):
    while True:
        new = (yield value)
        if new is not None:
            value = new


r = repeater(42)
next(r)
next(r)
r.send('chengyu')
