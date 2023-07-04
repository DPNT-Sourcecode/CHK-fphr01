from solutions.CHK import checkout_solution

def test_checkout_with_offer():
    assert checkout_solution.checkout("ABBA") == 145
    
def test_checkout_no_offer():
    assert checkout_solution.checkout("ABA") == 130
    
def test_all_skus():
    assert checkout_solution.checkout("ABCD") == 115
    
def test_illegal_skus():
    assert checkout_solution.checkout("ABBA1") == -1
    
def test_illegal_input():
    assert checkout_solution.checkout(1) == -1
    
    