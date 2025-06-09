
def get_fancy_numbers():
    fancy_numbers = []
    for a in range(1,10):
        for b in range(0,10):
            c = abs(a - b)
            d = a + c
            if d <= 9 and (a + b + c + d == 12):
               fancy_numbers.append(f"{a}{b}{c}{d}")
    return fancy_numbers
print(get_fancy_numbers())
