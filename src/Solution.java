// import java.util.*;

public class Solution {
    public int InversePairs(int[] x) {
        int l = x.length;

        int a = function1(x, 0, l);

        return a;
    }

    int function1(int[] x, int a, int b) {
        int tmp = 0;
        int i;
        if (a < b - 1) {
            tmp += function1(x, a, (a + b) / 2);
            tmp = tmp % 1000000007;
            tmp += function1(x, (a + b) / 2, b);
            tmp = tmp % 1000000007;
            for (i = a; i < (a + b) / 2; i++) {

                for (int j = (a + b) / 2; j < b; j++) {
                    if (x[i] > x[j]) {
                        tmp++;
                    } else {
                        break;
                    }
                }
            }
            i = 0;
            while ((a + b) / 2 - i >= a) {
                swap(x, (a + b) / 2 - i, b);
                i++;
            }
        }
        return tmp % 1000000007;
    }

    void swap(int[] x, int a, int b) {
        int tmp;
        if (a < b) {
            for (int i = a; i < b - 1; i++) {
                if (x[i] > x[i + 1]) {
                    tmp = x[i];
                    x[i] = x[i + 1];
                    x[i + 1] = tmp;
                }
            }
        }
    }
}
