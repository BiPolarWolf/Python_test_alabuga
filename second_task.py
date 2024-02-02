def kki():
    a_count, b_count ,q_count = list(map(lambda x: int(x),input('Через пробел введите 3 числа :').split(' ')))
    q_list = a_cards = b_cards = []

    while len(a_cards) != a_count:
        a_cards =  list(map(lambda x: int(x),input(f'Через пробел введите {a_count} чисел для игрока А :').split(' ')))

    while len(b_cards) != b_count:
        b_cards =  list(map(lambda x: int(x),input(f'Через пробел введите {b_count} чисел для игрока B :').split(' ')))

    def update_q_count(a:list,b:list):
        count = 0
        a_b_list = a+b
        for i in a_b_list :
            if a_b_list.count(i) == 1:
                count+=1
        q_list.append(count)


    for i in range(q_count):
        typek,playerk,cardk = input(f'Введите изменение № {i+1} :').split(' ')

        if typek == '-1':
            if playerk=='A':
                a_cards.remove(int(cardk))
            elif playerk == 'B':
                b_cards.remove(int(cardk))

        elif typek == '1':
            if playerk == 'A':
                a_cards.append(int(cardk))
            elif playerk == 'B':
                b_cards.append(int(cardk))


        update_q_count(a_cards,b_cards)
        print(q_list)
    print('A',a_cards)
    print('B',b_cards)
    print(q_list)


if __name__ == '__main__':
    kki()