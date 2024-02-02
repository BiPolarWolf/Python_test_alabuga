def kki():
    a_count, b_count ,q_count = list(map(lambda x: int(x),
    input('Через пробел введите 3 числа :').strip().split()))
    q_list = a_cards = b_cards = []

    while len(a_cards) != a_count:
        a_cards =  list(map(lambda x: int(x),
        input(f'Через пробел введите {a_count} чисел для игрока А :').strip().split()))

    while len(b_cards) != b_count:
        b_cards =  list(map(lambda x: int(x),
        input(f'Через пробел введите {b_count} чисел для игрока B :').strip().split()))

    def update_q_count():
        count = 0
        a_fake = a_cards.copy()
        b_fake = b_cards.copy()

        for i in range(len(a_fake)):
            if a_fake[i] in b_fake:
                b_fake.remove(a_fake[i])
            else:
                count+=1

        count += len(b_fake)
        q_list.append(str(count))


    for i in range(q_count):
        typek,playerk,cardk = input(f'Введите изменение № {i+1} :').strip().split()

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

        update_q_count()
        print(' '.join(q_list))



if __name__ == '__main__':
    kki()



