from time import sleep
colorData=[]

def startQuickSort(data, drawData,stepTime):
    global colorData
    colorData=['grey' for x in range(len(data))]
    quickSort(data,0,len(data)-1,drawData,stepTime)
    colorData=['green' for x in range(len(data))]
    # drawData(data,colorData)

def quickSort(data,start,end,drawData,stepTime):
    if start>=end:
        return
    
    pivot=partition(data,start,end)
    quickSort(data,start,pivot-1,drawData,stepTime)
    quickSort(data,pivot+1,end,drawData,stepTime)

def partition(data,start,end):
    i=start-1
    pivot=data[end]
    for j in range(start,end):
        if data[j]<=pivot:
            i+=1
            data[i],data[j]=data[j],data[i]
    data[i+1],data[end]=data[end],data[i+1]
    return i+1

data=[434243,34,23,2323,121]
startQuickSort(data,0,0)
print(data)