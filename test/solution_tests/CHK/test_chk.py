from solutions.CHK import checkout_solution


def test_checkout_with_offer():
    assert checkout_solution.checkout("ABBA") == 145


def test_checkout_no_offer():
    assert checkout_solution.checkout("ABA") == 130


def test_checkout_all_with_free_offer_no_bogof():
    # 3A for 130, 5A for 200 = 330
    # 2B for 45 = 375
    # 2E for 80 , 1B for 0 = 455
    # 1C for 20 = 475
    # 1B for 30 = 505
    assert checkout_solution.checkout("ABABABBAAAAAEEC") == 505


def test_checkout_all_with_free_offer_with_bogof():
    # 3A for 130, 5A for 200 = 330
    # 2B for 45 = 375
    # 2E for 80 , 1B for 0 = 455
    # 1C for 20 = 475
    # 1B for 30 = 505
    # 3F for 20 = 525
    assert checkout_solution.checkout("ABAFBAFBBAAFAAAEEC") == 525


def test_multi_buy_free_offer():
    assert checkout_solution.checkout("BEBEEE") == 160


def test_no_bogof():
    assert checkout_solution.checkout("FF") == 20


def test_offers_with_no_bogof():
    assert checkout_solution.checkout("ABCDEFABCDEF") == 300


def test_new_additions_to_skus():
    # 525 + RRRQ(150) + Q(30) + UUUU(120) + U(40) + Z(21)

    assert checkout_solution.checkout("ABAFBAFBBAAFAAAEECRRRQQUUUUUZ") == 886


def test_group_deal():
    assert checkout_solution.checkout("STXYZ") == 82


def test_group_deal_multiple():
    assert checkout_solution.checkout("ZZYSTX") == 90


def test_all_skus():
    assert checkout_solution.checkout("ABCD") == 115


def test_illegal_skus():
    assert checkout_solution.checkout("ABBA1") == -1


def test_illegal_input():
    assert checkout_solution.checkout(1) == -1
