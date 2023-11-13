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
        // System.out.println(f);

        // 然后处理表达式中的括号问题,在处理的同时也将表达式进行了计算
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
        // 需要读一行,不然会导致输入中少读一行
        String tmp = input.nextLine();
        f = f.replace(" ", "");

        // 如果变量数大于0也就是存在变量,需要进行转换
        if (number > 0) {

            // 创建一个LinkedHashMap用于保存变量与真值的一一对应
            // 选择LinkedHashMap而不是HashMap的原因是LinkedHashMap是有序排列
            // 因此在后续对其的遍历时,遍历顺序是按照字符串中变量的顺序
            // 刚好和后续输入变量真值时顺序一一对应

            // key是变量,val就是对应的真值
            LinkedHashMap<String, String> lhm = new LinkedHashMap<String, String>();

            // 遍历字符串,开始寻找变量并添加到LinkedHashMap中,此时只添加了变量,并没有获得对应的真值
            // 先添加,后续更改真值
            for (int i = 0; i < f.length(); i++) {
                char c = f.charAt(i);

                // 最终添加的key,也就是变量名
                String stringKey = "" + c;

                // 只有字母开头才是变量
                if (c >= 'a' && c <= 'z') {

                    // 使用循环去判断字母后续是否是数字
                    while (i + 1 < f.length()) {
                        if (f.charAt(i + 1) >= '0' && f.charAt(i + 1) <= '9') {
                            stringKey = stringKey + f.charAt(i + 1);
                            i++;
                        }

                        else {
                            // 当后续不是数字时退出循环
                            break;
                        }
                    }

                    // 将获得的变量名添加入LinkedHashMap,val无所谓,后续输入时会更改
                    lhm.put(stringKey, "1");
                }
            }

            // 遍历LinkedHashMap的每一个值
            for (String key : lhm.keySet()) {

                // 输入获得该值对应的真值
                tmp = input.nextLine();
                tmp = tmp.replace(" ", "");

                // 判断输入值,以决定该变量的真值
                if (tmp.equals("true")) {
                    lhm.replace(key, "1");
                } else {
                    lhm.replace(key, "0");
                }
            }

            // 如此以来获得了变量与真值一一对应的LinkedHashMap
            // 再遍历一遍LinkedHashMap,将字符串中的变量替换为变量的真值
            for (String key : lhm.keySet()) {
                f = f.replace(key, lhm.get(key));
            }

        }

        // 替换输入时直接输入的T或者F
        f = f.replace("T", "1");
        f = f.replace("F", "0");
        return f;
    }

    // 去除字符串中的非运算符
    static String removeNot(String f) {

        // 因为会有"~~~~~~~1"这种情况出现,因此只替换一遍是不够的,需要循环判断以替换
        while (f.contains("~1") || f.contains("~0")) {
            f = f.replace("~1", "0").replace("~0", "1");
        }
        return f;
    }

    // 简单计算器,仅用于计算两个真值之间的计算
    // symbol是运算符
    static String simpleCalculator(String f, String symbol) {
        boolean a = false;
        boolean b = false;
        boolean result = false;

        // 将字符串中的两个真值提取出来
        // b采用倒数最后一个元素,是因为字符串内的运算符不是一个固定长度
        // 例如"&"和"<->"长度不一样
        a = (f.charAt(0) == '1');
        b = (f.charAt(f.length() - 1) == '1');

        // 通过等价关系,把这些运算转换为 与或非 的形式,方便直接调用java的逻辑运算符计算
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

    // 计算器,仅能计算不带括号的表达式
    // 基本原理是将长表达式处理为多个二元真值表达式
    static String Calculator(String f) {
        // 保存这四种运算符,方便简化代码,减少重复代码书写量
        // 同时按照运算优先级保存,以实现遍历时不同运算符的优先处理
        String[] symbols = { "&", "|", "->", "<->" };

        // 依次遍历运算符
        for (String i : symbols) {

            // 因为表达式中同一个运算符可能并不止一个,因此需要循环处理,直到不含该运算符为止
            while (f.contains(i)) {

                // 举例说明: 0|1&0|1
                // 先处理 & 符号

                // tag就是&的下标
                int tag = f.indexOf(i);

                // 因此根据&的下标,可以得到这个二元真值表达式的下标范围
                // 使用i.length()是因为不同符号长度不同,例如"&"和"<->"
                String tmp = f.substring(tag - 1, tag + 1 + i.length());
                // tmp的结果就是 "1&0"

                // 调用简单计算器计算 "1&0" 的结果,将他重新赋给tmp
                tmp = simpleCalculator(tmp, i);

                // 计算完这一部分后,字符串就可以更新了
                // 更新为 "0|"+"0"+"|1"
                // 即0|0|1
                f = f.substring(0, tag - 1) + tmp + f.substring(tag + 1 + i.length());
            }
        }

        return f;
    }

    // 处理表达式中的括号问题,在处理的同时也将表达式进行了计算
    // 基本原理是将括号中的内容提取出来,使用计算器计算得到的结果,达到去除括号的效果
    static String removeParenthesis(String f) {
        // 首先去除字符串中的非运算符
        // 因为这个函数会递归调用

        // 举例说明:比如如果最开始是 ~(1&0)
        // 此时调用一次removeNot()是处理不了的,因为这是带有括号的非
        // 但使用了一次removeParenthesis()后,会将其处理为~0
        // 同时再一次递归调用了removeParenthesis()
        // 就会再调用一次removeNot(),达到处理非的效果
        f = removeNot(f);

        // 如果带有括号,则处理括号
        if (f.contains("(")) {

            // 举例说明: 1|(1&(1|1)|0)&(1|0)
            // 使用ab记录最大的括号内的下标范围
            // 最大括号,也就是第一次出现 '(' 到最后一次出现 ')' 的范围
            int a = f.indexOf("(");
            int b = f.lastIndexOf(")");

            // 此时tmp也就是 1&(1|1)|0
            String tmp = f.substring(a + 1, b);

            // 再递归调用removeParenthesis(),处理tmp中的括号问题
            // 递归最后结果是没有括号的表达式,并计算出了结果,也就是1或者0
            tmp = removeParenthesis(tmp);

            // 因为计算出了最大括号的值,因此需要更新字符串
            // 1&(1|1)|0值为1
            // 因此f更新为 "1|" + "1" + "&(1|0)"
            f = f.substring(0, a) + tmp + f.substring(b + 1);

            // 可以看到,后续结果中依然有括号,因此还需要调用removeParenthesis()处理
            return removeParenthesis(f);
        }

        // 否则直接返回该表达式的计算结果
        else {
            return Calculator(f);
        }
    }
}
