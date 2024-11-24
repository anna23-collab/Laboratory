numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

sum-num = sum(num for num in numbers if num is not None)
len-num = len(numbers)
srednee_arifmetic = sum-num / len-num

numbers = [srednee_arifmetic if num is None else num for num in numbers]

print("Измененный список:", numbers)

