class Solution(object):
    def topKFrequent(self, nums, k):
        freq_map = {}
        for num in nums:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1
        
        sorted_freq_map = sorted(freq_map.items(), key = lambda x: x[1], reverse = True)

        top_k_elements = []

        for i in range(0, k):
            top_k_elements.append(sorted_freq_map[i][0])
        
        return top_k_elements
            

        