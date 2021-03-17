#####################################################################################
##              Simple program to demonstrate Chess.com API using Python           ##
##              Author: Anom Chakravorty | Github: anomic30                        ##
#####################################################################################
import requests
from chessdotcom import get_leaderboards
from chessdotcom import get_player_stats
from chessdotcom import get_player_game_archives

def print_leaderboards():
    data = get_leaderboards().json['leaderboards']
    categories = data.keys()
    for category in categories:
        print(category)
        for idx, entry in enumerate(data[category]):
            print("Rank: {}  | UserName: {}  | Rating: {}".format(idx + 1, entry['username'], entry['score']))


def print_player_rating(username):
    data = get_player_stats(username).json['stats']
    # print(data)
    categories = ['chess_blitz', 'chess_rapid', 'chess_bullet']
    for i in categories:
        print("Category: {}".format(i))
        print("Current rating: {}".format(data[i]['last']['rating']))
        print("Best rating: {}".format(data[i]['best']['rating']))
        print("Records: {}".format(data[i]['record']))

def get_most_recent_game(username):
    data=get_player_game_archives(username).json
    url = data['archives'][-1]
    games = requests.get(url).json()
    game = games['games'][-1]
    print(game['url'])
    

if __name__ == "__main__":
    print("<<<< This Python script demonstrates the use of chess.com API >>>>")
    while True:
        print("1. To print leaderboards, press '1'\n2. To print player rating, press '2'\n3. To watch a players last match, press '3'")
        print("4. To quit the program, press '4'")
        n=input(">>> ").lower().rstrip()
        if n=='4':
            break
        elif n=='1':
            print_leaderboards()
            print("\n")
        elif n=='2':
            name = input("Enter the user name: ")
            print_player_rating(name)
            print("\n")
        elif n=='3':
            name = input("Enter the user name: ")
            get_most_recent_game(name)
            print("\n")
        else:
            print("Invalid choice")


