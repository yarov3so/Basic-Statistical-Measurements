import numpy as np
import statistics as stat
import streamlit as st

st.title("Basic Statistical Measurements")

st.markdown("Calculates range, mean, mean deviation, median and mode(s), if any.")

data_str=st.text_input("Enter all the numerical entries that appear in your data set, separated by commas:")

if data_str=="":
    st.stop()

data_str=data_str.replace(" ", "")
data=data_str.split(",")
data=[float(el) for el in data]
data=np.array(data)
mean_data=data.mean() 
if int(mean_data)==float(mean_data):
    mean_data=int(mean_data)

def try_int(num):
    
    num_int=None
    try:
        num_int=int(num)
    except:
        None
    if num==num_int:
        return num_int
    elif (num<=0.1 and num>=0) or (num>=-0.1 and num<=0):
        return "{:.2g}".format(float(num))
    else:
        return round(float(num),2)

median_data=stat.median(data)

st.text("")

st.markdown(f"Your data set has **{len(data)}** entries.")

st.markdown(f"Sorted in ascending order, they are: {[try_int(el) for el in sorted(data)]}")

st.text("")

st.markdown(f"**Range:**")
st.markdown(f"Range = Maximum value - Minimum value = {try_int(max(data))} - {try_int(min(data))} = **{try_int(max(data)-min(data))}**")

st.text("")

mean_data=round(mean_data,2)
mean_data=try_int(mean_data)

mean_calc="( "+(" + ".join([str(try_int(val)) for val in data]))+" )"+" / "+f"{len(data)}" + " = " + f"**{mean_data}**"
st.markdown("**Mean:**")
st.markdown(f"Mean = {mean_calc}")

st.text("")

mean_div_calc=""
for val in data:
    mean_div_calc+=" | "+f"{try_int(val)} - "+f"{try_int(round(mean_data,2))} |  + "
mean_div_calc="( "+mean_div_calc[:-2]+f") / {len(data)}  =  **{try_int(round((sum(abs(data-mean_data*np.ones(len(data)))))/len(data),2))}**"

st.markdown("**Mean Deviation:**")
st.markdown(f"Mean Deviation = {mean_div_calc}")

st.text("")

st.markdown("**Median:**")

if len(data)%2==0:
    st.markdown(f"Your data set has an even number of entries. Therefore, the median is the mean of the two middle terms:")
    median_calc=f" ( {try_int(sorted(data)[-1+len(data)//2])} + {try_int(sorted(data)[len(data)//2])} ) / 2  =  **{try_int(median_data)}**"
    st.markdown(f"Median = {median_calc}")
else:
    st.markdown("Your data set has an odd number of entries. Therefore, the median is the middle term:")
    median_calc=f"**{try_int(sorted(data)[len(data)//2])}**"
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
    st.markdown("Your data set has no mode, as all the entries are distinct.")
elif len(modes)==1:
    st.markdown(f"The mode of your data set is **{modes[0]}**")
else:
    st.markdown(f"Your data set has the following modes: {modes_str}")

st.text("")
st.markdown("""*Crafted by yarov3so*   
<a href="https://www.buymeacoffee.com/yarov3so" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="width: 9em; height: auto; padding-top: 0.7em; padding-bottom: 1em" ></a>  
See my other [Math Help Tools](https://mathh3lptools.streamlit.app)""",unsafe_allow_html=True)
