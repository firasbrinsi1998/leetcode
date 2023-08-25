class Solution {
    public boolean isPalindrome(int x) {
        if(x==0){
            return true;
        }
       if(x<0) {
           return false;
       }
       if (x%10==0){
           return false;
       }

        int reversed_int=0;
        while (reversed_int<x){
            int reste=x%10;
            x/=10;
            reversed_int=(reversed_int*10) + reste;
        }   
    
        if(x==reversed_int || x==reversed_int/10){
            return true;
        }
        else {
            return false;
        }
    }
}