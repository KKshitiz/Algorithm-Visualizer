from time import sleep
colorData=[]

def startInsertionSort(data, drawData,stepTime):

    colorData=['grey' for x in range(len(data))]
    for i in range(1,len(data)):
        key=data[i]
        colorData[i]='blue'
        drawData(data,colorData)
        sleep(stepTime)
        colorData[i]='grey'
        j=i-1
        while j>=0 and data[j]>key:
            colorData[j]='white'
            data[j+1]=data[j]
            drawData(data,colorData)
            colorData[j]='grey'
            j-=1
        data[j+1]=key
        colorData[i-1]='green'
        drawData(data,colorData)
        sleep(stepTime)

