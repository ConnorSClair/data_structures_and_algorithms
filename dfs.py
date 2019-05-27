def is_cycle(adj_list) -> bool:
    # expect {a:[b,c],b:[c,d]...}
    unvisited = set(adj_list.keys())
    to_explore = []
    while len(unvisited) > 0:
        # pick a starting new starting node
        start = unvisited.pop()
        to_explore.append(start)
        path = set()
        path.add(start)
        while len(to_explore) > 0:
            this = to_explore.pop()
            for neighbour in adj_list[this]:
                # [b,c] etc.
                if neighbour in path:
                        return True
                if neighbour in unvisited:
                    to_explore.append(neighbour)
                    unvisited.remove(neighbour)
                    path.add(neighbour)
    return False
            


