#!/usr/bin/python3
# MCS.py -- Returns basic card info about a specifed string.
import json
import requests

scryfall_link = 'https://api.scryfall.com/cards/named?fuzzy='
mtg_card = input()

class Card:
	def __init__(self, name, card_type, mana_cost, oracle_text, rarity, from_set, legal_in, price):
		self.name = name
		self.card_type = card_type
		self.mana_cost = mana_cost
		self.oracle_text = oracle_text
		self.rarity = rarity
		self.from_set = from_set
		self.legal_in = legal_in
		self.price = price

	def display(self): 
		print('[' + self.name + ']')
		print('Type: ' + self.card_type)
		
		if 'Land' not in self.card_type:
			print('Cost: ' + self.mana_cost)

		print(self.oracle_text)
		print('Rarity: ' + self.rarity)
		print('Set: ' + self.from_set)
		print('Modern: ' + self.legal_in['modern'])
		print('Standard: ' + self.legal_in['standard'])
		print('Pauper: ' + self.legal_in['pauper'])

		if self.price['usd'] is None:
			self.price = 'Unavailable'
		
		else:
			self.price = '$' + self.price['usd']	

		print('Price: ' + self.price)

resp = requests.get(scryfall_link + mtg_card)
resp_obj = resp.json()

if resp_obj['object'] == 'error':
	print(resp_obj['details'])

else:
	card = Card(resp_obj['name'], resp_obj['type_line'], resp_obj['mana_cost'], resp_obj['oracle_text'], resp_obj['rarity'], resp_obj['set_name'], resp_obj['legalities'], resp_obj['prices'])		
	card.display()
