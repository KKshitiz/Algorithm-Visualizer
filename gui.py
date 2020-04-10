from tkinter import *
from tkinter import ttk
import random
sys.path.insert(1,'C:\\Users\\skili\\Documents\\GitHub\\Sorting-Algorithm-Visualizer\\algorithms')
# importing our specially designed algorithms
from linear_search import startLinearSearch
# from binary_search import startBinarySearch
from bubble_sort import startBubbleSort
# from insertion_sort import startInsertionSort
# from selection_sort import startSelectionSort
# from merge_sort import startMergeSort
# from quick_sort import startQuickSort

#to store the array/heights of rectangle
data = []
#to store the colour of respective rectangles
colorData = []



#to start visualization
def visualize(algorithm,stepTime):
    stepTime/=10
    print(stepTime)
    if algorithm=="Bubble Sort":
        startBubbleSort(data,drawData,stepTime)
    elif algorithm=="Linear Search":
        startLinearSearch(data,drawData,stepTime)



#function to move the main window with the cursor drag
def get_pos(event):
    xwin = root.winfo_x()
    ywin = root.winfo_y()
    startx = event.x_root
    starty = event.y_root
    ywin = ywin - starty
    xwin = xwin - startx

    def move_window(event):
        root.geometry("800x600" + '+{0}+{1}'.format(event.x_root + xwin, event.y_root + ywin))
    startx = event.x_root
    starty = event.y_root

    topf.bind('<B1-Motion>', move_window)



#function to generate random data
def genData(data_size):
    global data,colorData
    data=colorData=[]
    colorData=['grey' for x in range(int(float(data_size)))]
    for _ in range(int(float(data_size))):
        data.append(random.randrange(1,100))
    drawData(data,colorData)



#function to draw rectangles, 'data' is a list of rectangle heights
def drawData(data,colorData):
    #clears canvas before drawing new data
    canvas.delete("all")
    #setting canvas height,width
    canvas_h=380
    canvas_w=600
    #setting the spacing between 2 rectangle
    spacing=20
    #set the width of 1 rectangle
    rectangle_w=(canvas_w-spacing*(len(data)-1))/len(data)

    #normalizing the data
    for i in range(len(data)):
        data[i]=data[i]/max(data)
 
    #drawing the normalized data
    for i,height in enumerate(data):
        x0=i*rectangle_w+(i+1)*spacing
        y0=canvas_h-height*(canvas_h-20)
        x1=(i+1)*rectangle_w+(i+1)*spacing
        y1=canvas_h
        canvas.create_rectangle(x0,y0,x1,y1,fill=colorData[i])
    root.update_idletasks()



#starts the gui
def main():
    global root
    root=Tk()
    root.title("Sorting Algorithm Visualizer")
    root.overrideredirect(1)
    root.maxsize(900,600)
    root.config(bg='black')

    #to store the selected algorithm
    algorithm=StringVar()

    #top frame for user input
    global topf
    topf=Frame(root,width=600, height=200 , bg='grey')
    topf.grid(row=0,column=0,padx=10,pady=5)
    topf.bind('<Button-1>', get_pos)

    #row 1 of topf
    Label(topf,text="Select Algorithm",bg='grey').grid(row=0,column=0,padx=5,pady=5,sticky=W)
    algorithm_menu=ttk.Combobox(topf,textvariable=algorithm,values=['Linear Search','Binary Search','Bubble Sort','Selection Sort','Insertion Sort','Merge Sort','Quick Sort','Radix Sort'])
    algorithm_menu.grid(row=0,column=1,padx=5,pady=5)
    algorithm_menu.current(0)
    Button(topf,text="Visualise",bg='white',command=lambda : visualize(algorithm.get(),speed.get())).grid(row=0,column=2,padx=5,pady=5)

    #row 2 of topf
    global size,speed
    size=IntVar()
    speed=IntVar()
    Label(topf,text="Size",bg='grey').grid(row=1,column=0,padx=5,pady=5,sticky=W)
    size_scale=ttk.Scale(topf,variable=size,from_=3,to=100,command=genData)
    size_scale.grid(row=1,column=1,padx=5,pady=5)
    size.set(50)

    Label(topf,text="Step Speed (sec)",bg='grey').grid(row=1,column=2,padx=5,pady=5,sticky=W)
    speed_scale=ttk.Scale(topf,variable=speed,from_=1,to=10)
    speed_scale.grid(row=1,column=3,padx=5,pady=5)


    #canvas for visualisation
    global canvas
    canvas = Canvas(root,width=600,height=380,bg='black')
    canvas.grid(row=1,column=0,padx=10,pady=5)
    # data=genData(50)
    # drawData(data)
    

    

    root.mainloop()

if __name__ == "__main__":
    main()