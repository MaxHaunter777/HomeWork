def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        if result == 2:
            return "Простое"
        elif result > 1:
            if result % 2 == 0:
                return "Составное"
            for n in range(3, int(result**0.5) + 1):
                if result % n == 0:
                    return "Составное"
                else:
                    return "Простое"
        else:
            return print("Число не простое и не состовное")
    return wrapper


@is_prime
def sum_three(*args):
    result = sum(args)
    print(result)
    return result


result = sum_three(2, 3, 4)
print(result)
