import java.util.*;

public class Solution {
    public int findNthDigit(int n) {
        int digits = 1;
        long startNum = 1;
        long totalNum = 9;

        while (n > totalNum) {
            n -= totalNum;
            startNum *= 10;
            digits++;

            totalNum = 9 * startNum * digits;
        }

        System.out.println(startNum);

        long tmp = startNum + (n - 1) / digits;
        int tmp1 = (n - 1) % digits;
        System.out.println(tmp);
        String re = "" + tmp;
        return re.charAt(tmp1) - '0';
    }

    long pow(long n) {
        if (n == 0)
            return 1;
        return 10 * pow(n - 1);
    }
}