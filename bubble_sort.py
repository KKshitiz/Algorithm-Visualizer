import time

def startBubbleSort(data, drawData):
    for i in range(len(data)-1):
        for j in range(len(data)-i-1):
            if data[j]>data[j+1]:
                data[j],data[j+1]=data[j+1],data[j]
                drawData(data)
                time.sleep(0.2)