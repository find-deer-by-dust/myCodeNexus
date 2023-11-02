import java.util.*;

public class Solution {
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     *
     * 
     * @param number long长整型
     * @return long长整型
     */
    public long cutRope(long number) {
        if (number <= 3)
            return number - 1;
        long a = number / 3;
        long b = number % 3;
        long c = 998244353L;
        if (b == 0) {
            return pow3WithMod(a, c) % c;
        } else if (b == 1) {
            return pow3WithMod(a - 1, c) * 4 % c;
        } else {
            return pow3WithMod(a, c) * 2 % c;
        }
    }

    public long pow3WithMod(long n, long mod) {
        if (n == 0)
            return 1;
        if (n == 1)
            return 3;
        long part = pow3WithMod(n / 2, mod);
        if (n % 2 == 0)
            return part * part % mod;
        else
            return 3 * part * part % mod;
    }
}