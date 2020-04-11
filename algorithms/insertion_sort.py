from time import sleep
colorData=[]

def startInsertionSort(data, drawData,stepTime):

    colorData=['grey' for x in range(len(data))]
    for i in range(1,len(data)):
        key=data[i]
        j=i-1
        while j>=0 and data[j]>key:
            data[j+1]=data[j]
            j-=1
        data[j+1]=key
