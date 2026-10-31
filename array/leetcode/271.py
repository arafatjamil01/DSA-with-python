class Solution:

    def encode(self, strs: List[str]) -> str:
        new_strs = ''
        for i in strs:
            # for each item in the array, use length(int) then #, then the string, for each one
            # new_strs += f"{len(i)}#{i}"
            new_strs += f"{i}###"
        return new_strs


    def decode(self, s: str) -> List[str]:
        # get the length of the word followed 
        new_list = s.split("###")
        new_list.pop()
        print(new_list)
        
strs = ["#"]
solution = Solution()
encoded_string = solution.encode(strs)
decoded_strs = solution.decode(encoded_string)
