class Solution:
    def findUnion(self, a, b):
        seen = set()
        union = []
        for x in a:
            if x not in seen:
                union.append(x)
                seen.add(x)
        for x in b:
            if x not in seen:
                union.append(x)
                seen.add(x)
        union.sort()
        return union
