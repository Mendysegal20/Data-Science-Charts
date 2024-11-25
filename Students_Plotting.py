from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('students.csv', delimiter=',')


# ------------------------------------------------------------------------
# pie of number of males nd females. pie works with numerics

plt.figure(1)
m = len(df.loc[df['Gender'] == 'M']) # num of males
f = len(df.loc[df['Gender'] == 'F']) # num of females
plt.pie([m,f], labels=['Male', 'Female'],
        autopct='%.2f%%', colors=['skyblue', 'lightpink'], startangle=90)
plt.title('Devision of ' + str(m + f) + ' students')
plt.legend(loc='upper left')

# ------------------------------------------------------------------------
# horizontal bar of GPA of the students

plt.figure(2)
sorted_df = df.sort_values(by=['GPA']) # we can sort by gpa for better visual of the barh
gpa = sorted_df['GPA']
names = sorted_df['Name']
plt.barh(names, gpa, height=0.3, color=['#9370DB'], edgecolor='black')
plt.xlabel('GPA', fontsize=14)
plt.ylabel('Name', fontsize=12)
# plt.legend(loc='upper left')


# ------------------------------------------------------------------------
# pie of distribution of majors

plt.figure(3)
majors = Counter(df['Major'])
num_of_majors = list(majors.values())
names_of_majors = list(majors.keys())
plt.pie(num_of_majors,
        labels=names_of_majors, autopct=lambda p:int(round(p/100*sum(num_of_majors)))) # show by number


plt.show()




