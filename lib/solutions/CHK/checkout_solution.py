# noinspection PyUnusedLocal
# skus = unicode string
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
    if not isinstance(skus, str) or not set(skus).issubset(PRICES):
        return -1
    
    skus_present = set(skus) 

    value = 0
    
    for item in skus_present:
        quantity_of_item = skus.count(item)
        if item in OFFERS:
            required_quantity = OFFERS[item][0]
            offer_quantity, single_quantity = divmod(quantity_of_item, required_quantity)
            
            value += offer_quantity*OFFERS[item][1]
            value += single_quantity*PRICES[item]
            
        else:
            value += quantity_of_item*PRICES[item]
            
    return value
            
