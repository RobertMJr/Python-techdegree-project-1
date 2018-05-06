import csv

#create lists to store future teams and players   
xp_players = []
new_players = []
sharks = []
dragons = []
raptors= []

def create_teams():
    # read the csv file
    with open('soccer_players.csv', newline='') as csvfile:
        teamreader = csv.DictReader(csvfile)
        
        # sort the teams by experience, dividing them in experienced and unexperienced players
        for row in teamreader:
            if row['Soccer Experience'] == 'YES':
                xp_players.append((row['Name'], row['Soccer Experience'], row['Guardian Name(s)']))
            else:
                new_players.append((row['Name'], row['Soccer Experience'], row['Guardian Name(s)']))

    # evenly distribute the experienced players among the three teams            
    for counter, player in enumerate(xp_players):
        if counter <3:
            sharks.append(player)
        elif counter < 6:
            dragons.append(player)
        else:
            raptors.append(player)
    # evenly distribute the players with no experience among the three teams            
    for counter, player in enumerate(new_players):
        if counter <3:
            sharks.append(player)
        elif counter <6:
            dragons.append(player)
        else:
            raptors.append(player)

def write_to_file():
    
    #open the file teams.txt for writing, create it if it doesn't exist
    file = open("teams.txt", "w")

    # write the details of the Sharks team to the file    
    file.write("Sharks \n" + "====== \n")
    for i in sharks:
        file.write(", ".join(i) + "\n")
        
    # write the details of the Dragons team to the file           
    file.write("\nDragons \n" + "======= \n")
    for i in dragons:
        file.write(", ".join(i) + "\n")
        
    # write the details of the Raptors team to the file           
    file.write("\nRaptors \n" + "======= \n")
    for i in raptors:
        file.write(", ".join(i) + "\n")

            
    file.close()
             
def welcome_letter(team):
    # check and ensure the correct team will be mentioned in the welcome letter, add different training dates
    if team == sharks:
        team_name = 'Sharks'
        date_and_time = 'Monday, 20th of April, at 2PM'
    elif team == dragons:
        team_name = 'Dragons'
        date_and_time = 'Tuesday, 21st of April, at 3PM'
    else:
        team_name = 'Raptors'
        date_and_time = 'Friday, 24th of April, at 1PM'

    # go through the team    
    for i in team:
        #make sure the text file will have the format firstname_lastname
        name = i[0].split(" ")
        name = name[0].lower() + "_" + name[1].lower()
        guardian = i[2]
        #write the welcome letter
        file = open("{}.txt".format(name), "w")
        file.write("""Dear {},
\nI am glad to inform you that {} has been selected to be part of the soccer team {}.\nPlease join us {} for the first practice session.
                    \n\nThank you.\nRobert Muraru\nSoccer League Coordinator""".format(guardian, i[0], team_name, date_and_time))
        file.close()

# ensure script does not execute when imported       
if __name__ == "__main__":
    create_teams()
    write_to_file()
    welcome_letter(sharks)
    welcome_letter(dragons)
    welcome_letter(raptors)

