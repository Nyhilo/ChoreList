import csv

class ChoreList:
    def __init__(self, Filename="chores.csv"):
        self.filename = Filename
        self.workers = []
        self.chores = []

    def printUsage(self):
        print("Open the included .csv file 'chores.csv by default' in a text or spreadsheet editor.")
        print("The first line should be a list of names of the individuals that the chores are being split between.")
        print("The following lines should be the name of each chore paired with a value assigned to it.")
        print("An example file might look like the following:\n")
        print("Name1,Name2,Name3")
        print("Chore1,1")
        print("Chore2,3")
        print("Chore3,2")
        print("Chore4,1")
        print("Chore5,4\n")

    def loadChores(self):
        import os.path
        if not os.path.exists(self.filename):
            with open(self.filename,newline='') as file:
                pass
            self.printUsage()
            exit()
        else:
            pass    # Read the file, load the values into self.workers and self.chores


def main():
    print("This script is a work in progress.")
    print("Future functionality will be as follows:\n")
    l = ChoreList()
    l.printUsage()

if __name__ == '__main__':
    main()