# Given a string s of '(' , ')' and lowercase English characters.
#
# Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.
#
# Formally, a parentheses string is valid if and only if:
#
# It is the empty string, contains only lowercase characters, or
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.
#
#
# Example 1:
#
# Input: s = "lee(t(c)o)de)"
# Output: "lee(t(c)o)de"
# Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
# Example 2:
#
# Input: s = "a)b(c)d"
# Output: "ab(c)d"
# Example 3:
#
# Input: s = "))(("
# Output: ""
# Explanation: An empty string is also valid.
#
#
# Constraints:
#
# 1 <= s.length <= 105
# s[i] is either'(' , ')', or lowercase English letter.


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        OPEN = '('
        CLOSE = ')'
        stack = []
        prefix = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == OPEN:
                if prefix > 0:
                    prefix -= 1
                else:
                    continue
            elif s[i] == CLOSE:
                prefix += 1
            stack.append(s[i])

        prefix = 0
        result = []
        for i in range(len(stack) - 1, -1, -1):
            if stack[i] == CLOSE:
                if prefix > 0:
                    prefix -= 1
                else:
                    continue
            elif stack[i] == OPEN:
                prefix += 1
            result.append(stack[i])

        return "".join(result)


sol = Solution()
assert sol.minRemoveToMakeValid("lee(t(c)o)de)") == "lee(t(c)o)de"
assert sol.minRemoveToMakeValid("a)b(c)d") == "ab(c)d"