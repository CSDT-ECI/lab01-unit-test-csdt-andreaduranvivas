from yatzy import Yatzy

# These unit tests can be run using the py.test framework
# available from http://pytest.org/


def test_demo():
        expected = 15
        actual = 15
        assert expected == actual


def test_chance_sumAllDice():
        d1 = 1
        d2 = 1
        d3 = 3
        d4 = 3
        d5 = 6

        expected =  14
        actual = Yatzy.chance(d1, d2, d3, d4, d5)

        assert expected == actual

def test_yatzy_sameNumberDice_fiftyPoints():
        dice = [1, 1, 1, 1, 1]

        expected =  50
        actual = Yatzy.yatzy(dice)

        assert expected == actual

def test_yatzy_differentNumberDice_zeroPoints():
        dice = [1, 1, 1, 2, 1]

        expected =  0
        actual = Yatzy.yatzy(dice)

        assert expected == actual

def test_ones_sumOfOnes():
        dice = [1, 1, 1, 2, 1]

        expected =  4
        actual = Yatzy.ones(dice[0], dice[1], dice[2], dice[3], dice[4])

        assert expected == actual

def test_twos_sumOfTwo():
        dice = [1, 1, 1, 2, 1]

        expected =  2
        actual = Yatzy.twos(dice[0], dice[1], dice[2], dice[3], dice[4])

        assert expected == actual

def test_threes_sumOfThree():
        dice = [1, 1, 1, 3, 3]

        expected =  6
        actual = Yatzy.threes(dice[0], dice[1], dice[2], dice[3], dice[4])

        assert expected == actual

def test_fours_sumOfFour():

        dice = [4,4,4,4,1]
        expected = 16

        game = Yatzy(dice[0], dice[1], dice[2], dice[3], dice[4])

        assert expected == game.fours()

def test_crazyChance_allPairs():

        dice = [2, 4, 6, 2, 2]
        game = Yatzy(dice[0], dice[1], dice[2], dice[3], dice[4])

        expected = 48

        assert expected == game.crazy_chance()


def test_crazyChance_allImpairs():

        dice = [1, 1, 3, 5, 5]
        game = Yatzy(dice[0], dice[1], dice[2], dice[3], dice[4])

        expected = 30

        assert expected == game.crazy_chance()

def test_crazyChance_Mixed():

        dice = [2, 4, 3, 5, 6]
        game = Yatzy(dice[0], dice[1], dice[2], dice[3], dice[4])

        expected = 52

        assert expected == game.crazy_chance()



