def some(*args):
    arg_list = args
    print(arg_list)
    for i in range(len(arg_list)):
            if arg_list[i] != arg_list[i+1]:
                some(*args[i+1:i-1])
            else:
                print(arg_list[i])





some(0,1,1,2,3,3,2,1,0)

# print(some(0,1,1,2,3,4,4,5,5,3,2,0))