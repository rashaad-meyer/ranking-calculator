import unittest
from collections import defaultdict
from io import StringIO
import sys
from main import process_input, sort_teams, assign_ranks, generate_output

class TestLeagueRanking(unittest.TestCase):
    def test_process_input(self):
        lines = [
            "Team A 3, Team B 1",
            "Team C 2, Team A 2",
            "Team B 0, Team C 1",
        ]
        expected = {"Team A": 4, "Team B": 0, "Team C": 4}
        self.assertEqual(process_input(lines), expected)

    def test_sort_teams(self):
        team_points = {"Team A": 4, "Team B": 0, "Team C": 4}
        expected = [("Team A", 4), ("Team C", 4), ("Team B", 0)]  # Sorted alphabetically when points are equal
        self.assertEqual(sort_teams(team_points), expected)

    def test_assign_ranks(self):
        sorted_teams = [("Team A", 4), ("Team C", 4), ("Team B", 0)]
        expected = [(1, "Team A", 4), (1, "Team C", 4), (3, "Team B", 0)]  # Team A and C are tied, so same rank
        self.assertEqual(assign_ranks(sorted_teams), expected)

    def test_generate_output(self):
        rankings = [(1, "Team A", 4), (1, "Team C", 4), (3, "Team B", 0)]
        expected_output = '\n'.join([
            '1. Team A, 4 pts',
            '1. Team C, 4 pts',
            '3. Team B, 0 pts'
        ])
        self.assertEqual(generate_output(rankings), expected_output)

if __name__ == "__main__":
    unittest.main()
