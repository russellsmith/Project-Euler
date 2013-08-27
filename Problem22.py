"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 * 53 = 49714.

What is the total of all the name scores in the file?
"""

def string_score(string_to_score):
    score = 0
    for s in string_to_score:
        score += ord(s) - 64
        
    return score

if __name__ == "__main__":
    f= open("files/names.txt", 'r')
    names = f.readline()
    names = names.split(',')
    names = [name.replace('"', '') for name in names]
    # Sort names alphabetically
    names.sort()
    
    total_score = 0
    
    for i in xrange(0, len(names)):
        rank = i + 1
        name = names[i]
        score = string_score(name)
        total_score += rank * score

    print 'Total score is %d' % total_score