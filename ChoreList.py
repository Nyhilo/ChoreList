class ChoreList:
    def __init__(self, Filename="chores.csv"):
        self.filename = Filename
        self.workers = []
        self.fullworkers = []
        self.chores = []
        self.average = 0

    def __str__(self):
        out = ""
        if len(self.workers)>0:
            for worker in self.workers:
                out = out+worker[0]+": Points: "+str(worker[1])+"\n"
                for i in range(2,len(worker)):
                    out = out+"\t"+worker[i][0]+", "+str(worker[i][1])+"\n"
        if len(self.fullworkers)>0:
            for worker in self.fullworkers:
                out = out+worker[0]+": Points: "+str(worker[1])+"\n"
                for i in range(2,len(worker)):
                    out = out+"\t"+worker[i][0]+", "+str(worker[i][1])+"\n"
        # print("Workers that can take more chores:",self.workers)
        # print("Workers that have chores:",self.fullworkers)
        # print("Chores:")
        # for item in self.chores:
        #     print(item)
        # return "Points per person: " + str(round(self.average,2))
        return out + "\n"

    def printUsage(self):
        print("Open the included .csv file 'chores.csv by default' in a text or"
            + " spreadsheet editor.")
        print("The first line should be a list of names of the individuals that"
            + " the chores are being split between.")
        print("The following lines should be the name of each chore paired with"
            + " a value assigned to it.")
        print("An example file might look like the following:\n")
        print("Name1,Name2,Name3")
        print("Chore1,1")
        print("Chore2,3")
        print("Chore3,2")
        print("Chore4,1")
        print("Chore5,4\n")

    def loadChores(self):
        import os.path
        import csv
        if not os.path.exists(self.filename):
            with open(self.filename,'w+') as file:
                pass
            self.printUsage()
            exit()
        else:
            # Read the file, load the values into self.workers and self.chores
            with open(self.filename,'r',newline='') as file:
                reader = csv.reader(file, delimiter=',', quotechar='|')
                nameFlag = True
                for row in reader:
                    if nameFlag:
                        self.workers=row
                        nameFlag = False
                    else:
                        self.chores.append([row[0],int(row[1])])
        tempList = []
        for name in self.workers:
            tempList.append([name,0])
        self.workers = tempList
        self.chores=sorted(self.chores, key=lambda l: l[1])

        totalPoints = 0
        for chore in self.chores:
            totalPoints += chore[1]
        self.average = totalPoints/len(self.workers)

    def pick(self):
        import random
        if len(self.chores)>0:
            chore = self.chores.pop()
            if len(self.workers)>0:
                r = random.randint(0,len(self.workers)-1)
                worker = self.workers.pop(r)
                worker[1] += chore[1]
                worker.append(chore)
                if worker[1] > self.average:
                    self.fullworkers.append(worker)
                else:
                    self.workers.append(worker)
            else:
                self.workers=sorted(
                    self.workers, key=lambda l: l[1], reverse=true)

                worker = self.fullworkers.pop()
                worker[1] += chore[1]
                worker.append(chore)
                self.fullworkers.append(worker)

            return True
        else:
            return False


def main():
    chores = ChoreList()
    chores.loadChores()
    while len(chores.workers)>0 and len(chores.chores)>0:
    # for i in range(0,6):
        chores.pick()
    
    print(chores)


if __name__ == '__main__':
    main()