import sys
from collections import defaultdict

def process_input(lines):
    team_points = defaultdict(int)
    for line in lines:
        line = line.strip()
        if not line:
            continue
        parts = line.split(', ')
        if len(parts) != 2:
            continue  # Skip invalid lines
        try:
            # Split each team part into name and score
            team1_str, team2_str = parts
            team1_name, team1_score = team1_str.rsplit(' ', 1)
            team1_score = int(team1_score)
            team2_name, team2_score = team2_str.rsplit(' ', 1)
            team2_score = int(team2_score)
        except ValueError:
            continue  # Skip invalid formats

        # Update points based on match outcome
        if team1_score > team2_score:
            team_points[team1_name] += 3
            team_points[team2_name] += 0
        elif team1_score == team2_score:
            team_points[team1_name] += 1
            team_points[team2_name] += 1
        else:
            team_points[team1_name] += 0
            team_points[team2_name] += 3
    return team_points

def sort_teams(team_points):
    # Sort by descending points, then ascending team name
    return sorted(team_points.items(), key=lambda x: (-x[1], x[0]))

def assign_ranks(sorted_teams):
    if not sorted_teams:
        return []
    rankings = []
    current_group_points = None
    current_group_start = 0
    for index, (team, points) in enumerate(sorted_teams):
        if points != current_group_points:
            current_group_points = points
            current_group_start = index
        rankings.append((current_group_start + 1, team, points))
    return rankings

def generate_output(rankings):
    output = []
    for rank, team, points in rankings:
        pt_str = 'pt' if points == 1 else 'pts'
        output.append(f"{rank}. {team}, {points} {pt_str}")
    return '\n'.join(output)

def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as f:
            lines = f.readlines()
    else:
        lines = sys.stdin.read().splitlines()
    team_points = process_input(lines)
    sorted_teams = sort_teams(team_points)
    rankings = assign_ranks(sorted_teams)
    print(generate_output(rankings))

if __name__ == "__main__":
    main()