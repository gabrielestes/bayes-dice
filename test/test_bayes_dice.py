from src.bayes_dice import BayesDice

def test_class_works():
    bd = BayesDice()
    assert isinstance(bd, BayesDice)

def test_choose_die():
    bd = BayesDice()
    assert bd.choose_die() in bd.dice

def test_roll_die():
    bd = BayesDice()
    bd.rolldie()
