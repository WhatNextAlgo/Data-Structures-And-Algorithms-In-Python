def naive_search(pattern,text):
    m = len(pattern)
    n = len(text)
    if m > n:return -1

    # this operation takes O(n)
    for i in range(n - m + 1):
        # track the letters in the pattern (starting 0)
        # from left to right

        j = 0
        # all the letters of the pattern O(m) - in worse case
        # this approach takes O(n * m)
        while j < m:

            # we have to compare the characters
            if text[i + j] != pattern[j]:
                break

            # consider the next characters
            j += 1
        if j == m:
            print("found a match at index: %s "%(i))


if __name__ == "__main__":
    naive_search("abcd","abcderdfeabcd")




