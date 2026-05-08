class Solution:
    def binstr(self, n):
        # code here
        binary_str=[]
        for i in range(2**n):
            temp=bin(i)[2:].zfill(n)
            binary_str.append(temp)
        return binary_str