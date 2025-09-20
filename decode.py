class Solution:
    def decodeString(self, s: str) -> str:

        cur_string=""
        num=0
        result=""
        stack=[]
        for char in s:
            if char.isdigit():
                num=num*10+int(char)
                            
            elif char=='[':
                stack.append((cur_string,num))
                num=0
                cur_string=""
                

            elif char.isalpha():
                cur_string+=char
                
            elif char==']':
                element=stack.pop()
                
                cur_string=element[0]+(element[1])*cur_string    
                
        return cur_string

        
