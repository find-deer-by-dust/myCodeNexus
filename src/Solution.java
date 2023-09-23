import java.util.*;

public class Solution {
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     *
     * 第N个月的兔子对数总和
     * 
     * @param monthNum int整型 monthNum个月
     * @return int整型
     */
    int big = 0;
    int small1 = 1;
    int small2 = 0;
    // int small3=0;
    // int sum;
    public int sum_rabbit(int monthNum) {
        // write code here
        if (monthNum == 1) {
            return big+small1+small2;
        }
        int tmp;
        tmp=small2;
        // small3=small2;
        small2=small1;
        big=big+tmp;
        small1=big;
        
        
        return sum_rabbit(monthNum - 1);
    }
}