def efficient_fibonacci_algorithm(n):
    f = [0] * n
    f[1] = 1

    for i in range(2, n):
        f[i] = f[i - 1] + f[i - 2]
    
    return f

def main():
    value = colect_data()
    result = efficient_fibonacci_algorithm(value)
    print(result)


def colect_data():

    value = input("Enter with value: ")
    return int(value)

main()