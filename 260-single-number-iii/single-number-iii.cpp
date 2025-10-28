class Solution {
public:
    vector<int> singleNumber(vector<int>& nums) {
        unsigned int res=0;
        for(const int num:nums){
            res^=num;
        }
        
        unsigned int mask=res&(-res);
        int grpA=0,grpB=0;
        for (const int num: nums){
            if ((num & mask)==0){
                grpA^=num;
            }
            else{
                grpB^=num;
            }
                
        }
        return {grpA,grpB};
    }
};