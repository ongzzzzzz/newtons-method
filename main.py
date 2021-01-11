import numpy as np

class Approxy:
	def __init__(self, loops=10):
		self.loops = loops

	def nwtn_sqrt(self, x):
		# sqrt(a) = x ====>>>> x^2 = a
		# f(x) = x^2 - a = 0
		guess = x/2 # initial guess
		for i in range(self.loops):
			guess = guess - ((guess**2 - x) / (2*guess))
		return guess

	def nwtn_w(self, x):
		# f(x) = xe^x - a = 0
		guess = np.log(x) # initial guess
		for i in range(self.loops):
			expguess = np.exp(guess)
			guess = guess - ((guess*expguess) - x)/(guess*expguess + expguess)
		return guess
	
	def nwtn_selfroot(self, x):
		# a^1/a = x ====>>>> x^a = a
		# f(x) = x^a - a = 0
		guess = 1.5 # initial guess - this works well for only values close to 0
		# undefined for even roots of negative numbers
		if (x<0 and x%2==0): return 'undefined' 
		for i in range(self.loops):
			# print(guess)
			guess = guess - ( guess**(1-x) * (1 - x*(guess**(-x))) )
		return guess

	# add exponential
		
thing = Approxy(10)
print('sqrt(69):', thing.nwtn_sqrt(69))
print('W(69):', thing.nwtn_w(69))
print('selfroot(2):', thing.nwtn_selfroot(2))