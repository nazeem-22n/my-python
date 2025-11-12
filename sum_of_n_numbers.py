#sum_of_n_numbers
def sum_of_n_numbers():
    n = int(input("enter number "))
    total = 0
    for i in range(n):
        number = float(input("Enter a number: "))
        total = total + number
    return total
result = sum_of_n_numbers()
