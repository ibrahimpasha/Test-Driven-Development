from timeit import default_timer as timer

def performance_time(function, position, repeats):
    splits = []
    for _ in range(repeats):
        start = timer()
        function(position)
        splits.append(timer() - start)
    return min(splits), sum(splits) / len(splits)