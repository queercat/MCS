#!/usr/bin/python3
# MCS.py -- Returns basic card info about a specifed string.
import json
import requests

scryfall_link = 'https://api.scryfall.com/cards/named?fuzzy='
mtg_card = input()

class Card:
	def __init__(self, name, card_type, mana_cost, oracle_text, price):
		self.name = name
		self.card_type = card_type
		self.mana_cost = mana_cost
		self.oracle_text = oracle_text
		self.price = price

	def display(self): 
		print('[' + self.name + ']')
		print(self.card_type)
		
		if 'Land' not in self.card_type:
			print(self.mana_cost)

		print(self.oracle_text)
		print('$' + self.price)

resp = requests.get(scryfall_link + mtg_card)
resp_obj = resp.json()

if resp_obj['object'] is 'error':
	print(resp_obj['details'])

else:
	card = Card(resp_obj['name'], resp_obj['type_line'], resp_obj['mana_cost'], resp_obj['oracle_text'], resp_obj['usd'])		
	card.display()
