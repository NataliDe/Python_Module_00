def nata(a):
    i = 1
    if i < a:
        nata(a - 1)
    print("Day", a)


def ft_count_harvest_recursive():
    a = int(input("Days until harvest: "))
    nata(a)
