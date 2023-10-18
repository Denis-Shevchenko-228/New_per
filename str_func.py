def upper(x):
    """Функция преобразования строки в верхний регистр"""
    upper_s = []
    for c in x:
        if c.upper():
            upper_s.append(c)

    return "".join(upper_s)

def upper_sring(string):
    """Функция преобразования первой буквы в верхний регистр"""
    return string.title()