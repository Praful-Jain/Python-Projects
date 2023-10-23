import csv
import matplotlib.pyplot as plt

def read_file(csv_file):
    # Open the CSV file for reading.
    with open(csv_file) as file:
        # Create a CSV reader object.       
        csv_reader = csv.DictReader(file)    
        match_reader = list(csv_reader)  
    return match_reader


def execute(match_reader):
    matches_played={}        # will be organized as : team --> year --> no. of matches played in that year
    
    for row in match_reader:    #traverse match_reader
        team1 = row['team1']
        team2 = row['team2']
        
        #if team1,team2 not present in dict1 then initialize them
        if team1 not in matches_played:
            matches_played[team1]={}
        if team2 not in matches_played:
            matches_played[team2]={}
            
            
        year = row['season']
        
        if year not in matches_played[team1]:
            matches_played[team1][year]=0
        matches_played[team1][year]+=1
            
        if year not in matches_played[team2]:
            matches_played[team2][year]=0
        matches_played[team2][year]+=1
  
  
    match_history={}   # will be organized as : team --> no. of matches played from 2008 to 2017

    for team in matches_played:
        for i in range(2008,2018):      #traverse over the years
            year = str(i)
            
            if team not in match_history:   #if team not present in final then add it to final and initialize it as list
                match_history[team]=[]
            
            
            if year not in matches_played[team]: #if a team not played any match in a particulary year then for that year append the team list(in final) with 0
                match_history[team].append(0)
            else:                       # else append with number of matches played
                match_history[team].append(matches_played[team][year])
        
    for i in match_history:
        print(i,"--",match_history[i])
    return match_history

def plot(match_history):            
    x = [2008,2009,2010,2011,2012,2013,2014,2015,2016,2017]
    j = [0] * len(x)    #j is a list which will update the bottom-height in each iteration : initially - [0,0,0,0,0,0,0,0,0,0]


    # traverse the teams
    for i in match_history:
        plt.bar(x,match_history[i],bottom=j,label=i)    # plot team i on the bar-graph with its bottom height as list-j 
        for indx in range(len(j)):              # update the bottom height for next team in list j
            j[indx] += match_history[i][indx] 
        
    plt.legend(loc='upper right')
    plt.xlabel('Season')
    plt.ylabel('No. of matches played')
    plt.title('Stacked chart of matches played by team by season')
    plt.show()
                    
                    
match_reader = read_file('IPL dataset analytics/matches.csv')
match_history = execute(match_reader)
plot(match_history)