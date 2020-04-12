from time import sleep


def startMergeSort(data, drawData,stepTime):
    global colorData
    colorData=['grey' for x in range(len(data))]
    mergeSort(data,0,len(data)-1,drawData,stepTime)
    colorData=['green' for x in range(len(data))]
    drawData(data,colorData)


def merge(data,start,end,drawData,stepTime):
    i=start
    j=(start+end)//2+1
    a=[]
    while i<=(start+end)//2 and j<=end:
        colorData[i]=colorData[j]='blue'
        drawData(data,colorData)
        colorData[i]=colorData[j]='grey'
        sleep(stepTime)
        if data[i]<data[j]:
            colorData[i]='green'
            drawData(data,colorData)
            sleep(stepTime)
            colorData[i]='grey'
            a.append(data[i])
            i+=1
        else:
            colorData[j]='green'
            drawData(data,colorData)
            sleep(stepTime)
            colorData[j]='grey'
            a.append(data[j])
            j+=1
    
    while i<=(start+end)//2:
        colorData[i]='green'
        drawData(data,colorData)
        sleep(stepTime)
        colorData[i]='grey'
        a.append(data[i])
        i+=1
    
    while j<=end:
        colorData[j]='green'
        drawData(data,colorData)
        sleep(stepTime)
        colorData[j]='grey'
        a.append(data[j])
        j+=1
    for x in range(start,end+1):
        data[x]=a[x-start]



def mergeSort(data,start,end,drawData,stepTime):
    
    if start>=end:
        return

    colorData[start:end+1]=['white' for x in range(start,end+1)]
    drawData(data,colorData)
    sleep(stepTime)
    colorData[start:end+1]=['grey' for x in range(start,end+1)]


    mergeSort(data,start,(start+end)//2,drawData,stepTime)
    mergeSort(data,(start+end)//2+1,end,drawData,stepTime)
    merge(data,start,end,drawData,stepTime)


    colorData[start:end+1]=['white' for x in range(start,end+1)]
    drawData(data,colorData)
    sleep(stepTime)
    colorData[start:end+1]=['grey' for x in range(start,end+1)]
    # for x in range(start,end+1):
    #     drawData(data,colorData)
    #     sleep(stepTime)
