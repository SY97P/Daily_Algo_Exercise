file = open('구간_합_구하기.txt', 'r')
input = file.readline


from math import ceil, log2


class SegmentTree:
    def __init__(self, arr):
        self.arr_size = len(arr)
        self.size = 2 ** (ceil(log2(self.arr_size)) + 1)
        self.tree = [0] * self.size
        self.build_tree(0, self.arr_size - 1, 0, arr)

    def build_tree(self, l, r, tree_idx, arr):
        if l == r:
            self.tree[tree_idx] = arr[l]
            return self.tree[tree_idx]

        m = (l + r) // 2
        l_tree = self.build_tree(l, m, tree_idx * 2, arr)
        r_tree = self.build_tree(m + 1, r, tree_idx * 2 + 1, arr)
        self.tree[tree_idx] = l_tree + r_tree
        return self.tree[tree_idx]

    def update(self, idx, diff):
        self.update_helper(0, self.arr_size - 1, idx, diff, 0)

    def update_helper(self, l, r, idx, diff, tree_idx):
        if idx < l or idx > r:
            return

        self.tree[tree_idx] += diff

        if l != r:
            m = (l + r) // 2
            self.update_helper(l, m, idx, diff, tree_idx * 2)
            self.update_helper(m + 1, r, idx, diff, tree_idx * 2 + 1)

    def query(self, s, e):
        return self.query_helper(0, self.arr_size - 1, s, e, 0)

    def query_helper(self, l_bound, r_bound, s_query, e_query, tree_idx):
        if l_bound > e_query or r_bound < s_query:
            return 0
        if s_query <= l_bound and r_bound <= e_query:
            return self.tree[tree_idx]

        mid = (l_bound + r_bound) // 2
        l_tree = self.query_helper(l_bound, mid, s_query, e_query, tree_idx * 2)
        r_tree = self.query_helper(mid + 1, r_bound, s_query, e_query, tree_idx * 2 + 1)
        return l_tree + r_tree


def main():
    n, m, k = map(int, input().split())
    nums = [0] + [int(input()) for _ in range(n)]

    segment = SegmentTree(nums)

    for _ in range(m + k):
        a, b, c = map(int, input().split())
        if a == 1:
            segment.update(b, c - nums[b])
        elif a == 2:
            value = segment.query(b, c)
            print(value)


if __name__ == '__main__':
    main()
