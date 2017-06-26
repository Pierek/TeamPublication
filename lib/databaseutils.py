import pymssql


class Database:

    def __init__(self):
        self.conn = pymssql.connect(server='localhost:1443', user='teampolska', password='Krakow123',
                               database='WideWorldImporters')

    def get_products(self):
        cursor = self.conn.cursor()
        cursor.execute(
            'SELECT TOP 100 CAST(c.CustomerID AS varchar(10)), c.CustomerName, c.CustomerCategoryName FROM [Website].[Customers] c;')
        row = cursor.fetchone()
        while row:
            print(str(row[0]) + " " + str(row[1]) + " " + str(row[2]))
            row = cursor.fetchone()

        cursor.close()

    def close(self):
        self.conn.close();
