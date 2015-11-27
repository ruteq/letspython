l = [0, 1, 2, 3, 4, 5]
#l = []
other_list = []

if l == []:
    print (0)
else:
    for i in range(0, len(l)):
        if i % 2 == 1:
            other_list.append(i)
    print other_list
    print sum(other_list)*(l[-1])

