class Team:

    def __init__(
        self,
        team_name,
        required_skills
    ):

        self.team_name = team_name

        self.required_skills = required_skills

        self.members = []

    def add_member(
        self,
        member_name,
        skill
    ):

        self.members.append({
            "name": member_name,
            "skill": skill
        })

    def display_team(self):

        print(
            f"\nTeam: {self.team_name}"
        )

        print(
            "Required Skills:",
            ", ".join(self.required_skills)
        )

        print("\nMembers:")

        for member in self.members:

            print(
                f"{member['name']} "
                f"- "
                f"{member['skill']}"
            )


if __name__ == "__main__":

    team = Team(
        "Code Warriors",
        ["Python", "UI/UX"]
    )

    team.add_member(
        "Sujal",
        "Python"
    )

    team.display_team()