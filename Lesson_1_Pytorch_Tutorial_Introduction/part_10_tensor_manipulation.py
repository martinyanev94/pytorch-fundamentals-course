x = torch.arange(6)
print("X", x)

x = x.view(2, 3)
print("X", x)
[3, 4, 5]])
x = x.permute(1, 0)  # Swapping dimension 0 and 1
print("X", x)
[1, 4],
          [2, 5]])
