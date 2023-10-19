def upper(x):
    upper_s = []
    for c in x:
        if c.upper():
            upper_s.append(c)

    return "".join(upper_s)

s = 'qwertyu iopasd fghjklz xcvbnm'
print(s.title())