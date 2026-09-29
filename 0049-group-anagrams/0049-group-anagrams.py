from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        if not strs:
            return []

        hashing = {
            'a' : 0,
            'b' : 1, 
            'c' : 2,
            'd' : 3,
            'e' : 4,
            'f' : 5,
            'g' : 6, 
            'h' : 7,
            'i' : 8,
            'j' : 9,
            'k' : 10,
            'l' : 11,
            'm' : 12,
            'n' : 13,
            'o' : 14,
            'p' : 15,
            'q' : 16,
            'r' : 17,
            's' : 18,
            't' : 19,
            'u' : 20,
            'v' : 21,
            'w' : 22, 
            'x' : 23,
            'y' : 24, 
            'z' : 25
        }

        families = defaultdict(list)
        for word in strs:
            bag = [0 for _ in range(26)]
            for char in word:
                bag[hashing[char]] += 1
            families[tuple(bag)].append(word)

        return [list(x) for x in families.values()]

"""
from collections import defaultdict
        # We will consider that anagrams can be represented as "bags" of letters, where count matters
        families = defaultdict(list)

        for word in strs:
            bag = defaultdict(int)
            for char in word:
                bag[char] += 1
            families[dict(bag)].append(word)

        return families.values()

"""
        