class Solution(object):
    def getLucky(self, s, k):
        convert_num_str= ''.join(str(ord(i)-96) for i in s)
        for x in range(k):
            convert_num_str=str(sum(int(i) for i in convert_num_str))
        return int(convert_num_str)
        