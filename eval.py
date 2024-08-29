

def add_item(a,arr):
    arr.append(a)
    

def remove_item(a,arr):
    arr.remove(a)


def search_item(a,arr):
   
    arr.sort()
    i=0
    j=len(arr)-1
    while(i<j):
        m = (i+j)//2
        if(arr[m]==a):
            return 1
        elif(arr[m]>a):
            i=m+1
        else:
            j=m-1
    return 0    
     

def display_list(arr):
    for x in arr:
        print(x)

ar = []
add_item("A",ar)
add_item("z",ar)
add_item("B",ar)

remove_item("z",ar)
display_list(ar)
if(search_item("C",ar)):
    print("YES")
else:
    print("NO")
display_list(ar)


