import sys
import pymssql
from lib.databaseutils import Database
from lib.xmlutils import XML


if __name__ == '__main__':
    db = Database()
    #db.get_products()
    xml1 = XML()
    xml1.write2file(db.get_products())
    db.close()

