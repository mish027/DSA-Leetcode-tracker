bool isPowerOfTwo(int n) {

    if (n<=0){
        return false;
    }
    int limit = log(n)/log(2); //value never changes, so recalculation is not needed

    for (int i=0; i<=limit;i++){

        if (n==pow(2,i)){
            return true;
        }
        
    }
    return false;
    
}