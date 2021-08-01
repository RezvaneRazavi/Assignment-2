len_fibo = int(input('len fibo= '))
fibo_list = list()

f1 = 1
f2 = 0

for i in range(len_fibo):
    fibo_list.append(f1)

    temp = f1 + f2
    f2 = f1
    f1 = temp

print(list(fibo_list))