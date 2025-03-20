import numpy as np
import statistics as stat
import streamlit as st

st.title("Basic Statistical Measurements")
st.text("*by yarov3so*)")

data_str=st.text_input("Please enter the values of all the entries in your data set, separated by commas:")

if data_str=="":
    st.stop()

data_str=data_str.replace(" ", "")
data=data_str.split(",")
data=[float(el) for el in data]
data=np.array(data)
mean_data=data.mean() 
if int(mean_data)==float(mean_data):
    mean_data=int(mean_data)

def try_int(val):
    if int(val)==float(val):
        return int(val)
    else:
        return float(val)

median_data=stat.median(data)

st.text("")

st.text(f"Your data set has {len(data)} values.")

st.text("")

st.text(f"Range:  Max - Min = {max(data)} - {min(data)} = {max(data)-min(data)}")

st.text("")

mean_calc="Mean: ""( "+(" + ".join([try_int(val) for val in data]))+" )"+" / "+f"{len(data)}" + " = " + f"{mean_data}"
st.text(f"{mean_calc}")

st.text("")

mean_div_calc=""
for val in data:
    mean_div_calc+=" | "+f"{val} -"+f"{mean_data} |  + "
mean_div_calc="( "+mean_div_calc[:-2]+f") / {len(mean_data)}  =  {(sum(abs(data-mean_data*np.ones(len(data)))))/len(data)}"

st.text(f"Mean deviation: {mean_div_calc}")

st.text("")

st.text("Median:")

if len(data)%2==0:
    st.text(f"Your data set has an even number of entries. Therefore, the median is the mean of the two middle terms:")
    median_calc=f" ( {sorted(data)[-1+len(data)//2]} + {sorted(data)[len(data)//2]} ) / 2  =  {median_data}"
    st.text(f"Median: {median_calc}"
else:
    st.text("Your data set has an odd number of entries. Therefore, the median is the middle term:")
    median_calc=f" {sorted(data)[len(data)//2]}"
    st.text(f"Median: {median_calc}")

st.text("")

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

if len(modes)==len(data):
    st.text("Your data set has no mode.")
elif len(modes)==1:
    st.text(f"The mode of your data set is {modes[0]}")
else:
    st.text(f"Your data set has the following modes: {modes}")
