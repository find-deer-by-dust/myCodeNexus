import java.util.*;

public class Test {
    public int[] test(int[] x) {
        int l = x.length;
        int[] a = x.clone();
        int[] b = x.clone();
        long stime, etime;

        stime = System.currentTimeMillis();
        a = function1(a, 0, l);
        etime = System.currentTimeMillis();
        System.out.printf("1执行时长：%d 毫秒.\n", (etime - stime));

        stime = System.currentTimeMillis();
        b = function2(b);
        etime = System.currentTimeMillis();
        System.out.printf("2执行时长：%d 毫秒.\n", (etime - stime));

        return x;
    }

    int[] function1(int[] x, int a, int b) {
        function1(x, a, b);

        return x;
    }

    int[] function2(int[] x) {
        int tag = 0;
        int l = x.length;
        int tmp;
        while (tag == 0) {
            tag = 1;
            for (int i = 0; i < l - 1; i++) {
                for (int j = i + 1; j < l; j++) {
                    if (x[i] > x[j]) {
                        tag = 0;
                        tmp = x[i];
                        x[i] = x[j];
                        x[j] = tmp;
                    }

                }
            }

        }

        return x;
    }
}
