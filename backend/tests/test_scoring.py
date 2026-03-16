from app.engine.scoring import score, is_farkle, is_hot_dice

def test_single_one_scores_100():
    assert score([1]) == 100

def test_single_five_scores_50():
    assert score([5]) == 50

def test_two_ones_scores_200():
    assert score([1, 1]) == 200

def test_two_fives_scores_100():
    assert score([5, 5]) == 100

def test_three_ones_scores_1000():
    assert score([1, 1, 1]) == 1000

def test_three_twos_scores_200():
    assert score([2, 2, 2]) == 200

def test_three_threes_scores_300():
    assert score([3, 3, 3]) == 300

def test_three_fours_scores_400():
    assert score([4, 4, 4]) == 400

def test_three_fives_scores_500():
    assert score([5, 5, 5]) == 500

def test_three_sixes_scores_600():
    assert score([6, 6, 6]) == 600

def test_four_ones_scores_1000():
    assert score([1, 1, 1, 1]) == 1000

def test_four_twos_scores_1000():
    assert score([2, 2, 2, 2]) == 1000

def test_four_threes_scores_1000():
    assert score([3, 3, 3, 3]) == 1000
    
def test_four_fours_scores_1000():
    assert score([4, 4, 4, 4]) == 1000
    
def test_four_fives_scores_1000():
    assert score([5, 5, 5, 5]) == 1000
    
def test_four_sixes_scores_1000():
    assert score([6, 6, 6, 6]) == 1000

def test_five_ones_scores_2000():
    assert score([1, 1, 1, 1, 1]) == 2000

def test_five_twos_scores_2000():
    assert score([2, 2, 2, 2, 2]) == 2000

def test_five_threes_scores_2000():
    assert score([3, 3, 3, 3, 3]) == 2000
    
def test_five_fours_scores_2000():
    assert score([4, 4, 4, 4, 4]) == 2000
    
def test_five_fives_scores_2000():
    assert score([5, 5, 5, 5, 5]) == 2000
    
def test_five_sixes_scores_2000():
    assert score([6, 6, 6, 6, 6]) == 2000

def test_six_ones_scores_3000():
    assert score([1, 1, 1, 1, 1, 1]) == 3000

def test_six_twos_scores_3000():
    assert score([2, 2, 2, 2, 2, 2]) == 3000

def test_six_threes_scores_3000():
    assert score([3, 3, 3, 3, 3, 3]) == 3000
    
def test_six_fours_scores_3000():
    assert score([4, 4, 4, 4, 4, 4]) == 3000
    
def test_six_fives_scores_3000():
    assert score([5, 5, 5, 5, 5, 5]) == 3000
    
def test_six_sixes_scores_3000():
    assert score([6, 6, 6, 6, 6, 6]) == 3000

def test_straight_scores_1500():
    assert score([1, 2, 3, 4, 5, 6]) == 1500

def test_four_of_a_kind_and_pair_scores_1500():
    assert score([2, 2, 2, 2, 6, 6]) == 1500

def test_three_pairs_scores_1500():
    assert score([2, 2, 3, 3, 4, 4]) == 1500
    assert score([1, 1, 2, 2, 3, 3]) == 1500
    assert score([1, 1, 3, 3, 5, 5]) == 1500
    assert score([1, 1, 2, 2, 4, 4]) == 1500

def test_two_triplets_scores_2500():
    assert score([3, 3, 3, 4, 4, 4]) == 2500

def test_combination_scores():
    assert score([2, 2, 5, 5, 2, 1]) == 400
    assert score([2, 2, 2, 2, 1]) == 1100
    assert score([1, 1, 1, 1, 5]) == 1050
    assert score([3, 3, 3, 3, 3, 1]) == 2100
    assert score([5, 5, 5, 1]) == 600
    assert score([2, 2, 2, 2, 2, 6]) == 2000

def test_is_farkle():
    assert is_farkle([3]) == True
    assert is_farkle([4, 4]) == True
    assert is_farkle([2, 3, 4]) == True
    assert is_farkle([3, 4, 6, 2]) == True
    assert is_farkle([1]) == False
    assert is_farkle([4, 4, 3, 3, 2, 2]) == False
    assert is_farkle([1, 4, 4]) == False
    assert is_farkle([1, 1, 5, 5, 6, 6]) == False

def test_is_hot_dice():
    assert is_hot_dice([1, 1, 1, 5, 5, 5]) == True
    assert is_hot_dice([1, 1, 1, 1, 1, 1]) == True
    assert is_hot_dice([1, 1, 5, 2, 2, 2]) == True
    assert is_hot_dice([2, 2, 5, 5, 2, 1]) == True
    assert is_hot_dice([2, 2, 5, 5, 4, 3]) == False
    assert is_hot_dice([3, 3, 3, 5, 5, 4]) == False
    assert is_hot_dice([1, 1, 1, 1, 1, 2]) == False