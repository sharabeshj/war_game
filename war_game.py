from random import shuffle

SUITE = 'H D S C'.split( )
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split( )

class Deck:
	def __init__(self):
		self.all_cards = [(s,r) for s in SUITE for r in RANKS]

	def shuffle(self):
		shuffle(self.all_cards)

	def split_deck(self):
		return (self.all_cards[:26],self.all_cards[26:])	


class Hand: 
	def __init__(self,cards):
		self.hand = cards

	def __str__(self):
		return "contains {} cards".format(len(self.hand))	

	def add_card(self,added_cards):
		self.hand.extend(added_cards)

	def remove_card(self):
		return self.hand.pop()

	def card_count(self):
		return len(self.hand)

class Player:
	def __init__(self,name,hand):
		self.name = name
		self.hand = hand

	def play_card(self):
		drawn_card = self.hand.remove_card()
		return drawn_card

	def remove_war_card(self):
		war_cards = []
		if self.hand.card_count() < 3:
			return war_cards
		else:
			for x in range(3):
				war_cards.append(self.hand.remove_card())
			return war_cards

	def still_has_cards(self):
		return self.hand.card_count()!=0		

print("WELCOME TO WAR GAME --coded in python")

deck = Deck()
deck.shuffle()
(hand1,hand2) = deck.split_deck()			

comp = Player("computer",Hand(hand1))
name = input("Choose your user name : ")
player = Player(name,Hand(hand2))

total_round = 1
war_count = 0

while player.still_has_cards() and comp.still_has_cards():
	table_cards = []
	total_round += 1
	print("It'round {}".format(total_round))
	print("standings : {} : {} , {} : {}".format(player.name,player.hand.card_count(),comp.name,comp.hand.card_count()))
	print("Each player has to take one card")
	
	player_card = player.play_card()
	comp_card = comp.play_card()
	# print(comp_card)
	table_cards.append(player_card)
	table_cards.append(comp_card)

	if player_card[1] == comp_card[1]:
		print("It's a war!!")
		print("Each player has to take 3 cards face down and one card face up")
		war_count += 1
		table_cards.extend(player.remove_war_card())
		table_cards.extend(comp.remove_war_card())

		war_card_player = player.play_card()
		war_card_comp = comp.play_card()

		table_cards.append(war_card_player)
		table_cards.append(war_card_comp)

		if RANKS.index(war_card_player[1]) > RANKS.index(war_card_comp[1]):
			print("{} has higher rank card".format(player.name))
			print("{} has lost the round".format(player.name))
			player.hand.add_card(table_cards)

		else:
			print("{} has higher rank card".format(comp.name))
			print("{} has lost the round".format(comp.name))
			comp.hand.add_card(table_cards)

	else:
		if RANKS.index(player_card[1]) > RANKS.index(comp_card[1]):
			print("{} has higher rank card".format(player.name))
			print("{} has lost the round".format(player.name))
			player.hand.add_card(table_cards)

		else:
			print("{} has higher rank card".format(comp.name))
			print("{} has lost the round".format(comp.name))
			comp.hand.add_card(table_cards)

if player.still_has_cards:
	print("{} has won the match".format(player.name))
	print("That match took {} rounds".format(total_round))
else:
	print("{} has won the match".format(comp.name))
	print("That match took {} rounds".format(total_round))	

