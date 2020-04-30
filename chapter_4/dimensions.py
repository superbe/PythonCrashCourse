dimensions = (200, 50)

print(dimensions[0])
print(dimensions[1])

# dimensions[0] = 250

my_t = (3,)
print(my_t[0])

for dimension in dimensions:
    print(dimension)

dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
