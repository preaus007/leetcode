def lengthOfLongestSubstring(s):
    seen = {}
    l = 0
    ln = 0
    for r in range(len(s)):
        char = s[r]
        if char in seen and seen[char] >= l:
            l = seen[char] + 1
        else:
            ln = max(ln, r - l + 1)
        seen[char] = r

    return ln

    # Solution with dequeue
    res = 0
    q = deque()
    for c in s:
        if c in q:
            while q.popleft() != c:
                pass
        q.append(c)
        res = max(res, len(q))
    
    return res

if __name__ == "__main__":
    a = "dvdf"
    result = lengthOfLongestSubstring(a)
    print(f"Maximum length are : {result}")
