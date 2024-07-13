#Dockcode Assessment Hexagon Pattern
def print_hexagon(rows, cols):
    for r in range(rows):
        for c in range(cols):
            print("  __  ", end=" ")
        print()
        for c in range(cols):
            print(" /  \\ ", end=" ")
        print()
        for c in range(cols):
            print("/    \\", end=" ")
        print()
        for c in range(cols):
            print("\\    /", end=" ")
        print()
        for c in range(cols):
            print(" \\__/ ", end=" ")
        print()
    
    # Print the last row of hexagons
    for c in range(cols):
        print("  __  ", end=" ")
    print()
    for c in range(cols):
        print(" /  \\ ", end=" ")
    print()
    for c in range(cols):
        print("/    \\", end=" ")
    print()


print("inputs :- 4 7")
print_hexagon(4, 7)
# print("\ninputs :- 3 5")
# print_hexagon(3, 5)
