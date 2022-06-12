# Решение задачи №2. Дан массив целых чисел. Нужно удалить из него нули.
# Можно использовать только О(1) дополнительной памяти

def remove_zero(array_1: list) -> list:
    """Функция принимает ссылку на список и удаляет из него все нули"""
    index = 0
    array_len = len(array_1)
    while index != array_len:
        if array_1[index] == 0:
            del array_1[index]
            array_len -= 1
            continue
        index += 1
    return array_1


if __name__ == "__main__":
    input_array_1 = [0, 1, 0, 0, 4, 5, 6, 7, 0, 8, -4, 0]  # input
    # Не используется дополнительной памяти
    print(f"Ответ: {remove_zero(input_array_1)}")
