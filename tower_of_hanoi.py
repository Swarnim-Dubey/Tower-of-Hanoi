# A = start
# C = ending
# B = medium


def tower_of_hanoi(n, start, medium, ending):
    if n == 1:
        print(f"Move disk 1 from {start} --> {ending}")
        return
            

    tower_of_hanoi(n-1, start, ending, medium)
    print(f"Move disk {n} from {start} --> {ending}")
    tower_of_hanoi(n-1, medium, start, ending)
    

n = int(input("Enter value for n : "))
tower_of_hanoi(n, 'A', 'B', 'C')
