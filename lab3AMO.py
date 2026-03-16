import random


# -------------------------------
# 1. ЛІНІЙНИЙ ПОШУК:
# перше і останнє входження
# -------------------------------
def find_first_occurrence(array, x):
    for i in range(len(array)):
        if array[i] == x:
            return i
    return -1


def find_last_occurrence(array, x):
    for i in range(len(array) - 1, -1, -1):
        if array[i] == x:
            return i
    return -1


# -------------------------------
# 2. ЛІНІЙНИЙ ПОШУК:
# кількість елементів, які
# співпадають з першим елементом
# -------------------------------
def count_equal_to_first(array):
    first = array[0]
    count = 0
    for i in range(len(array)):
        if array[i] == first:
            count += 1
    return count


# -------------------------------
# 3. ШВИДКЕ СОРТУВАННЯ
# -------------------------------
def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[len(array) // 2]
    left = []
    middle = []
    right = []

    for num in array:
        if num < pivot:
            left.append(num)
        elif num > pivot:
            right.append(num)
        else:
            middle.append(num)

    return quick_sort(left) + middle + quick_sort(right)


# -------------------------------
# 4. БІНАРНИЙ ПОШУК
# -------------------------------
def binary_search(array, x):
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2

        if array[mid] == x:
            return mid
        elif array[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# -------------------------------
# ОСНОВНА ПРОГРАМА
# -------------------------------

# Завдання 1
print("ЗАВДАННЯ 1")
array1 = [random.randint(1, 50) for _ in range(100)]
print("Згенерований масив із 100 елементів:")
print(array1)

x1 = int(input("Введіть шуканий елемент: "))

first_index = find_first_occurrence(array1, x1)
last_index = find_last_occurrence(array1, x1)

if first_index != -1:
    print("Перше входження елемента", x1, "знаходиться за індексом:", first_index)
    print("Останнє входження елемента", x1, "знаходиться за індексом:", last_index)
else:
    print("Елемент", x1, "у масиві не знайдено.")

print("\n" + "-" * 50 + "\n")

print("ЗАВДАННЯ 2")
array2 = [5, 8, 3, 5, 2, 9, 5, 1, 7, 4, 5, 6, 8, 2, 5, 0, 3, 5, 9, 5]
print("Масив із 20 елементів:")
print(array2)

count = count_equal_to_first(array2)
print("Перший елемент масиву:", array2[0])
print("Кількість елементів, які співпадають з першим:", count)

print("\n" + "-" * 50 + "\n")

print("ЗАВДАННЯ 3")
array3 = [random.randint(1, 100) for _ in range(100)]
print("Початковий масив:")
print(array3)

sorted_array3 = quick_sort(array3)
print("Відсортований масив:")
print(sorted_array3)

x3 = int(input("Введіть елемент для бінарного пошуку: "))

index = binary_search(sorted_array3, x3)

if index != -1:
    print("Елемент", x3, "знайдено у відсортованому масиві за індексом:", index)
else:
    print("Елемент", x3, "не знайдено у відсортованому масиві.")