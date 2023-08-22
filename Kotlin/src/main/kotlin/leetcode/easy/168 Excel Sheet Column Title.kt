package leetcode.easy
/*Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28
...


Example 1:

Input: columnNumber = 1
Output: "A"
Example 2:

Input: columnNumber = 28
Output: "AB"
Example 3:

Input: columnNumber = 701
Output: "ZY"


Constraints:

1 <= columnNumber <= 231 - 1*/
class `168 Excel Sheet Column Title` {

    fun convertToTitle(columnNumber: Int): String {
        var result = ""
        var number = columnNumber

        while (number > 0) {
            number--
            val rem = number % 26
            result += ('A' + rem).toChar()
            number /= 26
        }

        return result.reversed()
    }
}