"""Tests for calculations"""

import pytest
from regenslangen.calculations import get_dice_count_scores


@pytest.mark.parametrize(
    "test, expected",
    [
        (
            ["13133251", "31P53313", "3522233P"],
            [
                (1, "1", 3, 3),
                (1, "3", 3, 9),
                (1, "2", 1, 2),
                (1, "5", 1, 5),
                (2, "3", 4, 12),
                (2, "1", 2, 2),
                (2, "P", 1, 5),
                (2, "5", 1, 5),
                (3, "3", 3, 9),
                (3, "5", 1, 5),
                (3, "2", 3, 6),
                (3, "P", 1, 5),
            ],
        ),
        (
            ["233422P4", "52533424", "PP21241P"],
            [
                (1, "2", 3, 6),
                (1, "3", 2, 6),
                (1, "4", 2, 8),
                (1, "P", 1, 5),
                (2, "5", 2, 10),
                (2, "2", 2, 4),
                (2, "3", 2, 6),
                (2, "4", 2, 8),
                (3, "P", 3, 15),
                (3, "2", 2, 4),
                (3, "1", 2, 2),
                (3, "4", 1, 4),
            ],
        ),
    ],
)
def test_dice_count_scores(test, expected):
    """Test that dice_count_score fun works for two inputs."""

    assert get_dice_count_scores(test) == expected
