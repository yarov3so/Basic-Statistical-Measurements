import numpy as np
import statistics as stat
import streamlit as st

st.title("Basic Statistical Measurements")
st.markdown("*by yarov3so*")

data_str=st.text_input("Please enter all the numerical entries that appear in your data set, separated by commas:")

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

st.markdown(f"Your data set has **{len(data)}** entries.")

st.markdown(f"Sorted in ascending order, they are: {[try_int(el) in sorted(data)]}")

st.text("")

st.markdown(f"**Range:**")
st.markdown(f"Range = Maximum value - Minimum value = {max(data)} - {min(data)} = **{max(data)-min(data)}**")

st.text("")

mean_data=round(mean_data,2)
mean_data=try_int(mean_data)

mean_calc="( "+(" + ".join([str(try_int(val)) for val in data]))+" )"+" / "+f"{len(data)}" + " = " + f"**{mean_data}**"
st.markdown("**Mean:**")
st.markdown(f"Mean = {mean_calc}")

st.text("")

mean_div_calc=""
for val in data:
    mean_div_calc+=" | "+f"{val} - "+f"{mean_data} |  + "
mean_div_calc="( "+mean_div_calc[:-2]+f") / {len(data)}  =  **{round((sum(abs(data-mean_data*np.ones(len(data)))))/len(data),2)}**"

st.markdown("**Mean Deviation:**")
st.markdown(f"Mean Deviation = {mean_div_calc}")

st.text("")

st.markdown("**Median:**")

if len(data)%2==0:
    st.markdown(f"Your data set has an even number of entries. Therefore, the median is the mean of the two middle terms:")
    median_calc=f" ( {sorted(data)[-1+len(data)//2]} + {sorted(data)[len(data)//2]} ) / 2  =  **{median_data}**"
    st.markdown(f"Median = {median_calc}")
else:
    st.markdown("Your data set has an odd number of entries. Therefore, the median is the middle term:")
    median_calc=f"**{sorted(data)[len(data)//2]}**"
    st.markdown(f"Median = {median_calc}")

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
modes=[try_int(val) for val in data if count(data,val)==max_count]
modes=[ mode for mode in sorted(list(set(modes)))]

modes_str=""
for mode in modes:
    modes_str+=f"**{mode}**, "
modes_str=modes_str[:-2]

st.markdown("**Mode:**")
if len(modes)==len(data):
    st.markdown("Your data set has no mode.")
elif len(modes)==1:
    st.markdown(f"The mode of your data set is {modes[0]}")
else:
    st.markdown(f"Your data set has the following modes: {modes_str}")
