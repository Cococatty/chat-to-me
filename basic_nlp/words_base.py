"""
    Perform basic NLP tasks
    - calc_edit_distance
    - pattern_matching
"""

def calc_edit_distance(keyword: str, words: list):
    import editdistance
    result = []
    for record in words:
        dist = editdistance.eval(record, keyword)
        result.append(dist)
        print('Edit Distance for %s and %s is %d' % (record, keyword, dist))

    return result


def pattern_matching(pattern, full_str, surpress=True):
    """Return all matching instances"""
    import requests
    import re
    result = re.findall(pattern, full_str)
    if surpress: 
        result = list(set(result))
    return result
