def wordBreak(s, wordDict):
    n = len(s)
    dict_set = set(wordDict)

    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        for j in range(0, i):
            if dp[j] == 1 and s[j:i] in dict_set:
                dp[i] = 1
                break

    print(dp)
    return dp[n] == 1