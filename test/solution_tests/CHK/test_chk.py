from solutions.CHK import checkout_solution

def test_checkout():
    assert checkout_solution.checkout("ABBA") == 145
    
def test_illegal_skus():
    assert checkout_solution.checkout("ABBA1") == -1
    
def test_illegal_input():
    assert checkout_solution.checkout(1) == -1
    
    