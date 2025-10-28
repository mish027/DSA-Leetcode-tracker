class Solution {
public:
    bool isPowerOfTwo(int n) {
        
        if (n>0 && (n&(n-1))==0){
            return true;
        }
        return false;
    }
    /*In C++,== has higher precedence than &.You must write (n & (n - 1))==0*/
};