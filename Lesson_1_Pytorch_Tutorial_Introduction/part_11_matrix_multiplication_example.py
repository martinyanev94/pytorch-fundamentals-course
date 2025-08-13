x = torch.arange(6).view(2, 3)
print("X", x)

W = torch.arange(9).view(3, 3)
print("W", W)

h = torch.matmul(x, W)
print("h", h)
[42, 54, 66]])
