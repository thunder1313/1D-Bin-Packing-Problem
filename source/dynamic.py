def dynamic(problem, i, l):
    if i == -1 or l == 0:
        return 0
    if problem[0][i] > l:
        return function(problem, i-1, l)
    if problem[0][i] <= l:
        return max(function(problem, i-1, l), function(problem, i-1, l-problem[0][i]) + problem[1][i])