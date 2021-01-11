import numpy as np

class NewtonMethod:
	def __init__(self, loops=10):
		self.loops = loops

	def sqrt(self, x):
		# f(x) = x^2 - a = 0
		guess = x/2 # initial guess
		for i in range(self.loops):
			guess = guess - ((guess**2 - x) / (2*guess))
		return guess

	def w(self, x):
		# f(x) = xe^x - a = 0
		guess = np.log(x) # initial guess
		for i in range(self.loops):
			expguess = np.exp(guess)
			guess = guess - ((guess*expguess) - x)/(guess*expguess + expguess)
		return guess
		
	# add exponential
	# do x^(1/x)
		
thing = NewtonMethod()
print('sqrt(69):', thing.sqrt(69))
print('W(69):', thing.w(69))