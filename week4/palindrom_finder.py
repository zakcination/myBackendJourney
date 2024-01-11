def longestPalindrome( s):
        """
        :type s: str
        :rtype: str
        """
        ans = ''
        for i in range(len(s)):
            ans = max(ans,expand(s,i,i), expand(s,i,i+1), key = len)
        return ans
    

def expand(s,i,j):
    while i>=0 and j<len(s) and s[i] == s[j]:
        i -= 1
        j += 1
        print(s[i+1:j])
    return s[i+1:j]


if __name__ == "__main__":
    print(longestPalindrome("babad"))