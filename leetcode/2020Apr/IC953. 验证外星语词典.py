class Solution(object):
    def isAlienSorted(self, words, order):
        print order
        print words
        order_mapping = {}
        right_order = "abcdefghijklmnopqrstuvwxyz"
        for i in range(len(order)):
            order_mapping[order[i]]=right_order[i]
        # print order_mapping
        mapped_words = []
        for word in words:
            tmp = ''
            for c in word:
                c2 = order_mapping[c]
                tmp = tmp + c2
            mapped_words.append(tmp)
        print mapped_words
        mapped_words_copy = []
        for w in mapped_words:
            mapped_words_copy.append(w)
        mapped_words.sort()
        print mapped_words
        print mapped_words_copy
        for i in range(len(mapped_words)):
            if mapped_words[i] == mapped_words_copy[i]:
                continue
            else:
                return False
        return True