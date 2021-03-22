

def save_match(match, filename, player1, player2):
    matches_file = open(filename, 'w')
    player_array = [player1, player2]

    for player in player_array:
        matches_file.write('[\n')
        player.compile()

        for var in player.toText:
            matches_file.write(f'{var} - {player.toText[var]}\n')
        matches_file.write(']\n')

    match.compile()

    matches_file.write('(\n')
    for item in match.toText:
        matches_file.write(f'{item} - {match.toText[item]}\n')
    matches_file.write(')\n')

    for set_played in match.data:

        set_played.compile()

        matches_file.write('(\n')
        for item in set_played.toText:
            matches_file.write(f'{item} - {set_played.toText[item]}\n')
        matches_file.write('(\n')

        for game in set_played.data:

            game.compile()

            matches_file.write('(\n')
            for item in game.toText:
                matches_file.write(f'{item} - {game.toText[item]}\n')
            matches_file.write('(\n')

            for point in game.data:

                point.compile()

                for item in point.toText:
                    matches_file.write(f'{item} - {point.toText[item]}\n')

                matches_file.write('-\n')
            matches_file.write('--\n')
        matches_file.write('---\n')
    matches_file.write('----\n')

    matches_file.close()
