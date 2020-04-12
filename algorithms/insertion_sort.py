from time import sleep
colorData=[]

def startInsertionSort(data, drawData,stepTime):

    colorData=['grey' for x in range(len(data))]
    for i in range(1,len(data)):
        key=data[i]
        j=i-1

        colorData[i]='blue'
        drawData(data,colorData)
        sleep(stepTime)
        
        while j>=0 and data[j]>key:

            colorData[j]='white'
            drawData(data,colorData)
            sleep(stepTime)
            colorData[j]='grey'

            data[j+1]=data[j]
            j-=1

        data[j+1]=key

        colorData[j+1]='red'
        drawData(data,colorData)
        sleep(stepTime)
        colorData[j+1]='grey'
        colorData[i]='grey'

    colorData=['green' for x in range(len(data))]
    drawData(data,colorData)

