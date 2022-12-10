from random import randint


def get_unique_list_numbers() -> list[int]:
    unique_list = []
    while len(unique_list) != 15:
        number = randint(-10, 10)
        if number not in unique_list:
            unique_list.append(number)
    return unique_list


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
# end
