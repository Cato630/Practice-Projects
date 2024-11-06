#Player Data analasis
'''As a data analyst for the Kansas City Chiefs you have been given a dataset containing information about the players, their positions, and some game statistics.

Let's start analyzing!

    Create a list of dictionaries where each dictionary represents a player. Include attributes such as 'name,' 'position,' and 'jersey number.'
    Print out a list of all player positions in the dataset.
    Choose a player and update their game statistics in the dataset.
    Calculate the average statistics (e.g., yards gained, touchdowns) for all players and print the results.

Congratulations for reaching the end of this chapter! Using data structures, you were able to organize and analyze data for the Chiefs 😎. Think of all the things you can analyze!

✨Just remember practice makes perfect✨.

In the next chapter, we'll explore file input/output in Python. Hope you can handle it! 👀'''

players = [
    { 'name': 'Pattrick Maholmes', 'position': 'QuarterBack', 'GP': 8, 'CMP': 188, 'ATT': 269 } ,
    { 'name': 'Kareem_Hunt', 'position': 'Wide Reciever', 'GP': 5, 'CAR': 111, 'YDS': 414 } ,
    { 'name': 'Carson Steel', 'position': 'Center',  'GP': 8, 'CAR': 44, 'YDS': 111 }
]
    


positions = set(player['position'] for player in players)
print("Player Positions: ", positions)

def update_player_satistics(player_name, new_yards, new_touchdowns):
    for player in players:
        if player['name'] == player_name:
            player['YDS'] = new_yards
            player['TD'] = new_touchdowns
            print(f"Updated Statistics for {player_name}: ")
            print(f"Yards Gained: {player['YDS']}, Touchdowns: {player['TD']}")
            break
        else:
            print(f"No player found with name {player_name}")

update_player_satistics('Pattrick Maholmes', 50 , 3)