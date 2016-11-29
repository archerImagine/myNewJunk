package com.udacity.cs046.chapter01;

/**
 * Created by animeshb on 15/8/16.
 */
public class Algorithm02 {
    public static void main(String[] args) {
        int n = 10;

        while (n > 1){
            System.out.println(n);
//            System.out.println("% = " +(n%2));
            if ((n % 2 ) ==0){
//                System.out.println("n = " +n);
                n = n/2;
            }else{
                n = 3 * n + 1;
            }
        }
    }
}
