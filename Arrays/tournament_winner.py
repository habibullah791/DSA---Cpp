HOME_TEAM_WON = 1


def tournamentWinner(competitions, results):
    currentBestTeam = ""
    scores = {currentBestTeam: 0}

    # ["HTML", "C#"],
    # ["C#", "Python"],
    # ["Python", "HTML"]
    for idx, competition in enumerate(competitions):
        print(idx)
        result = results[idx]
        HomeTeam, AwayTeam = competition

        WinningTeam = HomeTeam if result == HOME_TEAM_WON else AwayTeam

        if WinningTeam not in scores:
            scores[WinningTeam] = 3
        else:
            scores[WinningTeam] += 3

        if scores[WinningTeam] > scores[currentBestTeam]:
            currentBestTeam = WinningTeam

    return currentBestTeam


competitions = [
    ["HTML", "Java"],
    ["Java", "Python"],
    ["Python", "HTML"],
    ["C#", "Python"],
    ["Java", "C#"],
    ["C#", "HTML"],
]
results = [0, 1, 1, 1, 0, 1]

print(tournamentWinner(competitions, results))
