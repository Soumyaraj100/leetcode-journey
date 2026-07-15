class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ""
        i = 0
        while i < len(s):
            if i + 2 < len(s) and s[i + 2] == "#":
                if s[i:i+3] == "10#":
                    ans += "j"
                elif s[i:i+3] == "11#":
                    ans += "k"
                elif s[i:i+3] == "12#":
                    ans += "l"
                elif s[i:i+3] == "13#":
                    ans += "m"
                elif s[i:i+3] == "14#":
                    ans += "n"
                elif s[i:i+3] == "15#":
                    ans += "o"
                elif s[i:i+3] == "16#":
                    ans += "p"
                elif s[i:i+3] == "17#":
                    ans += "q"
                elif s[i:i+3] == "18#":
                    ans += "r"
                elif s[i:i+3] == "19#":
                    ans += "s"
                elif s[i:i+3] == "20#":
                    ans += "t"
                elif s[i:i+3] == "21#":
                    ans += "u"
                elif s[i:i+3] == "22#":
                    ans += "v"
                elif s[i:i+3] == "23#":
                    ans += "w"
                elif s[i:i+3] == "24#":
                    ans += "x"
                elif s[i:i+3] == "25#":
                    ans += "y"
                elif s[i:i+3] == "26#":
                    ans += "z"
                i += 3
            else:
                if s[i] == "1":
                    ans += "a"
                elif s[i] == "2":
                    ans += "b"
                elif s[i] == "3":
                    ans += "c"
                elif s[i] == "4":
                    ans += "d"
                elif s[i] == "5":
                    ans += "e"
                elif s[i] == "6":
                    ans += "f"
                elif s[i] == "7":
                    ans += "g"
                elif s[i] == "8":
                    ans += "h"
                elif s[i] == "9":
                    ans += "i"
                i += 1
        return ans