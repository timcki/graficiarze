def find_hamilton(adj_list, actual, path=[]):
    if actual not in set(path):
        path.append(actual)
        if len(path) == len(adj_list) and 1 in adj_list[path[-1]]:
            path.append(path[0])
            return path

        for pt_next in adj_list.get(actual, []):
            res_path = [i for i in path]
            candidate = find_hamilton(adj_list, pt_next, res_path)
            if candidate is not None:  # skip loop or dead end
                return candidate
        return None
    else:
        return None


def check_hamilton_cycle(adj_list):
    result = find_hamilton(adj_list, 1, [])
    if result is not None:
        print(f"Hamilton's cycle: {','.join([str(i) for i in result])}")
    else:
        print("There is no Hamilton's cycle in given Graph")

