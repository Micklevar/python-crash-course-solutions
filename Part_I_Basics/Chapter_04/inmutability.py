# Proof of the immutability of tuples
dimensions = (200, 50)
print(f"Memory location of the original tuple:: {id(dimensions)}")
print("Original dimension:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print(f"\nMemory location of the tuple with new elements: {id(dimensions)}")
print("Modified dimensions:")
for dimension in dimensions:
    print(dimension)
