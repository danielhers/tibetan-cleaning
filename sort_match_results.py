from operator import itemgetter

def sort_matches(matches_file):
    line_scores = get_sorted_lines(matches_file)
    matches = open(matches_file, 'w')
    for match in line_scores:
        matches.write(match[0])
    matches.close()

def get_sorted_lines(matches_file):
    matches = open(matches_file, 'r')
    line_scores = []
    for line in matches:
        score = float(line.split(',')[4][:-1])
        line_scores.append((line, score))
    line_scores = sorted(line_scores, key=itemgetter(1), reverse=True)
    matches.close()
    return line_scores



if __name__ == '__main__':
    sort_matches(r'C:\Results\Tibet\test2_enum_stem')

