# Each step reduces the size of numbers by about a factor of 2
# Takes about log(ab) steps.
# GCDs of 100 digits numbers takes about 600 steps.
# Each step a single division

# Finding the correct algorithm requires 
# knowing something interesting about the problem :D
def euclidean_method(a, b):
    if(b == 0):
        return a
    else:
        a_module = a % b
        return euclidean_method(b, a_module)


def main():
    a, b = collect_data()
    result = euclidean_method(a, b)

    print("FINAL RESULT: ", result)


def collect_data():
    a_value = input("Enter with A value: ")
    b_value = input("Enter with B value: ")

    return int(a_value), int(b_value)

main()