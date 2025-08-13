x = torch.arange(12).view(3, 4)
print("X", x)

print(x[:, 1])   # Second column
print(x[0])      # First row
print(x[:2, -1]) # First two rows, last column
print(x[1:3, :]) # Middle two rows
