import java.util.*;

public class Solution {
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     *
     * 
     * @param n int整型
     * @return int整型
     */
    public int findNthDigit(int n) {
        int digits = 1;
        int startNum = 0;
        int totalNum = 10;
        while (n > totalNum) {
            n = n - totalNum;
            startNum = pow(digits);
            digits++;
            totalNum = 9 * pow(digits - 1);
        }

        return 1;
    }

    int pow(int n) {
        if (n == 0)
            return 1;
        return 10 * pow(n - 1);
    }
}