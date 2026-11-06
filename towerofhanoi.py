count = 0

def tower_of_hanoi(n, source, auxiliary, destination):
    global count

    if n == 1:
        count += 1
        print(f"Step {count}: Move disk 1 from {source} to {destination}")
        return

    tower_of_hanoi(n - 1, source, destination, auxiliary)

    count += 1
    print(f"Step {count}: Move disk {n} from {source} to {destination}")

    tower_of_hanoi(n - 1, auxiliary, source, destination)


n = int(input("Enter number of disks: "))

tower_of_hanoi(n, 'A', 'B', 'C')

print("\nTotal number of steps:", count)