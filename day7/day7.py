from itertools import chain

class FsObj:
    def __init__(self, name, weight, parent):
        self.name = name
        self.weight = weight
        self.parent = parent

    def getWeight(self):
        return self.weight

    def __str__(self) -> str:
        return f"{self.weight} {self.name}"

    def __iter__(self):
        yield self


class FsDir(FsObj):
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.children: list[FsObj] = []

    def getWeight(self):
        return sum([child.getWeight() for child in self.children])

    def __str__(self) -> str:
        return f"dir {self.name}"

    def __iter__(self):
        yield self
        for v in self.children:
            yield from v
        


if __name__ == '__main__':
    MAX_SIZE = 100000
    TOTAL_SIZE = 70000000
    REQUIRED_FREE = 30000000

    currentDir: FsObj = None
    head: FsObj = None

    with open("input.txt") as f:
        """
        Main flow:
        - Go line by line:
        - If line starts with "$" it's a command
            - then parse command
        If not, it's a listing
            - If starts with "dir"
                - make dir object and append to child, also set parent
            - else
                -Make FsObj and append as child, also set parent
        """
        # construct tree
        while(line := f.readline().rstrip()):
            if line.startswith("$"):
                # Do stuff
                cmdList = line.split(" ")
                cmd = cmdList[1] # 0 is $
                if cmd == "cd":
                    if head is None: 
                        print("Adding head")
                        head = FsDir(cmdList[2])
                        currentDir = head
                    else:
                        if cmd == "cd": # no logic needed for ls
                            if cmdList[2] == "..":
                                currentDir = currentDir.parent
                            else:
                                # find the correct child
                                child = list(filter(lambda fsobj: (fsobj.name == cmdList[2] and isinstance(fsobj, FsDir)), currentDir.children))[0]
                                currentDir = child
                        
            elif line.startswith("dir"):
                lineData = line.split(" ")
                newDir = FsDir(lineData[1], currentDir)
                currentDir.children.append(newDir)
            else: # it's a file:
                lineData = line.split(" ")
                newFile = FsObj(lineData[1], int(lineData[0]), currentDir)
                currentDir.children.append(newFile)
    totalSum = 0
    currMin = float('inf')
    freeSpace = TOTAL_SIZE - head.getWeight()
    amtToDelete = REQUIRED_FREE - freeSpace
    for child in head:
        print(child)
        if isinstance(child, FsDir) and child.getWeight() <= MAX_SIZE:
            print(f"DIR {child.name} is at most {MAX_SIZE}")
            totalSum += child.getWeight()
        if isinstance(child, FsDir) and child.getWeight() >= amtToDelete and child.getWeight() < currMin:
            currMin =child.getWeight()

    print(f"sum weight {totalSum}")
    print(f"Smallest dir that frees up enough space is {currMin} ")



    