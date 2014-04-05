#http://pr.efactory.de/e-outbound-links.shtml
def compute_ranks(graph):
    d = 0.8 # damping factor
    numloops = 3

    ranks = {}
    npages = len(graph)
    for page in graph:
        ranks[page] = 1.0 / npages

    for i in range(0, numloops):
        newranks = {}
        for page in graph:
            newrank = (1 - d) / npages

            for node in graph:
                if page in graph[node]:
                    newrank=newrank + d * (ranks [node] / len (graph [node]))


            newranks[page] = newrank
        ranks = newranks
    return ranks


graph={ "A":["B", "C" ],
        "B":["A" ],
        "C":[ "B", "D"],
        "D":["A" ]
        }

print compute_ranks(graph)
