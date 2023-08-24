class FlightTable:
    def __init__(self):
        self.matches = []

    def add_match(self, location, team1, team2, timing):
        self.matches.append({
            'Location': location,
            'Team 01': team1,
            'Team 02': team2,
            'Timing': timing
        })

    def list_matches_by_team(self, team):
        matches_by_team = []
        for match in self.matches:
            if match['Team 01'] == team or match['Team 02'] == team:
                matches_by_team.append(match)
        return matches_by_team

    def list_matches_by_location(self, location):
        matches_by_location = []
        for match in self.matches:
            if match['Location'] == location:
                matches_by_location.append(match)
        return matches_by_location

    def list_matches_by_timing(self, timing):
        matches_by_timing = []
        for match in self.matches:
            if match['Timing'] == timing:
                matches_by_timing.append(match)
        return matches_by_timing

def main():
    flight_table = FlightTable()

    # Adding matches to the flight table
    flight_table.add_match("Mumbai", "India", "Sri Lanka", "DAY")
    flight_table.add_match("Delhi", "England", "Australia", "DAY-NIGHT")
    flight_table.add_match("Chennai", "India", "South Africa", "DAY")
    flight_table.add_match("Indore", "England", "Sri Lanka", "DAY-NIGHT")
    flight_table.add_match("Mohali", "Australia", "South Africa", "DAY-NIGHT")
    flight_table.add_match("Delhi", "India", "Australia", "DAY")

    while True:
        print("\nChoose a search parameter:")
        print("1. List of all the matches of a Team")
        print("2. List of Matches on a Location")
        print("3. List of Matches based on timing")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            team = input("Enter the team name: ")
            matches = flight_table.list_matches_by_team(team)
        elif choice == '2':
            location = input("Enter the location: ")
            matches = flight_table.list_matches_by_location(location)
        elif choice == '3':
            timing = input("Enter the timing: ")
            matches = flight_table.list_matches_by_timing(timing)
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
            continue

        if not matches:
            print("No matches found.")
        else:
            print("\nMatch Details:")
            for match in matches:
                print(f"Location: {match['Location']}")
                print(f"Team 01: {match['Team 01']}")
                print(f"Team 02: {match['Team 02']}")
                print(f"Timing: {match['Timing']}")
                print()

if __name__ == "__main__":
    main()
