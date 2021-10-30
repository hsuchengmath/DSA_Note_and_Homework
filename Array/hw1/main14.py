









'''
GCD-By-EUCLID
Thm(A) : gcd(a, b) = gcd(b, a mod b)
Thm(B) : gcd(a,b) = gcd(b,a)
'''



class GcdByEUCLID:
    def __init__(self):
        a = 0
    
    def mod_func(self, m=int, n=int):
        if n > m:
            return m
        else:
        	return m - (int(m / n) * n)
  
    def main(self, a=int, b=int):
        # regard max(a,b) as c and min(a,b) as d
        c = max([a,b])
        d = min([a,b])
        # check whether c, d are integer multiple 
        while self.mod_func(m=c, n=d) != 0:
            # Thm(A) : gcd(a, b) = gcd(b, a mod b)
            tmp = c
            c = self.mod_func(m=c, n=d) 
            d = tmp
        return d





if __name__ == '__main__':
	# unit test
    test_data = [(1,1), (2,4), (2,5), (4,6), (6,4), (1,10), (100000,100000000000000000)]
    answer = [1, 2,1,2,2,1,100000]
    for i, unit_data in enumerate(test_data):
        print('test : ',GcdByEUCLID().main(a=unit_data[0], b=unit_data[1]))
        print('answer : ', answer[i])
        print('-------------------')
