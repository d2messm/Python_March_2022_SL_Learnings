from matplotlib import pyplot as pt

import pandas as pd

sales = pd.read_csv('Product_Sales.csv')

pt.bar(sales.Product,sales.Y2020,label="2020 sales")
pt.bar(sales.Product,sales.Y2018,label="2018 sales",bottom=sales.Y2018)

pt.xlabel("Products")
pt.ylabel("Sales")
pt.title("Yearly sales data")


pt.legend()

pt.show()
