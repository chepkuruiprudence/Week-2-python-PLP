set1 = set(map(int, input("Enter integers for the first set separated by spaces: ").split()))
set2 = set(map(int, input("Enter integers for the second set separated by spaces: ").split()))

# Create a new set with common elements
common_elements = set1.intersection(set2)
print(f"Common elements between the sets: {common_elements}")
