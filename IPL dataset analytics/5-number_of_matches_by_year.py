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
    # Will store the number of matches played each season
    matches_count = {}
    
    for row in match_reader :
        matches_count[row['season']] = matches_count.get(row['season'] , 0) + 1
            
    for i in matches_count :
        print(i ," : ",matches_count[i])   
    return matches_count

    
def plot(matches_count):
    # Plotting the bar graph
    plt.bar(matches_count.keys(),matches_count.values())
    plt.xlabel('Year')
    plt.xticks(rotation = 90)
    plt.ylabel('No. of matches')
    plt.title('Number of matches played per year for all the years in IPL.')
    plt.show() 
    

match_reader = read_file('IPL dataset analytics/matches.csv')
matches_count = execute(match_reader)
plot(matches_count)