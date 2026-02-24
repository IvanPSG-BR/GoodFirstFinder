import pytest

from app.modules.scoring.services import calculate_total_score


class TestCalculateTotalScore:
    def test_default_weights(self):
        score = calculate_total_score(
            documentation=8.0,
            community=6.0,
            activity=7.0,
            beginner_friendliness=9.0,
        )
        expected = round(8.0 * 0.30 + 6.0 * 0.25 + 7.0 * 0.20 + 9.0 * 0.25, 2)
        assert score == expected

    def test_score_clamped_to_max_10(self):
        score = calculate_total_score(10.0, 10.0, 10.0, 10.0)
        assert score == 10.0

    def test_score_clamped_to_min_0(self):
        score = calculate_total_score(-5.0, -5.0, -5.0, -5.0)
        assert score == 0.0

    def test_custom_weights(self):
        weights = {
            "documentation": 0.25,
            "community": 0.25,
            "activity": 0.25,
            "beginner_friendliness": 0.25,
        }
        score = calculate_total_score(4.0, 4.0, 4.0, 4.0, weights=weights)
        assert score == 4.0

    def test_zero_scores(self):
        score = calculate_total_score(0.0, 0.0, 0.0, 0.0)
        assert score == 0.0
