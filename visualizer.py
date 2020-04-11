from tkinter import *
from tkinter import ttk
import random
sys.path.insert(1,'C:\\Users\\skili\\Documents\\GitHub\\Sorting-Algorithm-Visualizer\\algorithms')
# importing our specially designed algorithms
from linear_search import startLinearSearch
from binary_search import startBinarySearch
from bubble_sort import startBubbleSort
from insertion_sort import startInsertionSort
from selection_sort import startSelectionSort
from merge_sort import startMergeSort
from quick_sort import startQuickSort

#to store the array/heights of rectangle
data = []
#to store the colour of respective rectangles
colorData = []



#exits the visualizer
def exitGui():
    root.destroy()



#to start visualization
def visualize(algorithm,stepTime):
    stepTime/=10

    print(stepTime)
    if algorithm=="Bubble Sort":
        startBubbleSort(data,drawData,stepTime)
    elif algorithm=="Linear Search":
        startLinearSearch(data,drawData,stepTime)
    elif algorithm=="Binary Search":
        startBinarySearch(data,drawData,stepTime)
    elif algorithm=="Merge Sort":
        startMergeSort(data,drawData,stepTime)
    elif algorithm=="Selection Sort":
        startSelectionSort(data,drawData,stepTime)
    elif algorithm=="Insertion Sort":
        startInsertionSort(data,drawData,stepTime)
    elif algorithm=="Quick Sort":
        startQuickSort(data,drawData,stepTime)
    elif algorithm=="Radix Sort":
        startMergeSort(data,drawData,stepTime)
    elif algorithm=="Heap Sort":
        startMergeSort(data,drawData,stepTime)
    



#function to move the main window with the cursor drag
def get_pos(event):
    xwin = root.winfo_x()
    ywin = root.winfo_y()
    startx = event.x_root
    starty = event.y_root
    ywin = ywin - starty
    xwin = xwin - startx

    def move_window(event):
        root.geometry("{0}x{1}+{2}+{3}".format(width,height,event.x_root + xwin, event.y_root + ywin))
    startx = event.x_root
    starty = event.y_root

    titlef.bind('<B1-Motion>', move_window)



#function to generate random data
def genData(data_size):
    global data,colorData
    data=colorData=[]
    colorData=['grey' for x in range(int(float(data_size)))]
    for _ in range(int(float(data_size))):
        data.append(random.randrange(1,100))
    drawData(data,colorData)
    sizel.config(text=str(format(int(float(data_size)),"0>3d")))



#function to draw rectangles, 'data' is a list of rectangle heights
def drawData(data,colorData):
    global height,width
    #clears canvas before drawing new data
    canvas.delete("all")
    #setting canvas height,width
    canvas_h=height-20
    canvas_w=width
    #setting the spacing between 2 rectangle
    spacing=2
    #set the width of 1 rectangle
    rectangle_w=(canvas_w-spacing*(len(data)-1))/len(data)

    #normalizing the data
    for i in range(len(data)):
        data[i]=data[i]/max(data)
 
    #drawing the normalized data
    for i,rect_height in enumerate(data):
        x0=i*rectangle_w+(i+1)*spacing
        y0=canvas_h-rect_height*(canvas_h-20)
        x1=(i+1)*rectangle_w+(i+1)*spacing
        y1=canvas_h
        canvas.create_rectangle(x0,y0,x1,y1,fill=colorData[i])
        # canvas.create_text(x0+2,y0-2,text=str(i),fill='white')
    root.update_idletasks()



#to change display delay
def dispDelay(delay):
    delayl.config(text=str(format(float(delay)/10,">03.1f")+" sec"))



#starts the gui
def main():

    #set width and height of window
    global width,height
    width=1000
    height=610

    global root
    root=Tk()
    root.title(" Algorithm Visualizer")
    style=ttk.Style()
    # style.map('TScale',foreground=[('pressed','red'),('active','yellow')])
    style.configure('TScale',background='black')
    # root.overrideredirect(1)
    # root.maxsize(width,height)
    root.resizable(0,0)
    root.config(bg='black')
    root.attributes('-topmost',1)

    #to store the selected algorithm
    algorithm=StringVar()

    global titlef,delayl,sizel
    titlef=Frame(root,width=width,height=height,bg='black')
    titlef.grid(row=0,column=0)
    titlef.bind('<Button-1>', get_pos)
    sizel=Label(titlef,text="50",bg='black',fg='white',font=('Helvetica',25,'bold'))
    sizel.pack(side=LEFT,padx=(10,200))
    Label(titlef,text="Algorithms Visualizer",bg='black',fg='white',font=('Helvetica',25,'bold')).pack(pady=10,side=LEFT)
    delayl=Label(titlef,text="0.0 sec",bg='black',fg='white',font=('Helvetica',25,'bold'))
    delayl.pack(side=LEFT,padx=(190,10))


    #top frame for user input
    topf=Frame(root,width=width, height=250 , bg='black')
    topf.grid(row=1,column=0,padx=10,pady=5)

    global size,speed
    size=IntVar()
    speed=IntVar()
    #row 1 of topf
    # Button(topf,text='x',command=exitGui).grid(row=0,column=5,sticky=E)
    Label(topf,text="Step Delay (sec)",bg='black',fg='white',font=('Helvetica',13,'bold')).grid(row=0,column=0,padx=5,pady=5,sticky=E)
    speed_scale=ttk.Scale(topf,variable=speed,from_=0,to=10,command=dispDelay)
    speed_scale.grid(row=0,column=1,padx=5,pady=5,sticky=W)

    Label(topf,text="Select Algorithm",bg='black',fg='white',font=('Helvetica',13,'bold')).grid(row=0,column=3,padx=(50,0),pady=5,sticky=E)
    algorithm_menu=ttk.Combobox(topf,textvariable=algorithm,state='readonly',values=['Linear Search','Binary Search','Bubble Sort','Selection Sort','Insertion Sort','Merge Sort','Quick Sort','Radix Sort'])
    algorithm_menu.grid(row=0,column=4,padx=5,pady=5,sticky=W)
    algorithm_menu.current(0)

    #row 2 of topf 
    Label(topf,text="Size",bg='black',fg='white',font=('Helvetica',13,'bold')).grid(row=1,column=0,padx=5,pady=5,sticky=E)
    size_scale=ttk.Scale(topf,variable=size,from_=3,to=100,command=genData)
    size_scale.grid(row=1,column=1,padx=5,pady=5,sticky=W)
    size.set(50)
    Button(topf,text="Visualise",bg='white',command=lambda : visualize(algorithm.get(),speed.get())).grid(row=1,column=3,padx=(50,0),pady=5,ipadx=10,sticky=W)
    


    #canvas for visualisation
    global canvas
    canvas = Canvas(root,width=width,height=height-20,bg='black')
    canvas.grid(row=2,column=0,padx=10,pady=5)
    genData(50)
    

    
    root.mainloop()

if __name__ == "__main__":
    main()