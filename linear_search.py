def linear_search(list,target):

    for i in range(0,len(list)):
        if list[i]==target:
            return i

    return None



def veryfi(index):
    if index is not None:
        print("target at index :",index)
    else:
        print("target not found")

num=[1,2,3,4,5,6,7,8,9,10]

result=linear_search(num,5)

veryfi(result)
