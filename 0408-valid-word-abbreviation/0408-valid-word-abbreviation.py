class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = j = 0
        if len(abbr) > len(word): return False

        while i < len(word) and j < len(abbr):
            
            if abbr[j].isalpha():
                if i < len(word) and abbr[j] == word[i]:
                    i += 1
                    j += 1
                else: return False
            else:
                if abbr[j] == '0': return False
                count = 0
                while j < len(abbr) and abbr[j].isnumeric():
                    count = count*10 + int(abbr[j])
                    j += 1
                i += count

        if i == len(word) and j == len(abbr): return True
        else: return False
       

        # t = O(n + m) and s = (1)        # Intialize some parameters
#         pointer_word, pointer_abbr = 0, 0

#         while pointer_word < len(word) and pointer_abbr < len(abbr):
#             if abbr[pointer_abbr].isdigit():
#                 if abbr[pointer_abbr] == '0': return False
#                 if len(abbr) > len(word): return False

#                 skip = 0
#                 while pointer_abbr < len(abbr) and abbr[pointer_abbr].isdigit():
#                     skip = skip * 10 + int(abbr[pointer_abbr])
#                     pointer_abbr += 1
#                 pointer_word += skip
#             else:
#                 if pointer_word >= len(word) or word[pointer_word] != abbr[pointer_abbr]: return False
#                 pointer_word += 1
#                 pointer_abbr += 1
#         return pointer_word == len(word) and pointer_abbr == len(abbr)