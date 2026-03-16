bool isPowerOfTwo(int n) {

    for (int i=0; i<=(log(n)/log(2));i++){

        if (n==pow(2,i)){
            return true;
        }
        
    }
    return false;
    
}