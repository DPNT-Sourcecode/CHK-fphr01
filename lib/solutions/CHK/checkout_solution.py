PRICES = {
    "A": 50,
    "AAA":130,
    "B": 30,
    "BB": 45,
    "C": 20,
    "D": 15,
}
# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus:str) -> int:
    sorted_skus = "".join(sorted(skus))
    list_of_grouped_skus = []
    current_sku = ""
    for sku in sorted_skus:
        if not current_sku:
            current_sku += sku
    
