class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        st = []
        for token in tokens:
            if token=='+' or token=='-' or token=='*' or token=='/':

                num1 = st.pop()
                num2 = st.pop()

                if token=='+':
                    st.append(num2+num1)

                elif token=='*':
                    st.append(num2*num1)
                        
                elif token=='-':
                    st.append(num2-num1)
                        
                else:
                    st.append(int(num2/num1)) # to truncate negative numbers to 0
                                   
            else:
                st.append(int(token))
        return st.pop()
        #mistake syntax for switch in python, its match case: