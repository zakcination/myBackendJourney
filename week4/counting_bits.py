def countBits(n):
    ans = [0]
    for i in range(1,n+1):

        cur = 0
        print(f"i:  {i} bin({i}) : {bin(i)}")
        while i:
            print(bin(i))
            cur += i & 1
            i >>= 1
        ans.append(cur)
        print("\n")
    return ans

if __name__ == "__main__":
    countBits(6)