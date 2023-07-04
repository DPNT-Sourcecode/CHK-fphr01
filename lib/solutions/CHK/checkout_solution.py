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
    "A": {3: 130, 5: 200},
    "B": {2: 45},
    "E": {2: "B"}
    }

def checkout(skus:str) -> int:
    if not isinstance(skus, str) or not set(skus).issubset(PRICES):
        return -1
    
    skus_present_count = { item: skus.count(item) for item in set(skus) }

    
    value = 0
    for item in OFFERS.keys():
        if item in skus_present_count:
            for required_offer_num in sorted(OFFERS[item], reverse=True):
                if isinstance(OFFERS[item][required_offer_num],str):
                    free_sku = OFFERS[item][required_offer_num]
                    while skus_present_count[item]>= required_offer_num:
                        skus_present_count[free_sku] = max(0, skus_present_count.get(free_sku, 0)-1)
                        skus_present_count[item] -= required_offer_num
            
                

            
        else:
            
    return value
            

        # quantity_of_item = skus.count(item)
        # if item in OFFERS:
        #     required_quantity = OFFERS[item][0]
        #     offer_quantity, single_quantity = divmod(quantity_of_item, required_quantity)
            
        #     value += offer_quantity*OFFERS[item][1]
        #     value += single_quantity*PRICES[item]




