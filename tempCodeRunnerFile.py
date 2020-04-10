    data=[10,20,30,40,50]
    #normalizing the data
    for i in len(data):
        data[i]=data[i]/max(data)
    print(data)