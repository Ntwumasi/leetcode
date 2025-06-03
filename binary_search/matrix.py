def find_mid_matrix(matrix, target):
    left = 0
    right = n * m - 1

    while left <= right:
        mid = (left + right) // 2
        row = mid // n
        col = mid % n
        nums = matrix[row][col]

        if nums == target:
            return

        if num > target:
            right = mid - 1
        else:
            left = mid + 1
    return
