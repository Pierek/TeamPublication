import pymssql
from lib.product import Product


class Database:

    def __init__(self):
        self.conn = pymssql.connect(server='localhost:1443', user='teampolska', password='Krakow123',
                               database='WideWorldImporters')

    def get_products(self):
        product_list = []
        cursor = self.conn.cursor()
        cursor.execute(
            'SELECT TOP 100 CAST(c.CustomerID AS varchar(10)), c.CustomerName, c.CustomerCategoryName FROM [Website].[Customers] c;')
        row = cursor.fetchone()
        while row:
            product = Product(str(row[0]), str(row[1]), str(row[2]))
            product_list.append(product)
            #print(str(row[0]) + " " + str(row[1]) + " " + str(row[2]))
            row = cursor.fetchone()

        cursor.close()
        return product_list

    def close(self):
        self.conn.close();
