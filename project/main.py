import sys
import pymssql

# from project.lib.project import Project
# from project.lib.options import Options

if __name__ == '__main__':
    conn = pymssql.connect(server='localhost:1443', user='teampolska', password='Krakow123',
                           database='WideWorldImporters')
    cursor = conn.cursor()
    cursor.execute('SELECT TOP 100 CAST(c.CustomerID AS varchar(10)), c.CustomerName, c.CustomerCategoryName FROM [Website].[Customers] c;')
    row = cursor.fetchone()
    while row:
        print(str(row[0]) + " " + str(row[1]) + " " + str(row[2]))
        row = cursor.fetchone()

    # options = Options()
    # opts = options.parse(sys.argv[1:])
    #
    # v = Project(opts)
    #
    # v.date()
    # v.print_example_arg()
