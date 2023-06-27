# 11729 하노이탑(완)
def hanoi(number_of_disks_to_move, from_, to_, via_):
    if number_of_disks_to_move == 1:
        print(from_, to_)
    else:
        hanoi(number_of_disks_to_move-1, from_, via_, to_)
        print(from_, to_)
        hanoi(number_of_disks_to_move-1, via_, to_, from_)

n = int(input())
print(2**n - 1)
hanoi(n,1,3,2)