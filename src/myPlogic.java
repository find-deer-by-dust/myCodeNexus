import java.util.*;

public class myPlogic {
    // 使用静态Scanner方便主函数和函数中调用
    static Scanner input = new Scanner(System.in);

    public static void main(String[] args) {
        String f = input.nextLine();
        int number = input.nextInt();

        // 首先将表达式中的变量转换为true或者false
        f = formulaTransform(f, number);
        // 可以打印出来看一下
        System.out.println(f);

        // 然后处理表达式中的括号问题
        f = removeParenthesis(f);

        // 最终结果是0或者1,但是不符合输出要求,因此需要转化
        if (f.equals("0")) {
            System.out.println("false");
        } else {
            System.out.println("true");
        }
    }

    // 转换表达式中的变量
    static String formulaTransform(String f, int number) {
        String tmp = input.nextLine();
        f = f.replace(" ", "");

        if (number > 0) {
            LinkedHashMap<Character, Character> lhm = new LinkedHashMap<Character, Character>();
            for (int i = 0; i < f.length(); i++) {
                char c = f.charAt(i);
                if (c >= 'a' && c <= 'z' && !lhm.containsKey(c)) {
                    lhm.put(c, '1');
                }
            }

            for (Character key : lhm.keySet()) {
                tmp = input.nextLine();
                tmp = tmp.replace(" ", "");
                if (tmp.equals("true")) {
                    lhm.replace(key, '1');
                } else {
                    lhm.replace(key, '0');
                }
            }
            for (Character key : lhm.keySet()) {
                f = f.replace(key, lhm.get(key));
            }
            f = f.replace("T", "1");
            f = f.replace("F", "0");
        }
        return f;
    }

    static String removeNot(String f) {
        while (f.contains("~1") || f.contains("~0")) {
            f = f.replace("~1", "0").replace("~0", "1");
        }
        return f;
    }

    static String simpleCalculator(String f, String symbol) {
        boolean a = false;
        boolean b = false;
        boolean result = false;
        a = (f.charAt(0) == '1');
        b = (f.charAt(f.length() - 1) == '1');

        if (symbol.equals("&")) {
            result = a && b;
        } else if (symbol.equals("|")) {
            result = a || b;
        } else if (symbol.equals("->")) {
            result = !a || b;
        } else if (symbol.equals("<->")) {
            result = (a && b) || (!a && !b);
        }
        if (result) {
            return "1";
        } else {
            return "0";
        }
    }

    static String Calculator(String f) {
        String[] symbols = { "&", "|", "->", "<->" };
        for (String i : symbols) {
            while (f.contains(i)) {
                int tag = f.indexOf(i);
                String tmp = f.substring(tag - 1, tag + 1 + i.length());
                tmp = simpleCalculator(tmp, i);
                f = f.substring(0, tag - 1) + tmp + f.substring(tag + 1 + i.length());
            }
        }

        return f;
    }

    static String removeParenthesis(String f) {
        f = removeNot(f);

        if (f.contains("(")) {
            int a = f.indexOf("(");
            int b = f.lastIndexOf(")");
            String tmp = f.substring(a + 1, b);
            tmp = Calculator(tmp);
            f = f.substring(0, a) + tmp + f.substring(b + 1);
            return removeParenthesis(f);
        } else {
            return Calculator(f);
        }
    }
}
