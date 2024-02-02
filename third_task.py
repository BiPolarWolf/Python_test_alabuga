def sql_test():
    rows_count, cols_count, filter_count = (
        list(map(lambda x: int(x), input('Через пробел введите 3 числа :').strip().split())))

    cols= input(f'Через пробел введите имена для колонок({cols_count}) штук :').strip().split()

    rows = []
    for i in range(rows_count):
        rows.append(list(map(lambda x: int(x), input(f'Через пробел введите'
         f' {cols_count} значений для строки {i+1} :').strip().split())))

    filters = []
    for q in range(filter_count):
        filter = input('Введите ограничение :').split()
        filters.append(filter)

    result_sum = 0

    for row in rows:
        filtered_row = True

        for filter in filters:
            col_name,op,value = filter
            col_index = cols.index(col_name)
            val = row[col_index]

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