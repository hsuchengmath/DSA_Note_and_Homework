






'''
GCD-By-DEF
'''



class GcdByDEF:
    def __init__(self):
        a = 0
    
    def mod_func(self, m=int, n=int):
        if n > m:
            return m
        else:
        	return m - (int(m / n) * n)
  
    def main(self, a=int, b=int):
		# init
        terminal_val = min(a, b)
		# if min(a,b) <= 1, then gcd(a,b) = 1
        if terminal_val <= 1:
            return 1
		# if min(a,b) > 1
        else:
            ans = 1
            for i in [2+j for j in range(terminal_val-1)]:
                if self.mod_func(m=a, n=i) == 0 and self.mod_func(m=b, n=i) == 0:
                    ans = i
            return ans





if __name__ == '__main__':
	# unit test
    test_data = [(1,1),(2,4), (2,5), (4,6), (6,4), (1,10), (100000,100000000000000000)]
    answer = [1,2,1,2,2,1,100000]
    for i, unit_data in enumerate(test_data):
        print('test : ',GcdByDEF().main(a=unit_data[0], b=unit_data[1]))
        print('answer : ', answer[i])
        print('-------------------')

















