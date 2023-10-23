import csv 
import matplotlib.pyplot as plt

def read_file(csv_file):
    
    # Open the CSV file for reading.
    with open(csv_file) as file:
        # Create a CSV reader object.       
        csv_reader = csv.DictReader(file)    
        deliveries_reader = list(csv_reader)  
    return deliveries_reader


def execute(deliveries_reader):
    # Dictionary to store runs of players of rcb
    runs_scored={}
    
    for row in deliveries_reader:
        if row['batting_team'] == 'Royal Challengers Bangalore' :
            if row['batsman'] in runs_scored :
                runs_scored[row['batsman']] += int(row['total_runs']) 
            else :
                runs_scored[row['batsman']] = int(row['total_runs']) 
          
    # Sorting in descending order      
    runs_scored = dict(sorted(runs_scored.items(),key = lambda x:x[1], reverse=True))
    
    # Dictionary to store top 10 RCB batsman
    top_ten={}
    count=0
    for i in runs_scored :
        top_ten[i]=runs_scored[i]
        count+=1
        if count==10 :
            break
        
    for i in top_ten:
        print(i , " : " , top_ten[i])
    return top_ten

def plot(top_ten):
    # Plotting the bar graph
    plt.bar(top_ten.keys(),top_ten.values())
    plt.xlabel('Player Name')
    plt.xticks(rotation=90)     #To print the labels vertically on the x-axis in Matplotlib,
    plt.ylabel('Total Runs Scored')
    plt.title('Top 10 batsmen of RCB')
    plt.show()
    
deliveries_reader = read_file('IPL dataset analytics/deliveries.csv')
top_ten = execute(deliveries_reader)
plot(top_ten)