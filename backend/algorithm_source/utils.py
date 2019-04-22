from numpy import mean, std


def summarize_results(results, maximize=True, top_n=10):
    # check for no results
    if len(results) == 0:
        print('no results')
        return
    # determine how many results to summarize
    n = min(top_n, len(results))
    # create a list of (name, mean(scores)) tuples
    mean_scores = [(k, mean(v)) for k, v in results.items()]
    # sort tuples by mean score
    mean_scores = sorted(mean_scores, key=lambda x: x[1])
    # reverse for descending order (e.g. for accuracy)
    if maximize:
        mean_scores = list(reversed(mean_scores))
    # retrieve the top n for summarization
    names = [x[0] for x in mean_scores[:n]]
    scores = [results[x[0]] for x in mean_scores[:n]]
    d = []
    for s in scores:
        d.append(s.tolist())
    ranks = []
    for i in range(n):
        name = names[i]
        mean_score, std_score = mean(results[name]), std(results[name])
        record = 'Rank=%d, Name=%s, Score=%.3f (+/- %.3f)' % (i + 1, name, mean_score, std_score)
        ranks.append({'value': record})
    return names, d, ranks
