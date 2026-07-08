class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        answer = []



        for num in nums:

            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1

        for i in range(k):
            highest_number = 0
            best_number = None

            for numnber, frequency in counts.items():
                if frequency > highest_number:
                    highest_number = frequency
                    best_number = numnber

            answer.append(best_number)
            del counts[best_number]

        return answer

    
