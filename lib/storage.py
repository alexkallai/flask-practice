import lib.logging as logging
import os
import sqlite3


class Storage:
    """
    This class is for synchronizing the data between
    the inventory in memory and the physical storage
    """

    relativeFilePath = "data"

    # Check if the storage file was created, if not, create it
    def __init__(self, dbname: str = "database.db") -> None:
        # Set up logging
        self.logger = logging.Logging(False)
        # Generate the paths
        self.dbname = dbname
        self.programFilePath = os.path.dirname(__file__)
        self.storageFolderPath = os.path.join(self.programFilePath, self.relativeFilePath)
        self.storageFilePath = os.path.join(self.programFilePath, self.relativeFilePath, self.dbname)
        print(self.storageFilePath)

        # Create the file if it doesn't exist yet
        if not self.filecreated(self.storageFilePath):
            self.createfile(self.storageFilePath)

        # Initialize the database
        self.initdb()

    def initdb(self):

        conn = sqlite3.connect(self.storageFilePath)

        c = conn.cursor()
        c.execute('''
                  CREATE TABLE IF NOT EXISTS products
                  ([product_id] INTEGER PRIMARY KEY, [product_name] TEXT)
                  ''')

        c.execute('''
                  CREATE TABLE IF NOT EXISTS prices
                  ([product_id] INTEGER PRIMARY KEY, [price] INTEGER)
                  ''')

        conn.commit()

    def filecreated(self, path) -> bool:
        try:
            logging.Logging.fileexists(path)  # using static method, because it's already written
            return True
        except Exception as e:
            self.logger.error(f"There was a problem with checking if {path} file exists.")
            return False

    def createfile(self, path) -> bool:
        try:
            logging.Logging.createfile(path)
            return True
        except Exception as e:
            self.logger.error(f"There was a problem with creating {path} file.")
            return False

    def readfile(self) -> str:
        try:
            with open(self.storageFilePath, "r") as f:
                lines = f.readlines()
            return lines
        except Exception as e:
            self.logger.error(f"There was a problem with opening the {self.storageFilePath} file for reading.")


    def writefile(self, datatowrite) -> bool:
        try:
            with open(self.storageFilePath, "w") as f:
                f.write(datatowrite)
            return True
        except Exception as e:
            self.logger.error(f"There was a problem with writing to the {self.storageFilePath} file.")
            return False

def main():
    hrportaldb = Storage()
    hrportaldb.writefile("valami")
    print(hrportaldb.readfile())


if __name__ == "__main__":
    main()