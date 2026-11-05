class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        KFrequent = {}

        for i in nums:
            if i in KFrequent:
                KFrequent[i] += 1
            else:
                KFrequent[i] = 1
        sortedByValue = dict(sorted(KFrequent.items(), key=lambda item: item[1], reverse=True))
        for idx, f in enumerate(sortedByValue):
            if idx == k: break
            result.append(f)
        return result