import os
import datetime


class Logging:
    """
    This class collects the needed functions for logging
    and debugging. Logging in file and to console is also possible.
    """

    workLogFileName: str = "hrportal.log"
    errorLogFileName: str = "error.log"
    logFolderName: str = "logs"

    # Check if the logfiles are present, if not, create them
    def __init__(self, parallelprinting: bool = True):
        print("-> Initializing the logging module")
        # Set variable to send logs to stdout too
        if parallelprinting:
            self.logandprint: bool = True
        else:
            self.logandprint: bool = False

        # Set paths
        self.filePath = os.path.dirname(__file__)
        self.projectRootFolder = os.path.dirname(self.filePath)
        self.logFilePath = os.path.join(self.projectRootFolder, self.logFolderName)
        self.workLogFilePath = os.path.join(self.projectRootFolder, self.logFolderName, self.workLogFileName)
        self.errorLogFilePath = os.path.join(self.projectRootFolder, self.logFolderName, self.errorLogFileName)

        if not self.pathexists(self.logFilePath):
            self.createpath(self.logFilePath)

        if not self.fileexists(self.workLogFilePath):
            self.createfile(self.workLogFilePath)
        if not self.fileexists(self.errorLogFilePath):
            self.createfile(self.errorLogFilePath)

    @staticmethod
    def pathexists(path) -> bool:
        if os.path.isdir(path):
            return True
        else:
            return False

    @staticmethod
    def createpath(path) -> bool:
        try:
            os.mkdir(path)
            print(f"-> {path} path created")
            return True
        except:
            print(f"-> There was a problem with creating {path}")
            return False

    @staticmethod
    def fileexists(path) -> bool:
        if os.path.isfile(path):
            return True
        else:
            return False

    @staticmethod
    def createfile(filename) -> bool:
        try:
            f = open(filename, "x")
            f.close()
            print(f"-> {filename} file created")
            return True
        except:
            print(f"-> There was a problem with creating {filename}")
            return False

    def log(self, message) -> bool:
        try:
            current_time = datetime.datetime.now()
            f = open(self.workLogFilePath, "a") # open as append mode
            message = f"{current_time} -- {message}\n"
            f.write(message)
            if self.logandprint:
                print(message)
            f.close()
            return True
        except:
            print(f"There was a problem with writing to {self.workLogFilePath}")
            return False

    def error(self, message) -> bool:
        try:
            current_time = datetime.datetime.now()
            f = open(self.errorLogFilePath, "a")  # open as append mode
            message = f"{current_time} -- {message}\n"
            if self.logandprint:
                print(message)
            f.write(message)
            f.close()
            return True
        except Exception as e:
            print(f"There was a problem with writing to {self.errorLogFilePath}")
            return False


def main():
    # Tests for this module
    logger = Logging(parallelprinting=True)
    logger.log("*****************TESTLOG*****************")
    logger.error("*****************TESTLOG*****************")
    logger.log("*****************TESTLOG*****************")
    logger.error("*****************TESTLOG*****************")
    logger.log("*****************TESTLOG*****************")
    logger.error("*****************TESTLOG*****************")


if __name__ == "__main__":
    main()
