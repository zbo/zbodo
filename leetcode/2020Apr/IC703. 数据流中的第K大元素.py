'''

设计一个找到数据流中第K大元素的类（class）。注意是排序后的第K大元素，不是第K个不同的元素。

你的 KthLargest 类需要一个同时接收整数 k 和整数数组nums 的构造器，它包含数据流中的初始元素。每次调用 KthLargest.add，返回当前数据流中第K大的元素。

示例:

int k = 3;
int[] arr = [4,5,8,2];
KthLargest kthLargest = new KthLargest(3, arr);
kthLargest.add(3);   // returns 4
kthLargest.add(5);   // returns 5
kthLargest.add(10);  // returns 5
kthLargest.add(9);   // returns 8
kthLargest.add(4);   // returns 8

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/kth-largest-element-in-a-stream
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

["KthLargest","add","add","add","add","add"]
[[3,[4,5,8,2]],[3],[5],[10],[9],[4]]

'''


class KthLargest(object):
    def __init__(self, k, nums):
        self.k = k
        self.nums = nums
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]>nums[j]:
                    temp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp
        self.memory = self.nums[:k]

    def insertIntoArray(self, val):
        for i in range(len(self.memory)):
            if i == len(self.nums)-1 and len(self.memory)<self.k:
                self.memory.append(val)
            if self.memory[i]>val:
                continue
            else:
                temp = self.memory[:i]
                temp.append(val)
                temp.extend(self.memory[i:])
                self.memory = temp[:self.k]
                break

    def add(self, val):
        self.insertIntoArray(val)
        print(self.memory)
        if len(self.memory) < self.k:
            return self.memory[len(self.nums)-1]
        else:
            return self.memory[self.k-1]



if __name__ == "__main__":
    # k = 2
    # arr = [0]
    # s = KthLargest(k, arr)
    # print(s.add(-1))
    # print(s.add(1))
    # print(s.add(-2))
    # print(s.add(-4))
    # print(s.add(3))
    k = 3
    arr = [4, 5, 8, 2]
    s = KthLargest(k, arr)
    print(s.add(3))
    print(s.add(5))
    print(s.add(10))
    print(s.add(9))
    print(s.add(4))
