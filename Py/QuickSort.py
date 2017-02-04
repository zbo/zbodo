import unittest

source = [11, 4, 5, 6, 7, 2, 1, 4, 7, 6, 7, 8, 0, 3]


# source = [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
# source = [0, 0, 0, 0, 0]
# source = [0]


def find_big_from_left(mid):
    for i in range(mid):
        if source[i] > source[mid]:
            return i
    return mid


def find_small_from_right(mid, end):
    for i in range(end, mid, -1):
        if source[i] < source[mid]:
            return i
    return mid


def swap(left, right):
    temp = source[left]
    source[left] = source[right]
    source[right] = temp


def sort_single(start, end):
    if source[start] > source[end]:
        swap(start, end)


def sort_onece(start, end):
    if start == end - 1:
        sort_single(start, end)
        return
    big_left = start
    small_right = end
    mid = (start + end) / 2
    while big_left != small_right:
        big_left = find_big_from_left(mid)
        small_right = find_small_from_right(mid, end)
        swap(big_left, small_right)
    sort_onece(start, mid)
    sort_onece(mid, end)


def quick_sort(source):
    if len(source) > 1:
        start = 0
        end = len(source) - 1
        sort_onece(start, end)
    return source


class mytest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testsum(self):
        self.assertEqual(str(quick_sort(source)), '[0, 1, 2, 3, 4, 4, 5, 6, 6, 7, 7, 7, 8, 11]', 'test sum fail')


if __name__ == '__main__':
    unittest.main()
