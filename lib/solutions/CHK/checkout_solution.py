# noinspection PyUnusedLocal
# skus = unicode string
from typing import List
PRICES = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
}

# tuple with quantity required and offer price
OFFERS = {
    "A": (3, 130),
    "B": (2, 45)
    }

def checkout(skus:str) -> int:
    skus_present = set(skus) 
    if not isinstance(skus, str) or not set(skus).issubset(PRICES):
        return -1
    
    value = 0
    
    for item in skus_present:
        quantity_of_item = skus.count(item)
        if item in OFFERS:
            required_quantity = OFFERS[item][0]
            offer_quantity, single_quantity = divmod(quantity_of_item, required_quantity)
            
            value += offer_quantity*OFFERS[item][1]
            value += offer_quantity*PRICES[item][1]
            



