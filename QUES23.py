#SELECTION SORT
      
def selectSort(arr):
    for i in range(len(arr)):
        print(arr)
        minValue=min(arr[i:])
        minInd=arr.index(minValue)
        arr[i],arr[minInd]=arr[minInd],arr[i]
def main():
    arr=[]
    n=int(input('enter no. of elements:'))
    for i in range (n):
        ele=int(input())
        arr.append(ele)
    print('final arr to use selection sort is:',arr)
    selectSort(arr)
    print('sorted sum is:',arr)
if _name=='main_':
    main()
                            
#INSERTION SORT

def insertion(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j=j-1
            arr[j+1]=key
            print(arr)
def main():
    arr=[]
    n=int(input('enter no. of elemenets:'))
    for i in range(n):
        ele=int(input())
        arr.append(ele)
    print('final arr to use insertion sort is:',arr)
    insertion(arr)
    print('sorted sum is',arr)
if _name=='main_':
    main()
                            
#BUBBLE SORT
                            
def bubbleSort(arr):
    for i in range (len(arr)-1,0,-1):
        for j in range(i):
            print(arr)
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
def main():
    arr=[]
    n=int(input('enter no. of elementes:'))
    for i in range(n):
        ele=int(input())
        arr.append(ele)
    print('final array to use bubble sort is is:',arr)
    bubbleSort(arr)
    print('sorted sum is:',arr)
if _name=='main_':
    main()
