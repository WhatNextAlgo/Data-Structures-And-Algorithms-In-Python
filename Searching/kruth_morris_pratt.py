def construct_pi(pattern):
    # the table has as many values as the length of the pattern (first item is always 0)
    pi_table = [0] * len(pattern)
    i = 1
    prefix_counter = 0

    # O(n) linear running time
    while i < len(pattern):
        if pattern[i] == pattern[prefix_counter]:
            prefix_counter += 1
            pi_table[i] = prefix_counter
            i += 1
        else:
            if prefix_counter != 0:
                prefix_counter = pi_table[prefix_counter -1]
            else:
                pi_table[i] = 0
                i += 1
    return pi_table

def search(text,pattern):
    pi_table = construct_pi(pattern)
    # index i tracks the text - index j tracks the pattern
    i , j = 0,0

    while i < len(text) and j < len(pattern):
        # if the characters are matching we increment both indexes  
        if text[i] == pattern[j]:
            i += 1
            j += 1
        # we found the pattern in the text ( + reinitialize the j index to be able to find more pattern)
        if j == len(pattern):
            print("Pattern found at index: ",i - j)
            j = pi_table[j-1]

        # if there is a match
        elif i < len(text) and text[i] != pattern[j]:
            # if we can decrement j then  we decrement it based on the pi table
            if j != 0:
                j = pi_table[j-1]
            # if we are not able to decremnt j (beacuse it has value 0) we incremnt i
            else:
                i += 1






if __name__ == "__main__":

    print(construct_pi("aafabaafab"))
    search('this is a test','test')
    search('aafabaafab','aafa')
