import java.util.*;

public class Solution {
    /**
     * 解码
     * 
     * @param nums string字符串 数字串
     * @return int整型
     */
    public int solve(String nums) {
        // write code here
        return function(nums, 0);
    }

    int function(String nums, int a) {
        int re = 0;
        if (a >= nums.length())
            return 1;
        if (nums.charAt(a) != '0') {
            re = re + function(nums, a + 1);
            if (a + 1 < nums.length()) {
                String tmp = nums.charAt(a) + "" + nums.charAt(a + 1);
                if (new Integer(tmp) >= 1 && new Integer(tmp) <= 26) {
                    re = re + function(nums, a + 2);
                }
            }

        }
        return re;
    }
}