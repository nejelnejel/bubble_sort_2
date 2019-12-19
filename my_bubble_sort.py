"""
Implementation of Bubble Sort
"""


def bubble_sort(list_of_numbers):
    """
    Function sorting a list of numbers

    :param list_of_numbers: list of numbers
    :return: sorted list of numbers
    """
    for i, _ in enumerate(list_of_numbers):
        for index, _ in enumerate(list_of_numbers[i:-1]):
            if list_of_numbers[index] > list_of_numbers[index + 1]:
                list_of_numbers[index], list_of_numbers[index + 1] = list_of_numbers[index + 1], list_of_numbers[index]
    return list_of_numbers


if __name__ == '__main__':
    my_lst = [79, 2, 54, 32, 7, 3, 1]
    bubble_sort(my_lst)
    print(my_lst)
