from time import sleep


def startMergeSort(data, drawData,stepTime):
    global colorData
    colorData=['grey' for x in range(len(data))]
    mergeSort(data,0,len(data)-1,drawData,stepTime)


def merge(data,start,end,drawData,stepTime):
    i=start
    j=(start+end)//2+1
    a=[]
    while i<=(start+end)//2 and j<=end:
        colorData[i]=colorData[j]='white'
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
            colorData[i]='green'
            drawData(data,colorData)
            sleep(stepTime)
            colorData[i]='grey'
            a.append(data[j])
            j+=1
    
    while i<=(start+end)//2:
        a.append(data[i])
        i+=1
    
    while j<=end:
        a.append(data[j])
        j+=1
    data[start:end+1]=a


def mergeSort(data,start,end,drawData,stepTime):
    
    if start>=end:
        return

    mergeSort(data,start,(start+end)//2,drawData,stepTime)
    mergeSort(data,(start+end)//2+1,end,drawData,stepTime)
    merge(data,start,end,drawData,stepTime)
