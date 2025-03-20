data_str=input("Please enter the values of all the entries in your data set, separated by commas.")
print("\n")

data_str=data_str.replace(" ", "")
data=data_str.split(",")
data=[float(el) for el in data]
data=np.array(data)
mean_data=data.mean() 
if int(mean_data)==float(mean_data):
    mean_data=int(mean_data)

median_data=stat.median(data)

uniquevals=set(data)

def count(data,value):
    i=0
    for el in data:
        if el==value:
            i+=1
    return i

counts=[count(data,value) for value in data]
max_count=max(counts)
modes=[val for val in data if count(data,val)==max_count]
modes=sorted(list(set(modes)))

print(f"The mean of your data set is {mean_data}")
print(f"The mean deviation of your data set is {(sum(abs(data-mean_data*np.ones(len(data)))))/len(data)}")

print(f"The median of your data set is {median_data}")

if len(modes)==len(data):
    print("Your data set has no mode.")
elif len(modes)==1:
    print(f"The mode of your data set is {modes[0]}")
else:
    print(f"Your data set has the following modes: {modes}")
