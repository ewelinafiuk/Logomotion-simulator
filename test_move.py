from Move import Move
from Paint import Paint
from Turtle import Turtle
import pytest


def test_way_of_move():
    move1 = Move('a', 1)
    move2 = Move('', 0)
    move3 = Move(1, 2)
    assert move1.how_to_move == 'a'
    assert move2.how_to_move == ''
    assert move3.how_to_move == 1


def test_value_of_moving():
    move1 = Move('a', 1)
    move2 = Move('', '')
    move3 = Move(1, '10000')
    assert move1.value_of_move == 1
    assert move2.value_of_move == ''
    assert move3.value_of_move == '10000'


def test_straight_move():
    turtle = Turtle([1, 2], 0)
    move1 = Move('straight', 1)
    move2 = Move('a', 10)
    x = 100
    y = 200
    move1.straight_move(turtle, x, y)
    assert turtle.position == [2, 2]

    move2.straight_move(turtle, x, y)
    assert turtle.position == [12, 2]


def test_straight_exception():
    turtle = Turtle([0, 0], 0)
    move = Move(' ', '[]')
    x = 100
    y = 200
    with pytest.raises(ValueError):
        move.straight_move(turtle, x, y)


def test_turn_move():
    turtle = Turtle([1, 2], 20)
    move1 = Move('turn', 30)

    move2 = Move('a', -10)

    move1.turn_move(turtle)
    assert turtle.turning_now() == 50

    move2.turn_move(turtle)
    assert turtle.turning_now() == 40


def test_turn_exception():
    turtle = Turtle([0, 0], '')
    move = Move(' ', '')
    move.turn_move(turtle)
    assert turtle.turn == ''


def test_movement_straigt():
    turtle = Turtle([1, 2], 0)
    move1 = Move('aaa', 90)

    move1.movement(turtle)
    assert turtle.position == [91, 2]

    move2 = Move('bbb', -10)
    move2.movement(turtle)
    assert turtle.position == [81, 2]

    move3 = Move('', 0)
    move3.movement(turtle)
    assert turtle.position == [81, 2]


def test_movement_turn():
    turtle = Turtle([1, 1], 90)
    move1 = Move('aaa', 10)
    move1.movement(turtle)
    assert int(turtle.position[0]) == 1
    assert int(turtle.position[1]) == 11
    move2 = Move('bbb', -10)
    move2.movement(turtle)
    assert turtle.position == [1, 1]


def test_movement_exception():
    turtle = Turtle(['', ''], '')
    move = Move('aaa', 10)

    with pytest.raises(ValueError):
        move.movement(turtle)


def test_straight_and_paint():
    move1 = Move('naprzod', 10)
    turtle1 = Turtle([10, 10], 0)
    turtle2 = Turtle([10, 20], 90)
    turtle3 = Turtle([0, 0], 45)
    file_to_save = 'new.png'
    x = 100
    y = 100
    paint = Paint(x, y, 'black', 7, file_to_save)

    move1.straight_and_paint(turtle1, paint, x, y)
    assert turtle1.position[0] == 20
    assert turtle1.position[1] == 10

    move1.straight_and_paint(turtle2, paint, x, y)
    assert turtle2.position[0] == 10
    assert turtle2.position[1] == 30

    move1.straight_and_paint(turtle3, paint, x, y)
    assert int(turtle3.position[0]) == 7
    assert int(turtle3.position[1]) == 7


def test_check_if_move_on_background():
    turtle1 = Turtle([10, 10], 0)
    x = 100
    y = 100
    move = Move('a', 0)
    move.check_if_move_on_bacground(turtle1, x, y)
    assert turtle1.position == [10, 10]

    turtle2 = Turtle([200, 100], 0)
    move.check_if_move_on_bacground(turtle2, x, y)
    assert turtle2.position == [100, 100]

    turtle3 = Turtle([-100, 0], 0)
    move.check_if_move_on_bacground(turtle3, x, y)
    assert turtle3.position == [0, 0]
