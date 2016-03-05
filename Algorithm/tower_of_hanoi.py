#!/usr/bin/python


def test_hanoi(dish_num):
    print "dish number:" + str(dish_num)
    hanoi(dish_num, "first tower", "middle tower", "third tower")


def hanoi(dish_num, from_tower, buffer_tower, to_tower):
    if dish_num == 1:
        print "move dish from " + from_tower + " to " + to_tower
    else:
        hanoi(dish_num - 1, from_tower, to_tower, buffer_tower)
        print "move dish from " + from_tower + " to " + buffer_tower
        hanoi(dish_num - 1, buffer_tower, from_tower, to_tower)