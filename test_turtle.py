from Turtle import Turtle


def test_initial_value():
    obj_1 = Turtle([1, 2], 3)
    obj_2 = Turtle([-11, 'a'], 'a')
    obj_3 = Turtle(None, None)
    assert obj_1.position == [1, 2]
    assert obj_1.turn == 3
    assert obj_2.position == [-11, 'a']
    assert obj_2.turn == 'a'
    assert obj_3.position == [0, 0]
    assert obj_3.turn == 0


def test_position_now():
    obj_1 = Turtle([1, 2], 3)
    obj_2 = Turtle([-11, 'a'], 'a')
    obj_3 = Turtle(None, None)
    assert obj_1.position_now()[0] == 1
    assert obj_1.position_now()[1] == 2
    assert obj_2.position_now()[0] == '-11'
    assert obj_2.position_now()[1] == 'a'
    assert obj_3.position_now()[0] == 0
    assert obj_3.position_now()[1] == 0


def test_turning_now():
    obj_1 = Turtle([1, 2], 3)
    obj_2 = Turtle([-11, 'a'], 'a')
    obj_3 = Turtle(None, None)
    assert obj_1.turning_now() == 3
    assert obj_2.turning_now() == 'a'
    assert obj_3.turning_now() == 0
