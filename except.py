try:
    answer = 10/0
    number = int(input(f"Enter a number:"))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError as err:
    print(err)