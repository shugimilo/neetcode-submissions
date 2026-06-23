class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda interval: interval[0])
        print(f"Sorted intervals: {intervals}")
        merged = []
        buffer = []
        for i, interval in enumerate(intervals):
            if buffer:
                if buffer[1] >= interval[0]:
                    print(f"Iteration: {i}, buffer end larger than interval start, assigning buffer = {[buffer[0], max(buffer[1], interval[1])]}")
                    buffer = [buffer[0], max(buffer[1], interval[1])]
                else:
                    merged.append(buffer)
                    print(f"Iteration: {i}, buffer end smaller than interval start, appending buffer to merged, buffer={buffer}, merged={merged}")
                    buffer = interval
            else:
                print(f"Iteration: {i}, buffer empty, assigning buffer = intervals[{i}] = {intervals[i]}")
                buffer = interval

        merged.append(buffer)

        return merged