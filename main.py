import matplotlib.pyplot as plt
import pandas as pd

headings = 'date,actual mean,actual min,actual max,average min,average max,record low,record high,record low year,record high year,actual precipitation,average precipitation,record precipitation'
date = []
act_max = []
act_min = []
avg_max = []
avg_min = []
# 1.1
with open('NYCTempRecord.txt', 'r') as txt_file:
    # print(txt_file.readline())
    txt_file.readline()
    with open('NYCTemps.csv', 'w') as csv_file:
        csv_file.write(headings + '\n')
        for line in txt_file:
            # print(line)
            csv_file.write(line)
            info = line.split(',')
            date.append(info[0])
            act_min.append(info[2])
            act_max.append(info[3])
            avg_min.append(info[4])
            avg_max.append(info[5])

# 1.2
# a.
tempYearMaxAct = {}
# b.
tempYearMinAct = {}
# c.
tempYearMaxAvg = {}
# d.
tempYearMinAvg = {}

with open('NYCTemps.csv', 'r') as file:
    file.readline()
    #print(len(file.readlines()))
    for i in range(len(date)):
        # a.
        tempYearMaxAct[date[i]] = act_max[i]
        # b.
        tempYearMinAct[date[i]] = act_min[i]
        # c.
        tempYearMaxAvg[date[i]] = avg_max[i]
        # d.
        tempYearMinAvg[date[i]] = avg_min[i]

# 1.3

act_hottest_temp = pd.Series(tempYearMaxAct).max()
print("Actual temp for hottest day: " + act_hottest_temp)
avg_hottest_temp = pd.Series(tempYearMaxAvg).max()
print("Average temp for hottest day: " + avg_hottest_temp)
act_coldest_temp = pd.Series(tempYearMaxAct).min()
print("Actual temp for coldest day: " + act_coldest_temp)
avg_coldest_temp = pd.Series(tempYearMaxAvg).min()
print("Average temp for coldest day: " + avg_coldest_temp)

# 1.6
df = pd.read_csv('NYCTemps.csv')

# 1.4
precipYearMaxAct = df['actual precipitation']
precipYearMinAct = df['actual precipitation']
precipYearAvg = df['average precipitation']

# 1.5
print(precipYearMaxAct.max())
print(precipYearMinAct.min())
print(precipYearAvg.min())

# 1.7
x_record_low_years = df['record low year'].sort_values().unique()
x_record_high_years = df['record high year'].sort_values().unique()
print(x_record_low_years[0])
print(x_record_high_years[0])
y_no_record_low_years = []
y_no_record_high_years = []

for i in range(len(date)):
    y_no_record_low_years[i] = df[df['record low year'] == x_record_low_years[i]].value_counts()
    y_no_record_high_years[i] = df['record high year'].str.contains(x_years[i]).sum()
print(y_no_record_low_years)
# print(count_2014)
# print(count_2015)

# a.
x = ['2014', '2015']
y = [count_2014, count_2015]
plt.xlabel('Year')
plt.ylabel('number of record high temps')
plt.title('Frequency Diagram')
plt.bar(x, y)
#plt.show()
# b.


# 1.8

# 1.9
