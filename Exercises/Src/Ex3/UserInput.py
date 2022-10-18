all_numbers = []
total_sum = 0

while True:
    print(f"Total sum: {total_sum}")
    user_in = input("Enter a number: ")

    if user_in == "quit":
        break

    number = int(user_in)
    total_sum += number
    all_numbers.append(number)

all_numbers.sort()
print(f"numbers: {all_numbers}")
