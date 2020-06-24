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
        print(f"{search_num} is Found At {mid+1} Position")
    else:
        print(f"{search_num} is Not Found")
    
#Driver Code Below

raw_nums=input("Enter Numbers (separated by comma) :: ")
search_num=int(input("Enter Number For Searching :: "))
nums=raw_nums.split(",")
array=[]
for num in nums:
    array.append(int(num))
searching(array, search_num)
