#Program to print * in a triangular pattern where number of rows is given by user
#the program will ask what kind of triangle you want to print and then it will print the triangle accordingly to selected option

triangle_type = input("Enter the type of triangle you want to print (left, right, or equilateral): ").lower()
rows = int(input("Enter the number of rows: "))

if triangle_type == "left":
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print("*", end="")
        print()
elif triangle_type == "right":
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "*" * i)
elif triangle_type == "equilateral":
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "*" * (2 * i - 1))
else:
    print("Invalid triangle type.")

if __name__ == "__main__":
    pass