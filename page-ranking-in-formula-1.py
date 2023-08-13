import pandas as pd
import numpy as np


drivers=pd.read_csv('C:\\Users\\Sakis\\Desktop\\ΜΑΠ\\DATA ANALYSIS\\4η Εργασία\\Drivers.csv',sep=';')

drivers.set_index('COUNTRY',inplace=True)


#uploading the data from exel,every column containing thw points that every driver has earnd in each country.
#for example the fist column contains thw poionts of Verstaben at the second HAMILTONS points etc.
#in every row is the counntry in which the races took place. 
#we used the data from the races that has took place in the 2022 year in order to avoid changes 
#from the drivers who took part in  



#creating a DataFrame with zeros in order to calculate the points that every driver has earned from the other drivers
#for example in column 1 an row 2 is  the points that has earned VERSTABEN from HAMILTON
#If VERSTABEN had won HAMILTON then is then the points of VERSTABEN are increased +1
results=np.zeros(400).reshape(20,20)
results = pd.DataFrame(results)


#using a triple loop
#j is refers to every every race
#k is the driver which we test if has won versus the other drivers
#and i refers to the other drivers 
#so every time that k driver has won i driver we add at him 1 point in the battle of these two and it is done for each race

for j in range(0,22):
    for k in range(0,20):
        for i in range(0,20):
            if drivers.iloc[j,k] > drivers.iloc[j,i]:
                results.iloc[k,i]=results.iloc[k,i]+1
                
results=results.transpose()


#in this part we construct the G MATRIX as the example in the paper with a value a=0.85
a=0.85
E=pd.DataFrame((np.ones(400)/20).reshape(20,20))
G=a*results + (1-a)*E
z=pd.DataFrame(np.ones(20)/20)

#we are continuing with a while loop in order to find the number of k which is the number of iterations necessary
#to reach the matrix G convergence.We use the power method estimating the error to be less than 10**(-6)
k=0
e=0.000001
error=1
x=pd.DataFrame([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
while error >= e:
    q1=G@x
    p=max(q1)
    x=q1/p
    error=np.linalg.norm(q1-x)
    k=k+1
    
#below we find the q vector which is a 1x20 vector containing the PR scores of each driver
#z is a 1x20 vector containing the initial estimated PR scores, we have populated this  entirely with the value 1/20
w=G**k
q=w@z    
    

    

#in this part of the exercise we use exactly the same way of thinking in order to solve the problem
#only the data is changed
#now we test the teams 
#as previous every column consists of the points that every team has won in each country
#every row consists of the countries where the races took place. The countries have set as indexes
#for example in row 0 and column 0 exists the points tha have won RED BULL in BAHRAIN etc.
teams=pd.read_csv('C:\\Users\\Sakis\\Desktop\\ΜΑΠ\\DATA ANALYSIS\\4η Εργασία\\teams.csv',sep=';')
teams.set_index('COUNTRY',inplace=True)


teams_results=np.zeros(100).reshape(10,10)
teams_results = pd.DataFrame(teams_results)

#we use exactly the same methodology as before with the drivers.The triple loop does exactly the same work fow teams as drivers

for j in range(0,22):
    for k in range(0,10):
        for i in range(0,10):
            if teams.iloc[j,k] > teams.iloc[j,i]:
                teams_results.iloc[k,i]=teams_results.iloc[k,i]+1

                
#below we tune exactly the same methodoly as drivers in order to find the PR scores for each team               

teams_results=teams_results.transpose()
a=0.85
E1=pd.DataFrame((np.ones(100)/10).reshape(10,10))
G1=a*teams_results + (1-a)*E1
z1=pd.DataFrame(np.ones(10)/10)
k1=0
e=0.000001
error_1=1
x1=pd.DataFrame([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
while error_1 >= e:
    q1=G@x1
    p=max(q1)
    x1=q1/p
    error_1=np.linalg.norm(q1-x1)
    k1=k1+1

w1=G1**k1
Q1=w1@z1


#Finally we print the PR scores for each driver first and for each team after
print(q)
print(Q1)

#As we observe the results we can see that Verstaben keeps the lowest score,after is HAMILTON and BOTTAS keeps the third lowest
#As regards the teams RED BULL keep the lowest PR score, FERRARI the second and MERCEDES the third
#Generally speaking we seek to find the lowest PR score which indicated the drover or team that has the more probabilities 
#to win the next race
