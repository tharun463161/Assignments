start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
print("Positive numbers in the range:", start, "to", end)
for num in range(start, end + 1):
    if num > 0:
        print(num, end=" ")
