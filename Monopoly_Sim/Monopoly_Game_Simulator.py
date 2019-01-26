import csv
import random

class dice:

    die1 = 0
    die2 = 0
    total = 0

    def roll(self):
        self.die1 = random.randint(1,6)
        self.die2 = random.randint(1,6)
        self.total = self.die1 + self.die2

class player:
    
    position = 0
    money = 1500
    owned_property = [] #array of position numbers for refrence to main property list
    jail_free = False
    doubles_counter = 0

    total_money_spent = 0
    total_money_earned = 0
    player_out = False
    in_jail = False

    def earn_money(self,amount):
        self.total_money_earned += amount
        self.money = self.money + amount
    
    def spend_money(self,amount):
        self.total_money_spent += amount
        self.money =  self.money - amount

    def check_doubles(self,dice_obj):
        if (dice_obj.die1 == dice_obj.die2):
            self.doubles_counter += 1
            if (self.doubles_counter == 3):
                self.in_jail = True
                self.position = 10


class property:

    name_of_property = ""
    position_num = 0
    times_landed_on = 0
    total_rent_paid = 0

    cost = 0
    currentRent = 0
    rent = 0
    house_1_rent = 0
    house_2_rent = 0
    house_3_rent = 0
    house_4_rent = 0
    hotel_rent = 0
    mortgage_value = 0
    house_cost = 0

    num_of_houses = 0
    num_of_hotels = 0
    owner = 5

    mortgage_state = False
    all_type_owned = False


class board:
    
    players = [player() for i in range(4)]
    spaces = [property() for i in range(40)]
    dice_obj = dice()
    with open("properties.csv", "r") as properties:
        reader = csv.DictReader(properties, delimiter = ',')
        line_count = 0
        for row in reader:
            spaces[line_count].position_num = row
            spaces[line_count].name_of_property = row["name"]
            spaces[line_count].cost = int(row["cost"])
            spaces[line_count].rent = int(row["rent"])
            spaces[line_count].currentRent = spaces[line_count].rent
            spaces[line_count].house_1_rent = int(row["house_1_rent"])
            spaces[line_count].house_2_rent = int(row["house_2_rent"])
            spaces[line_count].house_3_rent = int(row["house_3_rent"])
            spaces[line_count].house_4_rent = int(row["house_4_rent"])
            spaces[line_count].hotel_rent = int(row["hotel_rent"])
            spaces[line_count].mortgage_value = int(row["mortgage_value"])
            spaces[line_count].house_cost = int(row["house_cost"])
            line_count += 1

#moves property out of first list into second list, needs property position
def ownProperty(list1,list2,position,player):
    list1[position].owner = player
    list2.append(position)

if __name__ == "__main__":
    board = board()

end_game = False

tempCounter = 0 ##temp
while (not end_game):
    player_num = 0
    for player in board.players:
        board.dice_obj.roll()
        player.check_doubles(board.dice_obj)
        player.position += board.dice_obj.total
        if (player.position > 39):
            player.position -= 40
            player.earn_money(200)
            print("Player " + str(player_num) + " passed GO and collected $200!")
        currentProperty = board.spaces[player.position]#sets current porperty equal to variable
        print ("Player " + str(player_num) + " landed on "+ str(currentProperty.name_of_property) + "!")

        ##logic of player section
        if((currentProperty.owner == 5) and (currentProperty.rent != 0)):
            player.spend_money(currentProperty.cost)
            ownProperty(board.spaces, player.owned_property, player.position, player_num)
            print ("Player " + str(player_num) + " bought " + board.spaces[player.position].name_of_property + " for " + str(board.spaces[player.position].cost))
        else:
            if (currentProperty.owner < 5 and currentProperty.owner != player_num):
                board.players[currentProperty.owner].earn_money(currentProperty.currentRent)
                player.spend_money(currentProperty.currentRent)
                print ("Player " + str(player_num) + " paid Player " + str(currentProperty.owner) + " " + str(currentProperty.currentRent))
        
        print ("Player " + str(player_num) + " has " + str(player.money) + " Dollars")
        player_num += 1


    tempCounter += 1
    if (tempCounter == 10):
        end_game = True
    
