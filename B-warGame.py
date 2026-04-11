# war card game
#
#
import random

#Global variables
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs') #tuple for immutability
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
 #translating string to integer using a dictionary
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6,'Seven':7, 'Eight':8,'Nine':9,'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14} #obs: uppercased first letter



class Card:
    def __init__(self,suitP,rankP): #'P' as parameter
        self.suit = suitP
        self.rank = rankP
        self.value = values[rankP]
    def __str__(self): #str method defines print output for the class
        return self.rank + "of" + self.suit
    
#create 52 cards hold them as a list of card objects,shuffle,pop dealed cards
class Deck:
    def __init__(self):
        self.all_cards = []

        for suit in suits: #populating
            for rank in ranks:
                new_card = Card(suit,rank) #instanciating
                self.all_cards.append(new_card)

    def shuffle(self): # just to hide implementation details (encapsulation)
        random.shuffle(self.all_cards) #random method doesnt return anything just shuffles the attribute(list) 
    
    def deal_one(self):
        return self.all_cards.pop() #pop with no argument removes the last item, gotta shuffle it before
    
#hold current list of cards, remove or add cards, add 1 or + cards to their list
class Playaa:
    #top-left bottom-right
    #play from the top pop(0) first card; add to the bottom append(default)
    #add multiple cards with the extend(merges lists,puts it at the bottom aswell); append would generate a nested list [1,[2,3]]
    def __init__(self,name):
        self.name = name
        self.your_cards = []

    def remove_one(self):
        return self.your_cards.pop(0) #pops first(leftmost) card 

    def add_card_s(self,new_card_s):
        #adding +1 cards
        if type(new_card_s) == type([]):
            self.your_cards.extend(new_card_s)
        #adding 1 card
        else:
            self.your_cards.append(new_card_s[-1]) #explicit

    def __str__(self):
        return f"{self.player} has {len(self.your_cards)} cards."