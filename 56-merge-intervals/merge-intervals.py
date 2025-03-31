class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # Sort the intervals by start time.

        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        count = 0
        i = 0
        j = i + 1
        while i < len(sorted_intervals):
            while j < len(sorted_intervals) and sorted_intervals[j][0] <= sorted_intervals[i][1]:
                    sorted_intervals[i][1] = max(sorted_intervals[i][1], sorted_intervals[j][1])
                    j += 1

            # i and j includes all the overlapping intervals
            sorted_intervals[count][0] = sorted_intervals[i][0]        
            sorted_intervals[count][1] = sorted_intervals[i][1]    
            count += 1 
            i = j
            j = i + 1
        return sorted_intervals[:count]