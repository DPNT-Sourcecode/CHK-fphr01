from solutions.CHK import checkout_solution

def test_checkout_with_offer():
    assert checkout_solution.checkout("ABBA") == 145
    
def test_checkout_no_offer():
    assert checkout_solution.checkout("ABA") == 130
    
def test_checkout_all_with_free_offer():
    # 3A for 130, 5A for 200 = 330
    # 2B for 45 = 375
    # 2E for 80 , 1B for 0 = 455
    # 1C for 20 = 475
    # 1B for 30 = 505
    assert checkout_solution.checkout("ABABABBAAAAAEEC") == 505
    
def test_all_skus():
    assert checkout_solution.checkout("ABCD") == 115
    
def test_illegal_skus():
    assert checkout_solution.checkout("ABBA1") == -1
    
def test_illegal_input():
    assert checkout_solution.checkout(1) == -1
    
    