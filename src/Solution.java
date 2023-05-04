
import java.util.ArrayList;

public class Solution {
    public ArrayList<String> Permutation(String str) {
        if (str == null || str.length() == 0)
            return null;
        char[] c = str.toCharArray();
        ArrayList<int[]> tmp = new ArrayList<int[]>();
        int len = str.length();
        int[] num = new int[len];
        int[] list = new int[len];
        ArrayList<String> re = new ArrayList<String>();

        for (int i = 0; i < len; i++)
            num[i] = i;
        function(num, 0, list, tmp);

        System.out.println("---");
        for (int i = 0; i < tmp.size(); i++) {
            char[] tmp2 = new char[len];
            int[] tmp3 = tmp.get(i);
            for (int j = 0; j < len; j++) {
                tmp2[j] = c[tmp3[j]];
            }
            re.add(new String(tmp2));
        }

        for (int i = 0; i < re.size(); i++) {
            for (int j = i + 1; j < re.size(); j++) {
                if (re.get(i).compareTo(re.get(j)) == 0) {
                    re.set(j, "--");
                }
            }
        }

        for (int i = 0; i < re.size(); i++) {
            if (re.get(i).compareTo("--") == 0) {
                re.remove(i);
                i--;
            }
        }

        return re;
    }

    void function(int[] num, int index, int[] list, ArrayList<int[]> tmp) {

        if (index == num.length) {
            int[] x = list.clone();
            tmp.add(x);
        } else {
            for (int i = 0; i < num.length; i++) {
                if (num[i] != -1) {
                    list[index] = num[i];
                    num[i] = -1;
                    function(num, index + 1, list, tmp);
                    num[i] = i;
                }
            }
        }

    }
}