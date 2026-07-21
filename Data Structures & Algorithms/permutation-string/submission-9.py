class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # A child cannot be older than his father
        if len(s1) > len(s2):
            return False

        #26 letters of the english alphabet
        s1Count, s2Count = [0]*26, [0]*26

        # counting the first 3 characters of both strings (The main reason for this is to have the small one counted)
        # the second string is only here so we kill two stones with one bird
        for i in range(len(s1)):
            s1Count[ord(s1[i])-ord("a")] += 1
            s2Count[ord(s2[i])-ord("a")] += 1
        
        # if they match, early luck!
        if s1Count == s2Count:
            return True

        # Here the second string comparing part
        for j in range(len(s1), len(s2)):
            #count new val
            s2Count[ord(s2[j])-ord("a")] += 1
            #remove the oldest val so we only retain 3 characters
            s2Count[ord(s2[j-len(s1)])-ord("a")] -= 1
            if s1Count == s2Count:
                return True

        return False

