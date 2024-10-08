def flipColumn(arr, col):
    n = len(arr)

    for i in range(n):
        if arr[i][col] == 1:
            arr[i][col] = 0
        else:
            arr[i][col] = 1

def solution(beginning, target):
    answer = float("inf")
    rows = len(beginning)
    cols = len(beginning[0])

    flipped = []

    for i in range(rows):
        flipped.append([])
        for j in range(cols):
            if beginning[i][j]:
                flipped[i].append(0)
            else:
                flipped[i].append(1)

    for unit in range(1 << rows):
        rowFlipped = []
        flipCnt = 0
        for i in range(rows):
            comp = 1 << i

            if unit & comp:
                rowFlipped.append(flipped[i][:])
                flipCnt +=1
            else:
                rowFlipped.append(beginning[i][:])

        for j in range(cols):
            curCol = []
            targetCol = []

            for i in range(rows):
                curCol.append(rowFlipped[i][j])
                targetCol.append(target[i][j])

            if curCol != targetCol:
                flipColumn(rowFlipped, j)
                flipCnt +=1

        if rowFlipped == target:
            answer = min(answer, flipCnt)

    if answer == float("inf"):
        answer = -1

    return answer