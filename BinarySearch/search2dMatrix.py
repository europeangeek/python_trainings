from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # TODO: There is a list of matrix which is sorted, algo that must be used here is called binary search
        # TODO: Current solution is o(n), find a solution log (m * n) 
        row = 1.5
        for i in range(len(matrix)):
            if target >= matrix[i][0] and target <= matrix[i][-1]:
                row = i
        print(row)
        if row == 1.5:
            return False
            
        left, right = 0, len(matrix[row]) - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False




matrix, target = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], 3
s = Solution()
print(s.searchMatrix(matrix, target))