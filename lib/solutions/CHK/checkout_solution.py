# noinspection PyUnusedLocal
# skus = unicode string
PRICES = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
    "E": 40,
}

# tuple with quantity required and offer price
OFFERS = {
    "A": {3: 130, 5: 200},
    "B": {2: 45},
    }

FREE_OFFERS = {
    "E": {2: "B"}
}

def checkout(skus:str) -> int:
    if not isinstance(skus, str) or not set(skus).issubset(PRICES):
        return -1
    
    skus_present_count = { item: skus.count(item) for item in skus }

    value = 0
    for item in FREE_OFFERS.keys():
        if item in skus_present_count:
            for required_offer_num in sorted(FREE_OFFERS[item], reverse=True):
                
                if isinstance(FREE_OFFERS[item][required_offer_num],str):
                    free_sku = FREE_OFFERS[item][required_offer_num]
                    while skus_present_count[item]>= required_offer_num:
                        skus_present_count[free_sku] = max(0, skus_present_count.get(free_sku, 0)-1)
                        value += required_offer_num * PRICES[item]
                        skus_present_count[item] -= required_offer_num
                        
    for item in OFFERS.keys():
        if item in skus_present_count:
            for required_offer_num in sorted(OFFERS[item], reverse=True):
                
                if isinstance(OFFERS[item][required_offer_num],int):
                    while skus_present_count[item]>= required_offer_num:
                        print(skus_present_count)
                        value += OFFERS[item][required_offer_num]
                        skus_present_count[item] -= required_offer_num
                        
    for sku, count in skus_present_count.items():
        value += PRICES[sku]*count
            
            
    return value
