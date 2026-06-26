from game.score import Score

def test_score_increment():
    score = Score()

    initial = score.get_score()
    score.add_survival()

    assert score.get_score() == initial + 1


def test_score_reset():
    score = Score()
    score.add_survival()
    score.reset()

    assert score.get_score() == 0