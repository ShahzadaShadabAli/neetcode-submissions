class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []   # This will hold our final list of successful answers
        part = []  # This holds the current list of words we are trying out

        def dfs(i):
            # If we reached the end of the string, it means we successfully
            # split the whole string into good palindromes.
            if i == len(s):
                res.append(part.copy()) # Save a copy of our current list to the final answers
                return
            
            # Try making a cut at every possible position from 'i' to the end of the string
            for j in range(i, len(s)):
                
                # Check if the word from index 'i' to 'j' reads the same forwards and backwards
                if self.palindrome(s, i, j):
                    
                    # 1. Take the piece: Add this valid palindrome slice to our current list
                    part.append(s[i:j+1])
                    
                    # 2. Keep going: Move to the next character after 'j' and repeat the process
                    dfs(j+1)
                    
                    # 3. Clean up: Take the piece back out so the loop can try a different, longer cut
                    part.pop()

        # Start the process from the very first letter (index 0)
        dfs(0)
        return res


    def palindrome(self, s, l, r):
        # Check if a word is a palindrome using two pointers (left 'l' and right 'r')
        while l < r:
            # If the letters on opposite ends don't match, it's not a palindrome
            if s[l] != s[r]:
                return False
            
            # Move pointers closer to the middle
            l, r = l + 1, r - 1
            
        # If we checked all letters and they matched, it is a palindrome
        return True