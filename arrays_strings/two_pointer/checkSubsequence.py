def check_subsequence(s,t):
    i = j = 0
    while i < len(s) and j < len(t):
        if s[i]==t[j]:
            i+=1
        j+=1

    return  i len(s)

# Test cases
print(check_subsequence("abc", "ahbgdc"))  # True
print(check_subsequence("axc", "ahbgdc"))  # False
print(check_subsequence("ace", "abcde"))   # True