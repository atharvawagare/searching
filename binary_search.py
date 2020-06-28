#Binary Searching Function
def searching(array, search_num):
    flag=0
    lower=0
    upper=len(array)-1
    while lower<upper:
        mid=(lower+upper)//2
        if array[mid]==search_num:
            flag=1
            break
        elif array[mid]<search_num:
            lower=mid+1
        elif array[mid]>search_num:
            upper=mid-1
    if flag==1:
        print(f"{search_num} is Found")
    else:
        print(f"{search_num} is Not Found")

#Selection Sort Function
def sort(array):
    n=len(array)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if array[j]<array[min_index]:
                min_index=j
        array[i], array[min_index]=array[min_index], array[i]
    searching(array, search_num)
         
#Driver Code Below

raw_nums=input("Enter Numbers (separated by comma) :: ")
search_num=int(input("Enter Number For Searching :: "))
nums=raw_nums.split(",")
array=[]
for num in nums:
    array.append(int(num))
sort(array)
