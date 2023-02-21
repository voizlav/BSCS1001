def anagrams(string1, string2):
    if len(string1) != len(string2):
        return False
    
    sorted1 = sorted(string1)
    sorted2 = sorted(string2)

    for i in range(len(sorted1)):
        if sorted1[i] != sorted2[i]:
            return False
    return True
