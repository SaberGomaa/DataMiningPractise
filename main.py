
import  pandas as pd

def printdata():
    dataset = pd.read_excel("data.xlsx")
    print(dataset)


if __name__ == '__main__':
    printdata()

