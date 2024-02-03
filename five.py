def get_sum_simmilars():
    arrays_count = int(input('Введите сколько массивов будет :'))

    arrays = []
    result_sum = 0

    for i in range(arrays_count):
        current_len_array = int(input('Введите длинну массива :'))
        array = []
        while current_len_array != len(array):
            array = list(map(int,input(f'Через пробел введите числа : ').split()))
            arrays.append(array)

    # Курсор поставил чтобы он не проверял уже до этого проверенные массивы
    cursor = 0

    #Циклами сравниваются значения из 2ух массивов
    for array in arrays:
        for sub_array in arrays[cursor:]:
            i= 0

            if sub_array == array:
                continue

            while i < len(array) and i < len(sub_array) and array[i]== sub_array[i]:
                i+=1
                result_sum+=1

        cursor += 1

    return result_sum

if __name__ == '__main__':
    print(get_sum_simmilars())

