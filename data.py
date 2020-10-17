import numpy as np
import pandas as pd

### Two questions
### 1. What is the ratio of goal when playing at home versus playing away for each team?
### 2. Which teams scored the most goals each year?


def mostScores(tScores, teams):
    bestTeam = ' '
    bestScore = 0
    for x in teams:
        if tScores[x] > bestScore:
            bestTeam = x
            bestScore = tScores[x]
    return bestTeam



df = pd.read_csv("premierleague.csv")
print(df.head())
print(df.columns)
print()
print(df.info())
print(df.describe())


print()
print ("The first question is: Is there a benifit to playing as the home team versus playing as the away team")
print()

away = df['FTAG'].sum(0)
home = df['FTHG'].sum(0)

t1 = False  
t2 = False 

if away < home:
    print("Throught 2000-2018, the teams playing at home scored more goals overall.")
    print("Home team goals from 2000-2018 is: %i" % home)
    print("Away team goals from 2000-2018 is: %i" % away)
    t1 = True
else:
    print("The home teams did not score more than teams playing as the away team.")
print()
home = 0
away = 0

for x in df['FTR']:
    if x == 'H':
        home += 1
    elif x == 'A':
        away += 1

if away < home:
    print("Through 2000-2018 the home teams won more than the away teams")
    print("Home teams won: %i games" % home)
    print("Away teams won: %i games" % away)
    t2 = True
else:
    print("Away teams won more games than the home teams")

print() 

if t1 == True and t2 == True:
    print("Question: Is there a benifit to playing as the home team versus playing as the away team")
    print("Answer: Yes, based on the data the home team is more likely to win and score more goals than the away team.")
else:
    print("Question: Is there a benifit to playing as the home team versus playing as the away team")
    print("No, based on the data there is no difference in playing as the home team versus playing as the away.")

print()
print()
print("Question number two: Which teams scored the most each year?")
print()

print("The teams are:")
print(df["HomeTeam"].unique())



tScores = {
    "Team" : 0
}

teams = ["teams"]

for x in df["HomeTeam"].unique():
    tScores[x] = 0
    teams.append(x)

teams.remove("teams")
df['2_digits'] = df['Date'].astype(str).map(lambda x: x[-2:])
t = 0
year = 0
while year <= 18: 
    t = str(year).zfill(2)
    for x in teams:
        for y, z, q in zip(df["HomeTeam"], df["2_digits"], df["FTHG"]):
            if x == y and z == t:
                tScores[x] += q
        for y, z, q in zip(df["AwayTeam"], df["2_digits"].str[-2], df["FTAG"]):
            if x == y and z == t:
                tScores[x] += q
    t = year + 2000
    bTeam = mostScores(tScores, teams)
    print("In the Year " + str(t) + " the team that Scored the most was " + bTeam)
    year += 1
    for x in teams:
        tScores[x] = 0
    

