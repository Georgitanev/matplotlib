from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

labels = ['Watermelon', 'Apples', 'Avocado', 'Melon', 'Strawberries']
slices = [100, 60, 40, 30, 30]
colors = ['#ff7f7f', '#FFE100', '#FFF1B8', '#FFE100', '#DC143C']
explode = [0, 0, 0, 0.15, 0]

plt.pie(slices, labels=labels, colors=colors,
        explode=explode, shadow=True,
        startangle=90, autopct='%1.1f%%',
        wedgeprops={'edgecolor': 'black'})

plt.title("My Favorite Fruit Salad")
plt.tight_layout()
plt.show()
