# https://projecteuler.net/problem=24


def recurPermute(index, s, ans):

    # Base Case
    if index == len(s):
        ans.append("".join(s))
        return

    # Swap the current index with all
    # possible indices and recur
    for i in range(index, len(s)):
        s[index], s[i] = s[i], s[index]
        recurPermute(index + 1, s, ans)
        s[index], s[i] = s[i], s[index]

# Function to find all unique permutations
def findPermutation(s):

    # Stores the final answer
    ans = []

    recurPermute(0, list(s), ans)

    # sort the resultant list
    ans.sort()

    return ans


all = findPermutation("0123456789")
print(all[1000000-1])