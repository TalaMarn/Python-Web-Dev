import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 2, 30, 4, 50]

plt.plot(x, y)
plt.title("Sample Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

#========pie chart===========
data = [30, 20, 50]
Labels = ["Python", "Java", "C++"]
plt.pie(data, labels=Labels, autopct="%1.1f%%")
plt.show()