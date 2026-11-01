def combinationSum2(candidates, target):
    candidates.sort()
    result = []

    def backtrack(start, path, total):

        if total == target:
            result.append(path.copy())
            return

        if total > target:
            return

        for i in range(start, len(candidates)):

            # Skip duplicate elements at the same level
            if i > start and candidates[i] == candidates[i-1]:
                continue

            path.append(candidates[i])

            backtrack(i + 1, path, total + candidates[i])

            path.pop()

    backtrack(0, [], 0)

    return result

candidates = [10,1,2,7,6,1,5]
target = 8

print(combinationSum2(candidates, target))