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
    matches_won={}        # will be organized as : team --> year --> no. of matches won that year
    
    for row in match_reader:    #traverse match_reader
        
        winner = row['winner']
        if winner not in matches_won:
            matches_won[winner]={}
            
        year = row['season']
        if year not in matches_won[winner]:
            matches_won[winner][year]=0
        matches_won[winner][year]+=1
  
    
    final={}   # will be organized as : team --> no. of matches won from 2008 to 2017

    for team in matches_won:
        for i in range(2008,2018):      #traverse over the years
            year = str(i)
            
            if team not in final:   #if team not present in final then add it to final and initialize it as list
                final[team]=[]
            
            if year not in matches_won[team]: #if a team not won any match in a particulary year then for that year append the team list(in final) with 0
                final[team].append(0)
            else:                       # else append with number of matches won by that team
                final[team].append(matches_won[team][year])
        
    for i in final:
        print(i,"--",final[i])
    return final

def plot(final):    
    x = [2008,2009,2010,2011,2012,2013,2014,2015,2016,2017]
    j = [0]*len(x)  #j is a list which will update the bottom-height in each iteration : initially - [0,0,0,0,0,0,0,0,0,0]

    # traverse final dictionary
    for i in final:
        plt.bar(x,final[i],bottom=j,label=i)    # plot team i on the bar-graph with its bottom height as list-j 
        for indx in range(len(x)):              # update the bottom height for next team in list j
            j[indx] += final[i][indx]
            
    plt.legend(loc='upper right');
    plt.xlabel('Season')
    plt.ylabel('No. of matches won')
    plt.title('Number of matches won per team per year in IPL.')
    plt.show()


match_reader = read_file('IPL dataset analytics/matches.csv')
final = execute(match_reader)
plot(final)