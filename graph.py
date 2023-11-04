import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4, 5]
y = [0, 2, 4, 6, 8, 10]

plt.plot(x, y, color='red', linewidth=2, linestyle='-', label='y=2x')
plt.title('A Line Plot in Python')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

print("Success")
