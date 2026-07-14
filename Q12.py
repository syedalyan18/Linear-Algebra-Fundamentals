from statistics import mode

data=[10,60,20,30,20]
mean=sum(data)/len(data)
print("Mean : ",mean)

sorted_data=sorted(data)
median = sorted_data[len(data)//2] if len(data) % 2!= 0 else\
 (sorted_data[len(data)//2 - 1] + sorted_data[len(data)//2]) / 2

print("Median : ",median)

mode=mode(data)
print("Mode : ",mode)

variance=sum((x - mean)**2 for x in data ) / len(data) 
print("Variance : ",variance)

std_dev=variance ** 0.5
print("Standard Deviation : ",std_dev)