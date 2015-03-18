from collections import Counter, defaultdict

__all__ = ['merge_tuples']


def merge_tuples(tuples, merge_indexes, count_index, cls):
    # find items for merging
    tuples_set = set(tuples)
    merge_by_index = {}
    index_counter = {}
    for index in merge_indexes:
        merge_by_index[index] = defaultdict(set)
        index_counter[index] = Counter([t[index] for t in tuples])
        if len(index_counter[index]) != len(tuples):
            for item in tuples:
                if index_counter[index][item[index]] > 1:
                    merge_by_index[index][item[index]].add(item)
                    try:
                        tuples_set.remove(item)
                    except KeyError:
                        pass

    # search for self-intersections and update accordingly
    merge_list = sum(map(lambda d: d.values(), merge_by_index.values()), [])
    final_merge_list = []
    while merge_list:
        item = merge_list.pop()
        intersected = False
        for other_item in merge_list:
            if item.intersection(other_item):
                other_item.update(item)
                intersected = True
                break
        if not intersected:
            final_merge_list.append(item)

    # finally merge
    merged = set()
    for merger_item in final_merge_list:
        merged_item = list(merger_item)
        for index in merge_indexes:
            counter = defaultdict(lambda: 0)
            for t in merger_item:
                counter[t[index]] += t[count_index]
            merged_item[index] = sorted([t[index] for t in merger_item],
                                        key=lambda x: counter[x])[-1]
        merged_item[count_index] = sum([t[count_index] for t in merger_item])
        merged.add(cls(*merged_item))

    return list(tuples_set.union(merged))
