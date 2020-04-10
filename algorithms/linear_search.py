from time import sleep
from random import randrange
colorData=[]

def startLinearSearch(data, drawData,stepTime):
    index=randrange(0,len(data))
    colorData=['grey' for x in range(len(data))]
    colorData[index]='blue'
    for i in range(len(data)):
        colorData[i]='white'
        drawData(data,colorData)
        sleep(stepTime)
        if data[i]==data[index]:
            colorData[i]='green'
            drawData(data,colorData)
            sleep(stepTime)
            break
        else:
            colorData[i]='red'
            sleep(stepTime)