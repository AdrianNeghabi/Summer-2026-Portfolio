def calculate_average(scores):
    return sum(scores) / len(scores)


teams = []

while True:
    print("\n===== Robot Competition Score Manager =====")
    print("1. Register Team")
    print("2. View Teams")
    print("3. Update Team Scores")
    print("4. Display Rankings")
    print("5. Remove Team")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        team_name = input("Enter team name: ")
        team_number = input("Enter team number: ")

        design = float(input("Design Score: "))
        programming = float(input("Programming Score: "))
        teamwork = float(input("Teamwork Score: "))

        scores = [design, programming, teamwork]
        average = calculate_average(scores)

        team = {
            "name": team_name,
            "number": team_number,
            "scores": {
                "Design": design,
                "Programming": programming,
                "Teamwork": teamwork
            },
            "average": average
        }

        teams.append(team)
        print("Team registered successfully!")

    elif choice == "2":

        if len(teams) == 0:
            print("No teams registered.")
        else:
            for team in teams:
                print("\n-------------------------")
                print("Team:", team["name"])
                print("Number:", team["number"])
                print("Average Score:", round(team["average"], 2))

    elif choice == "3":

        number = input("Enter team number: ")

        found = False

        for team in teams:
            if team["number"] == number:

                print("Enter new scores:")

                design = float(input("Design Score: "))
                programming = float(input("Programming Score: "))
                teamwork = float(input("Teamwork Score: "))

                team["scores"]["Design"] = design
                team["scores"]["Programming"] = programming
                team["scores"]["Teamwork"] = teamwork

                team["average"] = calculate_average(
                    [design, programming, teamwork]
                )

                print("Scores updated!")
                found = True
                break

        if not found:
            print("Team not found.")

    elif choice == "4":

        if len(teams) == 0:
            print("No teams registered.")
        else:
            rankings = sorted(
                teams,
                key=lambda team: team["average"],
                reverse=True
            )

            print("\n===== Competition Rankings =====")

            place = 1

            for team in rankings:
                print(
                    f"{place}. {team['name']} - {round(team['average'],2)}"
                )
                place += 1

    elif choice == "5":

        number = input("Enter team number to remove: ")

        found = False

        for team in teams:
            if team["number"] == number:
                teams.remove(team)
                print("Team removed.")
                found = True
                break

        if not found:
            print("Team not found.")

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")