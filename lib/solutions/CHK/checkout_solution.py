# noinspection PyUnusedLocal
# skus = unicode string
PRICES = {
    "A": "50",
    "B": "30",
    "C": "20",
    "D": "15",
    "E": "40",
    "F": "10",
    "G": "20",
    "H": "10",
    "I": "35",
    "J": "60",
    "K": "70",
    "L": "90",
    "M": "15",
    "N": "40",
    "O": "10",
    "P": "50",
    "Q": "30",
    "R": "50",
    "S": "20",
    "T": "20",
    "U": "40",
    "V": "50",
    "W": "20",
    "X": "17",
    "Y": "20",
    "Z": "21",
}
# tuple with quantity required and offer price
OFFERS = {
    "A": {3: 130, 5: 200},
    "B": {2: 45},
    "F": {3: 20},
    "H": {5:45, 10:80},
    "K": {2:120},
    "P": {5: 200},
    "Q": {3:80},
    "U": {4: 120},
    "V": {2: 90, 3: 130},
    }

FREE_OFFERS = {
    "E": {2: "B"},
    "N": {3: "M"},
    "R": {3: "Q"},
    }

GROUP_OFFERS = {
    "STXYZ" : [3, 45]
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
                        
    skus_present_count = delete_empty_counts(skus_present_count)
    
    for group in GROUP_OFFERS.keys():
        quantity_required = GROUP_OFFERS[group][0]
        offer_price = GROUP_OFFERS[group][1]

        valid_for_group_offer_count = []
        for sku in group:
            valid_for_group_offer_count.append([sku,skus_present_count.get(sku, 0), PRICES[sku]])
        # sort list to prioritise higher value items
        sorted_list = sorted(valid_for_group_offer_count, key=lambda x: x[2], reverse=True)
        
        group_items = ""
        counter = 0
        for sku_list in sorted_list:
            sku_list_quantity = sku_list[1]
            while len(group_items) <= quantity_required and len(group_items) <= sku_list_quantity:
                if counter ==quantity_required:
                    value += offer_price
                    for item in group_items:
                        skus_present_count[item] -= 1
                    counter = 0
                for 
                    
    for item in OFFERS.keys():
        if item in skus_present_count:
            for required_offer_num in sorted(OFFERS[item], reverse=True):
                
                if isinstance(OFFERS[item][required_offer_num],int):
                    while skus_present_count[item]>= required_offer_num:
                        value += OFFERS[item][required_offer_num]
                        skus_present_count[item] -= required_offer_num
                        
    for sku, count in skus_present_count.items():
        value += PRICES[sku]*count
            
            
    return value

def delete_empty_counts(count_dict: dict) -> dict:
    del_keys= []
    for key, value in count_dict.items():
        if value == 0:
            del_keys.append(key)
    for key in del_keys:
        count_dict.pop(key)
        
    return count_dict







