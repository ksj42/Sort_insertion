array=[7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    min = array[i]
    for j in range(i+1,len(array)):
        if(min>array[j]):
            min=array[j]
            index=j
    temp=array[i]
    array[i]=min
    array[index]=temp
    print(array,min,index)
#print(array)




























'''array=[7,5,9,0,3,1,6,2,4,8]
for i in range(1,len(array)):
    for j in range(i,0,-1):
        #print(i);
        if array[j]<array[j-1]:
            array[j],array[j-1]=array[j-1],array[j]
        else:
            break
print(array)

array=[7,5,9,0,3,1,6,2,4,8]
for i in range(len(array)):
    min_index=i;
    for j in range(i+1,len(array)):
        #print(i);
        if array[min_index]>array[j]:
            min_index=j
    array[i],array[min_index]=array[min_index],array[i]
print(array)
'''