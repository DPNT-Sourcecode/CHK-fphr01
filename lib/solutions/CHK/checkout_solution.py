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
    skus_present = 
    
def sort_and_list_group_skus(skus: str) -> List[str]
    sorted_skus = "".join(sorted(skus))
    list_of_grouped_skus = []
    current_sku = ""
    for sku in sorted_skus:
        if not current_sku:
            current_sku += sku
            continue
        if sku == current_sku[-1]:
            current_sku += sku
            continue
        list_of_grouped_skus.append(current_sku)
        current_sku = ""
        
    



