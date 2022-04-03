#inport pandas
import pandas

#load the csv file
sales = pandas.read_csv("Product_Sales.csv")

#display the records
print(sales[sales.Product=='TV'])
