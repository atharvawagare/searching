#Linear Searching Function
def searching(array, search_num):
    global flag
    for num in array:
        if num==search_num:
            flag=1
        else:
            flag=0
    if flag==1:
        print(f"{search_num} Found in Array At {array.index(num)}")
    else:
        print(f"{search_num} Not Found in Array")
    
#Driver Code Below

raw_nums=input("Enter Numbers (separated by comma) :: ")
search_num=int(input("Enter Number For Searching :: "))
flag=0
nums=raw_nums.split(",")
array=[]
for num in nums:
    array.append(int(num))
searching(array, search_num)
