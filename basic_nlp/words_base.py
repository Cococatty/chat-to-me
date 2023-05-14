"""
    Perform basic NLP tasks
"""

def calc_edit_distance(keyword: str, words: list):
    import editdistance
    result = []
    for record in words:
        dist = editdistance.eval(record, keyword)
        result.append(dist)
        print('Edit Distance for %s and %s is %d' % (record, keyword, dist))

    return result
