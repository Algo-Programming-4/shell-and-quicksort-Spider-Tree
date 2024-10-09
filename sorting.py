#bubble(list) -> sorted ist
def bubble(item):
    for i in range(len(item)-1):
        skip=True
        for j in range(len(item)-i-1):
            a=item[j]
            b=item[j+1]
            if a>b:
                item[j]=b
                item[j+1]=a
                skip=False
        if (skip):
           break
    return item

def interinsertionsort(unsorted,startI,gap):
   
    for i in range(gap+startI,len(unsorted),gap):
        j=i
        while j-gap>startI and unsorted[j-gap]>unsorted[j]:
            unsorted[j-gap],unsorted[j]=unsorted[j],unsorted[j-gap]
            j=j-gap
        
    return unsorted


#selection(list) -> sorted list
def selection(unsorted):
    for i in range(len(unsorted)-1):
        small = i
        for j in range(i+1, len(unsorted)):
         if unsorted[j] < unsorted[small]:
            small = j
        temp = unsorted[i]
        unsorted[i] = unsorted[small]
        unsorted[small] = temp
    return unsorted

#insertion(list) -> sorted list
def insertion(unsorted):
    for i in range(1,len(unsorted)):
        j=i
        while j>0 and unsorted[j-1]>unsorted[j]:
            unsorted[j-1],unsorted[j]=unsorted[j],unsorted[j-1]
            j=j-1
    return unsorted
#shell(list) -> sorted list
def shell(unsorted,gapValues):
    
    for gap in gapValues:
        for x in range(gap):
            interinsertionsort(unsorted,x,gap)
    return unsorted
def party(unsorted,low,high):
    mid=low+(high-low)//2
    pivot = unsorted[mid]
    done=False
    while not done:
          while(unsorted[low]<pivot):
              low+=1
          while(pivot<unsorted[high]):
              high-=1
          if(low>=high):
              done=True
          else:
              unsorted[low],unsorted[high]=unsorted[high],unsorted[low]
              low=low+1
              high=high-1
    return high
#quicksort(list) -> sorted list
def quicksort(unsorted,low,high):
    if(low>=high):
        return 
    lowEnd=party(unsorted,low,high)
    quicksort(unsorted,low,lowEnd)
    quicksort(unsorted,lowEnd+1,high)
    return unsorted
