










'''
GCD-By-EUCLID
Thm(A) : k * gcd(a / k, b / k) = gcd(a , b)
Thm(B) : if a>b, gcd(a,b) = gcd(a-b,b)
'''



class GcdByBinary:
    def __init__(self):
        a = 0
    
    def mod_func(self, m=int, n=int):
        if n > m:
            return m
        else:
        	return m - (int(m / n) * n)
  
    def swap(self, a, b):
        tmp = a
        a = b
        b = tmp
        return a, b

    def main(self, a=int, b=int):
        # regard max(a,b) as c and min(a,b) as d
        c = max([a,b])
        d = min([a,b])
        # int virtual integer multiple
        k = 1
        while c != 0 and d != 0:
            # Thm(A) : k * gcd(a / k, b / k) = gcd(a , b)
            if c % 2 == 0 and d % 2 == 0:
                c, d = int(c / 2), int(d / 2)
                k = k * 2
            elif c % 2 == 0 and d % 2 != 0:
                c = int(c / 2)
            elif c % 2 != 0 and d % 2 == 0:
                d = int(d / 2)
            if c < d:
                c, d = self.swap(c, d)
            # Thm(B) : if a>b, gcd(a,b) = gcd(a-b,b)  
            c = c - d 
        return k * d





if __name__ == '__main__':
	# unit test
    test_data = [(1,1), (2,4), (2,5), (4,6), (6,4), (1,10), (100000,100000000000000000)]
    answer = [1, 2,1,2,2,1,100000]
    for i, unit_data in enumerate(test_data):
        print('test : ',GcdByBinary().main(a=unit_data[0], b=unit_data[1]))
        print('answer : ', answer[i])
        print('-------------------')
