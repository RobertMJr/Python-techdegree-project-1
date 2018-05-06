import csv
   
xp_players = []
new_players = []
sharks = []
dragons = []
raptors= []

def create_teams():
    with open('soccer_players.csv', newline='') as csvfile:
        teamreader = csv.DictReader(csvfile)
        for row in teamreader:
            if row['Soccer Experience'] == 'YES':
                xp_players.append((row['Name'], row['Soccer Experience'], row['Guardian Name(s)']))
            else:
                new_players.append((row['Name'], row['Soccer Experience'], row['Guardian Name(s)']))
    for counter, player in enumerate(xp_players):
        if counter <3:
            sharks.append(player)
        elif counter < 6:
            dragons.append(player)
        else:
            raptors.append(player)
                
    for counter, player in enumerate(new_players):
        if counter <3:
            sharks.append(player)
        elif counter <6:
            dragons.append(player)
        else:
            raptors.append(player)

def write_to_file():
    file = open("teams.txt", "w")
        
    file.write("\nSharks \n" + "====== \n")
    for i in sharks:
        file.write(", ".join(i) + "\n")
            
    file.write("\nDragons \n" + "====== \n")
    for i in dragons:
        file.write(", ".join(i) + "\n")
            
    file.write("\nRaptors \n" + "====== \n")
    for i in raptors:
        file.write(", ".join(i) + "\n")

            
    file.close()
             

       
if __name__ == "__main__":
    create_teams()
    write_to_file()

