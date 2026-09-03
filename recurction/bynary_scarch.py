def bynary_scarch(data,tergat,high,low):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if tergat == data[mid]:
            return mid
        elif data[mid] > tergat:
            return bynary_scarch(data,tergat,mid - 1,low)
        else:
            return bynary_scarch(data,tergat,high,mid - 1)
        
number_list = [2,3,5,6,7,9,13,14,16,18,19,23,25]
low = 0
high = len(number_list) - 1

print("The given list of numbers is :",number_list)
target = int(input("Enter the tergat you eant to get :"))
result = bynary_scarch(number_list,target,high,low)
print("The outpuindex of the tergate element is :",result)