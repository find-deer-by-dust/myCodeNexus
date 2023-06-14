// import java.util.*;

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
        System.out.println(a[0] + "  " + a[a.length - 1]);

        stime = System.currentTimeMillis();
        b = function2(b);
        etime = System.currentTimeMillis();
        System.out.printf("2执行时长：%d 毫秒.\n", (etime - stime));
        System.out.println(b[0] + "  " + b[b.length - 1]);
        return x;
    }

    int[] function1(int[] x, int a, int b) {
        if (a != b) {
            function1(x, a, (a + b) / 2);
            function1(x, (a + b) / 2 + 1, b);
            int i = 0;
            while ((a + b) / 2 - i >= a) {
                swap(x, (a + b) / 2 - i, b);
                i++;
            }
        }
        return x;
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
