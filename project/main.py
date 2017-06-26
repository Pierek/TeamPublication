import sys
import pymssql
from lib.databaseutils import Database


if __name__ == '__main__':
    db = Database()
    db.get_products()
    db.close()
