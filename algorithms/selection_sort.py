from time import sleep
colorData=[]

def startSelectionSort(data, drawData,stepTime):

    colorData=['grey' for x in range(len(data))]
    for i in range(len(data)):
        min=data[i]
        min_index=i
        colorData[i]='blue'
        for j in range(i+1,len(data)):
            colorData[j]='white'
            drawData(data,colorData)
            colorData[j]='grey'
            sleep(stepTime)
            if data[j]<min:
                colorData[min_index]='grey'
                min=data[j]
                min_index=j
                colorData[j]='blue'
                drawData(data,colorData)
                # colorData[j]='blue'
                sleep(stepTime)
        data[min_index],data[i]=data[i],data[min_index]
        colorData[i+1:]=['grey' for x in range(i+1,len(data))]
        colorData[i]='green'
        drawData(data,colorData)
        sleep(stepTime)