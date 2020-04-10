from time import sleep
colorData=[]

def startBubbleSort(data, drawData,stepTime):

    colorData=['grey' for x in range(len(data))]
    for i in range(len(data)-1):
        for j in range(len(data)-i-1):
            colorData[j]=colorData[j+1]='white'
            drawData(data,colorData)
            colorData[j]=colorData[j+1]='grey'
            sleep(stepTime)
            if data[j]>data[j+1]:
                data[j],data[j+1]=data[j+1],data[j]
                colorData[j]=colorData[j+1]='red'
                drawData(data,colorData)
                colorData[j]=colorData[j+1]='grey'
                sleep(stepTime)
        colorData[len(data)-1-i]='green'
        drawData(data,colorData)
    colorData[0]='green'
    drawData(data,colorData)