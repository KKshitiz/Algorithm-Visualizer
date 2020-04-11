# Algorithm-Visualizer
Learn Algorithms by seeing them in action! Algorithms made easy through animations made in python3 using tkinter library

## User Interface
![UI](./assets/UI.png)

<br>

## Features
- Generate rectangular components with random heights representing element values to be worked upon
- Change number of elements - _'Size'_ and dynamically update the rectangular components. _'Size' can range from 3 to 100_
- Set _'Step-Delay'_ (in sec) - the time interval between each consecutive operation. _Step-delay can range from 0.0-1.0 sec with a resolution of 0.1 sec_
- Sliders have been provided for setting _'Size'_ and _'Step-Delay'_ thus eliminating the hassle of manual input
- Combobox for selecting Algorithm to visualize
- Counters for indicating _'Size'_ and _'Step-Delay'_

<br>

__NOTE: Although efforts have been made to keep the color scheme of the elements intuitive enough, if you wish to check a particular you can look up the color reference provided for every algorithm__ 

<br>


## Algorithms Covered
- ### Searching
  - #### Linear Search
    ![Linear search](./assets/linear.png)
    ##### Color Reference
    - Grey bar  : Elements
    - Blue bar  : Element to be searched
    - White bar : Element currently checking for equivalence
    - Green bar : Element found
  - #### Binary Search
    ![Linear search](./assets/binary.png)
    ##### Color Reference
    - Grey bar  : Elements
    - Blue bar  : Element to be searched
    - Red bar   : Elements discarded after checking
    - Green bar : Element found
  - #### Ternary Search(*)
- ### Sorting
  - #### Bubble Sort
    ![bubble sort](./assets/bubble.png)
    ##### Color Reference
    - Grey bar  : Elements
    - Red bar   : Elements not found in sorted order
    - White bar : Element currently being compared
    - Green bar : Element in sorted order
  - #### Selection Sort
    ![selection sort](./assets/selection.png)
    - Grey bar  : Elements
    - Blue bar  : Element found to be minimum in that iteration
    - White bar : Element being compared with minimum element
    - Green bar : Element in sorted order
    ##### Color Reference
  - #### Insertion Sort(*)
  - #### Merge Sort(*)
  - #### Quick Sort(*)
  - #### Radix Sort(*)

  ## Skip to a particular section
  - [User Interface](#user-interface)
  - [Features](#features)
  - [Algorithms Covered](#algorithms-covered)
    - [Linear Search](#linear-search)
    - [Binary Search](#binary-search)
    - [Bubble Sort](#bubble-sort)
    - [Selection Sort](#selection-sort)
    - [Insertion Sort](#insertion-sort)
    - [Merge Sort](#merge-sort)
    - [Quick Sort](#quick-search)
    - [Radix Sort](#radix-search)