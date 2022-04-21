from calendar import day_abbr
import pandas as pd
from regex import E

df = pd.read_csv('Oregon Hwy 26 Crash Data for 2019 - Crashes on Hwy 26 during 2019.csv')

data_day = df[(df['Record Type'] == 1)]

#Check if all crashes occur in 2019
if(df['Crash Year'].dropna() == 2019).all():
  print("All occured in crashes in 2019")
else:
  print("No, all did not occur in 2019")

#Check if every crash has Unique Serial #
if(df['Serial #'].dropna().duplicated().any()):
  print("No, all are not unique")
else:
  print("All Unique Serial #")

#Check if every crash has unique participant ID
if(df['Participant ID'].dropna().duplicated().any()):
  print("No, all are not unique")
else:
  print("All Unique participant ID")


