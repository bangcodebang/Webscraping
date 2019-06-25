import matplotlib.pyplot as plt
import csv


date = []
price = []





path = "/home/rohit/Downloads/stock-market/GOOGL.csv"
file = open(path)
csvreader = csv.reader(file)
header = next(csvreader)
for row in csvreader:
    date1 = row[0]#you only get the years
    open_price = float(row[1])
    price.append(open_price)
    date.append(date1)


plt.plot(date[0:10],price[0:10])
plt.show()
plt.close(fig=None)