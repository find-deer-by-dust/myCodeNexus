import java.util.*;

public class Solution {
    public int Add(int num1, int num2) {
        int tmp = num1;
        do {
            tmp = num1;
            num1 = num1 & num2;
            num1 = num1 << 1;
            num2 = tmp ^ num2;
        } while (num1 != 0);
        return num2;
    }
}