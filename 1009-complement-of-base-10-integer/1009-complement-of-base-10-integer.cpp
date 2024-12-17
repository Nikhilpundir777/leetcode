class Solution {
public:
    int bitwiseComplement(int n) {

        int rem,ans=0,mul=1;
        if(n==0)
        return 1;

        while(n){

            rem=n%2;
            rem=rem^1;
            n/=2;

            ans=ans+rem*mul;
            mul*=2;

        }
        return ans;
        
    }
};