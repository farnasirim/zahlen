#!/usr/bin/env python
from ds.tree.order_statistics_tree import OrderStatisticsTree
from ds.tree.order_statistics_tree import Node

import math



def main():
    tree = OrderStatisticsTree(Node)
    values = [6.2, 1.2, 4.4, 1.3, 0.3]
    print(values)

    for val in values:
        tree.insert(val)

    while True:
        val = float(input())
        print("get_rank:", get_rank(val, tree, 5))
        print("get_rank_apx:", tree.get_rank_apx(val))


def get_rank(val, tree, n):
    lo = 1
    hi = n
    index = -1
    ans_val = float("inf")
    while lo <= hi:
        md = (lo + hi)//2
        value_of_md = tree.kth_smallest_key(md)
        print(value_of_md, val)
        if abs(value_of_md - val) < abs(ans_val - val):
            ans_val = value_of_md
            index = md
        if val < value_of_md:
            hi = md - 1
        else:
            lo = md + 1

    return index


if __name__ == "__main__":
    main()
