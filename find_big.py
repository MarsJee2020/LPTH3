

def  getBig(arr):

    if len(arr) == 0:
        return None
    if len == 1:
        return arr[0]

    if len(arr) == 2:
        # return (arr[0] >= arr[1]) ? arr[0] : arr[1]
        return arr[0] if (arr[0] >= arr[1]) else arr[1]
    else:
        #return (arr[0] - getBig(arr[1:len(arr)]) >= 0 ) ? arr[0] : getBig(arr[1]:len(arr))]
        return arr[0] if (arr[0] - getBig(arr[1:len(arr)]) >= 0 ) else getBig(arr[1:len(arr)])


lst = [1,2,3,4,50,6,7,8,9]

print(getBig(lst))
