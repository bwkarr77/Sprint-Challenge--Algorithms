'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word, count=0):
    # TBC
    n = len(word)
    # print('word: ', word, n, count)
    if (n > 0):
        if (word[0] == "t") and (n > 1):
            if word[1] == 'h':
                count += 1
                return count_th(word[2:n], count)
        return count_th(word[1:n], count)
    else:
        return count
