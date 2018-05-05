import csv

# make sure the script does not execute when imported
if __name__ == "__main__":


    
    list_of_exp_players = []
    list_of_new_players = []
    def sort_players():
        with open('soccer_players.csv', newline='') as csvfile:
            teamreader = csv.DictReader(csvfile)
            for row in teamreader:
                if row['Soccer Experience'] == 'YES':
                    list_of_exp_players.append((row['Name'], row['Height (inches)'], row['Soccer Experience'], row['Guardian Name(s)']))
                else:
                    list_of_new_players.append((row['Name'], row['Height (inches)'], row['Soccer Experience'], row['Guardian Name(s)']))
            print("These are the experienced players: ")
            for player in list_of_exp_players:
                print(player)
            print("\n")
            print("These are the new players: ")
            for player in list_of_new_players:
                print(player)
        
sort_players()            

