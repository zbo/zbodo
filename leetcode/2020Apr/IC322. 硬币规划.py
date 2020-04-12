class Solution(object):
    def __init__(self):
        self.possible = []
        self.Min = -1

    def search_solution(self, coins, amount, used):
        # print "used={0} amount={1}".format(used,amount)
        if len(used) > self.Min - 1 and self.Min != -1:
            return
        if amount <= 0:
            return
        if amount in coins:
            used.append(amount)
            # print self.possible, used
            self.possible.append(len(used))

            if self.Min == -1 or len(used) < self.Min:
                self.Min = len(used)
            used.pop(len(used) - 1)
            return

        for c in coins:
            if c < amount:
                used.append(c)
                self.search_solution(coins, amount - c, used)
                used.pop(len(used) - 1)

    def coinChange(self, coins, amount):
        if amount == 0:
            return 0
        used = []
        self.search_solution(coins, amount, used)
        if len(self.possible) == 0:
            return -1
        return self.Min
        # print self.possible


class Solution(object):
    def __init__(self):
        self.possible = []
        self.memory = {}

    def minium_coins(self, coins, amount):
        if amount in self.memory:
            return self.memory[amount]
        minium = None
        if amount in coins:
            return 1
        for c in coins:
            if amount > c:
                next_value = self.minium_coins(coins,amount-c)
                if next_value is None:
                    continue
                if minium is None or next_value+1<minium:
                    minium = next_value+1
        self.memory[amount] = minium
        return minium

    def coinChange(self, coins, amount):
        if amount == 0:
            return 0
        min_v = self.minium_coins(coins, amount)
        print self.memory
        if min_v is None:
            return -1
        return min_v
