
def sql_test():

    #вводим кол-во - cтолбцов,строк и ограничений
    rows_count, cols_count, filter_count = (
        list(map(lambda x: int(x), input('Через пробел введите 3 числа :').strip().split())))

    # создаем списко имен для столбцов далее он пригодится
    cols= input(f'Через пробел введите имена для колонок({cols_count}) штук :').strip().split()

    # вводим строки в список rows
    rows = []
    for i in range(rows_count):
        rows.append(list(map(lambda x: int(x), input(f'Через пробел введите'
         f' {cols_count} значений для строки {i+1} :').strip().split())))

    # вводим ограничие в список filters
    filters = []
    for q in range(filter_count):
        filter = input('Введите ограничение :').split()
        filters.append(filter)

    #Сюда считаем общую сумму всех валидных строк
    result_sum = 0


    for row in rows:
        # статус того что строка прошла проверку фильтрами
        filtered_row = True

        for filter in filters:
            col_name,op,value = filter

            # находим индекс для столбца через имя
            col_index = cols.index(col_name)

            val = row[col_index]

            # здесь сравниваются значения из фильтра и реально значение строки
            # если строка проходит то сумма ее значений заносится в финальный результат
            if op == '>':
                if not (val>int(value)):
                    filtered_row = False
                    break
            elif op == '<':
                if not (val < int(value)):
                    filtered_row = False
                    break

        if filtered_row:
            result_sum += sum(row)

    return result_sum

if __name__ == '__main__':
    print(sql_test())