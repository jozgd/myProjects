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

class chanceCard:

    def zero(self,player,player_num,outfile):
        player.position = 0
        player.passedGO(outfile,player_num)
        #Advance to Go (Collect $200)
    def one(self,player,player_num,outfile):
        if(player.positon>24):
            player.passedGO(outfile,player_num)
        player.position = 24
        #Advance to Illinois Ave—If you pass Go, collect $200
    def two(self,player,player_num,outfile):
        if(player.positon>11):
            player.passedGO(outfile,player_num)
        player.position = 11
        #Advance to St. Charles Place – If you pass Go, collect $200
    def three(self,player,player_num,outfile):
        if(player.position > 12 and player.position<28):
            player.position = 28
        else:
            if(player.position>28):
                player.passedGO(outfile,player_num)
            player.position = 12
        board.dice_obj.roll()
        #Advance token to nearest Utility. If unowned, you may buy it from the Bank. If owned, throw dice and pay owner a total ten times the amount thrown.
    def four(self,player,player_num,outfile):
        temp = 0#no use
        #Advance token to the nearest Railroad and pay owner twice the rental to which he/she {he} is otherwise entitled. If Railroad is unowned, you may buy it from the Bank.
    def five(self,player,player_num,outfile):
        temp = 0#no use
        #Bank pays you dividend of $50
    def six(self,player,player_num,outfile):
        temp = 0#no use
        #Get Out of Jail Free
    def seven(self,player,player_num,outfile):
        temp = 0#no use
        #Go Back 3 Spaces
    def eight(self,player,player_num,outfile):
        temp = 0#no use
        #Go to Jail–Go directly to Jail–Do not pass Go, do not collect $200
    def nine(self,player,player_num,outfile):
        temp = 0#no use
        #Make general repairs on all your property–For each house pay $25–For each hotel $100
    def ten(self,player,player_num,outfile):
        temp = 0#no use
        #Pay poor tax of $15
    def eleven(self,player,player_num,outfile):
        temp = 0#no use
        #Take a trip to Reading Railroad–If you pass Go, collect $200
    def tweleve(self,player,player_num,outfile):
        temp = 0#no use
        #Take a walk on the Boardwalk–Advance token to Boardwalk
    def thirteen(self,player,player_num,outfile):
        temp = 0#no use
        #You have been elected Chairman of the Board–Pay each player $50
    def fourteen(self,player,player_num,outfile):
        temp = 0#no use
        #Your building and loan matures—Collect $150
    def fifteen(self,player,player_num,outfile):
        temp = 0#no use
        #You have won a crossword competition—Collect $100

class communityCard:

    def zero(self,player,player_num,outfile):
        temp = 0#no use
        #Advance to Go (Collect $200)
    def one(self,player,player_num,outfile):
        temp = 0#no use
        #Bank error in your favor—Collect $200
    def two(self,player,player_num,outfile):
        temp = 0#no use
        #Doctor's fee—Pay $50
    def three(self,player,player_num,outfile):
        temp = 0#no use
        #From sale of stock you get $50
    def four(self,player,player_num,outfile):
        temp = 0#no use
        #Get Out of Jail Free
    def five(self,player,player_num,outfile):
        temp = 0#no use
        #Go to Jail–Go directly to jail–Do not pass Go–Do not collect $200
    def six(self,player,player_num,outfile):
        temp = 0#no use
        #Grand Opera Night—Collect $50 from every player for opening night seats
    def seven(self,player,player_num,outfile):
        temp = 0#no use
        #Holiday Fund matures—Receive $100
    def eight(self,player,player_num,outfile):
        temp = 0#no use
        #Income tax refund–Collect $20
    def nine(self,player,player_num,outfile):
        temp = 0#no use
        #It is your birthday—Collect $10
    def ten(self,player,player_num,outfile):
        temp = 0#no use
        #Life insurance matures–Collect $100
    def eleven(self,player,player_num,outfile):
        temp = 0#no use
        #Pay hospital fees of $100
    def tweleve(self,player,player_num,outfile):
        temp = 0#no use
        #Pay school fees of $150
    def thirteen(self,player,player_num,outfile):
        temp = 0#no use
        #Receive $25 consultancy fee
    def fourteen(self,player,player_num,outfile):
        temp = 0#no use
        #You are assessed for street repairs–$40 per house–$115 per hotel
    def fifteen(self,player,player_num,outfile):
        temp = 0#no use
        #You have won second prize in a beauty contest–Collect $10
    def sixteen(self,player,player_num,outfile):
        temp = 0#no use
        #You inherit $100


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

    def passedGO(self,outfile,player_num):
        self.position -= 40
        self.earn_money(200)
        outfile.write("Player {} passed GO and collected $200!\n".format(player_num))


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
    
    players = [player() for i in range(4)]#list of the player objects
    spaces = [property() for i in range(40)]#list of empty player objects
    chance_commands = ["zero","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen"]
    community_commands = ["zero","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen"]
    
    random.shuffle(chance_commands)
    random.shuffle(community_commands)
    
    dice_obj = dice()
    chance_obj = chanceCard()
    community_obj = communityCard()

    with open("properties.csv", "r") as properties:#give the properties objects their properties based on the csv
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

def drawChance(chance_commands,outfile,player,player_num):
    print(chance_commands)
    func = chance_commands[0]##attempted switch case
    board.chance_obj.func(player,player_num,outfile)
    chance_commands.append(chance_commands.pop(chance_commands[0]))
    print(chance_commands)


if __name__ == "__main__":
    board = board()

end_game = False

with open("outfile.txt" , 'w') as outfile:
    tempCounter = 0 ##temp
    while (not end_game):
        player_num = 0
        for player in board.players:
            if(not player.player_out):
                board.dice_obj.roll()
                player.check_doubles(board.dice_obj)
                player.position += board.dice_obj.total
                drawChance(board.chance_commands,outfile,player,player_num)#########
                if (player.position > 39):
                    player.passedGO(outfile,player_num)
                currentProperty = board.spaces[player.position]#sets current porperty equal to variable
                outfile.write("Player {} landed on {}!\n".format(player_num,currentProperty.name_of_property))

                ##logic of player section
                if((currentProperty.owner == 5) and (currentProperty.rent != 0) and (player.money>currentProperty.cost)):
                    player.spend_money(currentProperty.cost)
                    ownProperty(board.spaces, player.owned_property, player.position, player_num)
                    outfile.write("Player {} bought {} for {} dollars.\n".format(player_num,board.spaces[player.position].name_of_property,board.spaces[player.position].cost))
                else:
                    if (currentProperty.owner < 5 and currentProperty.owner != player_num):
                        board.players[currentProperty.owner].earn_money(currentProperty.currentRent)
                        player.spend_money(currentProperty.currentRent)
                        outfile.write("Player {} paid Player {} {} dollars.\n" .format(player_num,currentProperty.owner,currentProperty.currentRent))
                
                outfile.write("Player {} has {} dollars.\n".format(player_num,player.money))
                if(player.money<0):
                    outfile.write("Player {} has gone bankrupt and has been eliminated from the game!\n").format(player_num)
                    player.player_out = True
                player_num += 1


        tempCounter += 1
        if (tempCounter == 100):
            end_game = True
    
