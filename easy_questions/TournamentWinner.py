def tournamentWinner(competitions:list, results:list):
    res = {}
    for idx, winner in enumerate(results):
        winner = not(winner)
        res[competitions[idx][winner]] =  res[competitions[idx][winner]] + 3 if res.get(competitions[idx][winner]) else 3
    return max(res, key=res.get)


if __name__ == '__main__':
    assert tournamentWinner([
  ["HTML", "C#"],
  ["C#", "Python"],
  ["Python", "HTML"]
], [0, 0, 1]) == 'Python'