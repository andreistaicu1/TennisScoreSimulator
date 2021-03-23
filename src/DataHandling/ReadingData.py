from src.Classes.TennisMatch import *
from src.Classes.Players import *


def split_text(text, split_char):
    text_array = [[]]
    current_item = 0

    for line in text:

        if line == split_char:
            text_array.append([])
            current_item += 1

        else:
            text_array[current_item].append(line)

    text_array.pop()

    return text_array


def get_between_char(text, char_start, char_end):

    start = -1

    for index in range(len(text)):

        if text[index] == char_start:
            if start == -1:
                start = index

        elif text[index] == char_end:
            if start != -1:
                end = index
                return text[start + 1:end], end

    return [], 0


def read_player(text_array):

    recompile = {}
    for line in text_array:
        fragment = line.split()
        recompile[fragment[0]] = fragment[2]

    new_player = Players(recompile['name'], float(recompile['first_percentage']), float(recompile['double_fault']),
                         float(recompile['ace']), float(recompile['first_serve_pts_won']),
                         float(recompile['second_serve_pts_won']), float(recompile['first_return_pts_won']),
                         float(recompile['second_return_pts_won']))

    return new_player


def read_point(text_array):
    recompile = {}
    for line in text_array:
        fragment = line.split()
        if len(fragment) > 2:
            recompile[fragment[0]] = fragment[2]

    new_point = TennisPoint()

    new_point.iterate_point(recompile)

    return new_point


def read_game(text_array, ad, player1, player2):
    game_metadata, end = get_between_char(text_array, '(', ')')

    recompile = {}
    for line in game_metadata:
        fragment = line.split()
        recompile[fragment[0]] = fragment[2]

    points_text = split_text(text_array[end:], '-')
    points = []

    for point_text in points_text:
        points.append(read_point(point_text))

    if len(recompile) == 2:
        item = TennisTiebreak(player1, player2, points[0].serving, int(recompile['tiebreak_length']))
        for point in points:
            item.iterate_breaker(point)

    else:
        item = TennisGame(player1, player2, points[0].serving, ad)
        for point in points:
            item.iterate_game(point)

    return item, type(item)


def read_set(text_array, ad, set_length, player1, player2):
    set_metadata, end = get_between_char(text_array, '(', ')')

    recompile = {}
    for line in set_metadata:
        fragment = line.split()
        recompile[fragment[0]] = fragment[2]

    games_text = split_text(text_array[end:], '--')
    games_type = []

    for game_text in games_text:
        games_type.append(read_game(game_text, ad, player1, player2))

    current_set = TennisSet(set_length, player1, player2, ad, bool(recompile['serving']),
                            bool(recompile['will_breaker']))

    for game, thing in games_type:
        if thing == TennisGame:
            current_set.iterate_set_game(game)
        else:
            current_set.iterate_set_breaker(game)

    return current_set


def read_match(text_array):
    end = 0

    player1_text, more = get_between_char(text_array[end:], '[', ']')
    end += more

    player2_text, more = get_between_char(text_array[end:], '[', ']')
    end += more

    match_metadata, more = get_between_char(text_array[end:], '(', ')')
    end += more

    player1 = read_player(player1_text)
    player2 = read_player(player2_text)

    recompile = {}
    for line in match_metadata:
        fragments = line.split()
        recompile[fragments[0]] = fragments[2]

    sets_text = split_text(text_array[end:], '---')
    sets = []

    for set_text in sets_text:
        sets.append(read_set(set_text, bool(recompile['ad']), int(recompile['set_length']), player1, player2))

    match = TennisMatch(player1, player2, int(recompile['to_win']), bool(recompile['serving']),
                        int(recompile['set_length']), bool(recompile['ad']), bool(recompile['final_set_breaker']))

    for set_played in sets:
        match.iterate_match(set_played)

    return match


def pull_data(filename):
    """
    :param filename: string - directing to a txt. file
    :return: an array of TennisMatch objects
    """
    matches_array = []
    text_array = [[]]

    matches_to_read = open(filename, 'r')
    current_match = 0

    for raw_line in matches_to_read:

        line = raw_line.split('\n')[0]

        if line == '----':
            text_array.append([])
            current_match += 1

        else:
            text_array[current_match].append(line)

    text_array.pop()

    for text_match in text_array:
        matches_array.append(read_match(text_match))

    return matches_array
