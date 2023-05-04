package forNowCoder;

import java.util.*;

public class Solution {
    public ArrayList<String> Permutation(String str) {
        ArrayList<String> res = new ArrayList<>();
        char[] chars = str.toCharArray();
        Permutation(chars, res, 0);

        return res;
    }

    public void Permutation(char[] chars, ArrayList<String> res, int i) {
        if (i == chars.length) {
            res.add(new String(chars));
            return;
        }
        // 每一层都使用一个hashset 来保存没有重复的字符，如果有重复，则不递归尝试获取排列
        HashSet<Character> temp = new HashSet<>();
        // 每个j位置的数都有机会来到i位置
        for (int j = i; j < chars.length; j++) {
            // 只要set中不包含j索引的字符，那么递归求解
            if (!temp.contains(chars[j])) {
                // 添加记录
                temp.add(chars[j]);
                // 交换位置
                permutationSwap(chars, i, j);
                // 递归求解
                Permutation(chars, res, i + 1);
                // 交换回来，下次循环继续
                permutationSwap(chars, i, j);
            }
        }
    }

    public void permutationSwap(char[] chars, int i, int j) {
        char temp = chars[i];
        chars[i] = chars[j];
        chars[j] = temp;
    }
}