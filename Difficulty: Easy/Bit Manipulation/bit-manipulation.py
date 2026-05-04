#User function Template for python3

class Solution:
    def bitManipulation(self, num, i):
        # Code here
        get=int(bool(num&(1<<(i-1))))

        setbit= num | (1<<(i-1))

        clear=num & ( ~(1<<(i-1)))
        print(get,setbit,clear)