from team import Team

def suggest_team(
    teams,
    user_skill
):

    matched_teams = []

    for team in teams:

        if (
            user_skill
            in
            team.required_skills
        ):

            matched_teams.append(
                team.team_name
            )

    return matched_teams


if __name__ == "__main__":

    team1 = Team(
        "AI Builders",
        ["Python", "ML"]
    )

    team2 = Team(
        "Design Masters",
        ["UI/UX", "Figma"]
    )

    teams = [team1, team2]

    skill = input(
        "Enter Your Skill: "
    )

    matches = suggest_team(
        teams,
        skill
    )

    print("\nSuggested Teams:")

    for match in matches:

        print(match)