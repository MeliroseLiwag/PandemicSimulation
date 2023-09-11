import pandas as pd
import numpy as np

data = pd.read_csv("Report 100000 reps.csv", header=0)
#print("Data: \n", data[:100]) # See if data is read correctly

## We only need columns "Day" and "Current Infected" for now
df = data.loc[:,["Day", "Current Infected"]]

## Find Expected Number of infected per day ##
## Group Data by "Day" and count the number of Infected
df_mean = df.groupby(["Day"]).mean().rename(columns={"Current Infected": "Mean"}).reset_index()

## Find Sample Mean ##
# Confidence Intervals for Day 1 and Day 2
joined = pd.merge(df, df_mean, on="Day")
day1 = joined[:100000]
day1_mean = (day1["Current Infected"] - day1["Mean"])**2

sm_day1 = day1_mean.sum()/(100000-1)
print("Mean Day 1: ", day1["Mean"][0])
print("Sample Mean Day 1: ", sm_day1)

day2 = joined[100000:200000]
day2_mean = (day2["Current Infected"] - day2["Mean"])**2
sm_day2 = day2_mean.sum()/(100000-1)
print("Mean Day 2: ", day2["Mean"][100000])
print("Sample Mean Day 2: ", sm_day2)

t = 1.96
print("Day 1 CI: [", round(day1["Mean"][0] - t * np.sqrt(sm_day1/100000),4), ","
      ,round(day1["Mean"][0] + t * np.sqrt(sm_day1/100000),4), "]")
print("Day 2 CI: [", round(day2["Mean"][100000] - t * np.sqrt(sm_day2/100000),4), ","
      ,round(day2["Mean"][100000] +  t * np.sqrt(sm_day2/100000),4), "]")

print("Average Number of Infected:\n", df_mean[:27])


## With Immunization ##
# Data has no header but has similar structure to the first data
data2 = pd.read_csv("Report with Immunization - 100000 reps.csv", header = None)
#print("Data with Immunization: \n", data2[:100]) # See if data is read correctly

# Only need columns "Day" and "Current Infected" 
df2 = data2.iloc[:,[1,3]].rename(columns={1:"Day", 3:"Current Infected"})

## Find Expected Number of Infected per day ##
## Group by "Day" and count the number of infected
df2_mean = df2.groupby(["Day"]).mean().rename(columns={"Current Infected": "Mean"}).reset_index()

## Find Sample Mean ##
# Confidence Intervals for Day 1 and Day 2
joined2 = pd.merge(df2, df2_mean, on="Day")
day1_2 = joined2[:100000]
day1_mean_2 = (day1_2["Current Infected"] - day1_2["Mean"])**2

sm_day1_2 = day1_mean_2.sum()/(100000-1)
print("Mean Day 1 w/ Immunization: ", day1_2["Mean"][0])
print("Sample Mean Day 1 w/ Immunization: ", sm_day1_2)

day2_2 = joined2[100000:200000]
day2_mean_2 = (day2_2["Current Infected"] - day2_2["Mean"])**2
sm_day2_2 = day2_mean_2.sum()/(100000-1)
print("Mean Day 2 w/ Immunization: ", day2_2["Mean"][100000])
print("Sample Mean Day 2 w/ Immunization: ", sm_day2_2)

t = 1.96
print("Day 1 CI w/ Immunization: [", round(day1_2["Mean"][0] - t * np.sqrt(sm_day1_2/100000),4), ","
      ,round(day1_2["Mean"][0] + t * np.sqrt(sm_day1_2/100000),4), "]")
print("Day 2 CI w/ Immunization: [", round(day2_2["Mean"][100000] - t * np.sqrt(sm_day2_2/100000),4), ","
      ,round(day2_2["Mean"][100000] +  t * np.sqrt(sm_day2_2/100000),4), "]")

