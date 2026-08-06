for row in range(4, 0, -1):
    for col in range(row):
        print(chr(65 + col), end=" ")
    print()