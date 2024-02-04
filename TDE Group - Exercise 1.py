def GetUniqueCharacter(s):

    if not all(char.islower() for char in s):
        return -1, "The input should only consist of lowercase English letters only" 
    
    char_counts = {}
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1

    # unique_chars = []
    # for char, count in char_counts.items():
    #     if count == 1:
    #         unique_chars.append(char)

    # return unique_chars
        
    for i, char in enumerate(s):
        if char_counts[char] == 1:
            return i + 1  # 1-based indexing

    return -1, "There is no unique character"


s = "llll"
index = GetUniqueCharacter(s)
print(index) 