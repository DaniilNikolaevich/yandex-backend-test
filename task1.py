# Решение задачи №1. Вернуть элементы, которые есть в первом списке, но нет во втором

def get_diff(array_1: list, array_2: list) -> list:
    set_1 = set(array_1)  # O(len(array_1))
    set_2 = set(array_2)  # O(len(array_2))
    return list(set_1 - set_2)  # O(len(len(set_1)+len(set_2)))


if __name__ == "__main__":
    input_array_1 = [0, 1, 0, 0, 4, 5, 6, 7, 0, 8, -4, 0]  # input
    input_array_2 = [0, 1, 9, 100, -4]  # input
    # В совокупности сложность O(len(set_1)+len(set_2)) = O(N)
    print(f"Ответ: {get_diff(input_array_1, input_array_2)}")
