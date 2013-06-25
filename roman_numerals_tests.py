import unittest;

class Conversor(object):
	def __init__(self):
		self.convertion_table = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}

	def convert(self, number):
		if number in self.convertion_table:
			return self.convertion_table[number]
		else:
			if (number+1) in self.convertion_table:
				roman_part_two = self.convertion_table[number+1]
				print 'I%s' %roman_part_two
				return 'I%s' %roman_part_two

			print sorted(self.convertion_table.keys(), None, None, True)
			for k in sorted(self.convertion_table.keys(), None, None, True):
				rest = number%k
				print 'number: %s rest: %s k: %s' %(number,rest,k)

				if rest == 0:
					times = number/k
					result = [self.convertion_table[k] for i in range(times)]
					print 'result1: %s' %result
					return ''.join(result)

				elif rest < number:
					times = number/k
					result = [self.convertion_table[k]*times]
					print "result2 %s" %result
					result2 = [self.convert(rest)]
					concatenation = result + result2
					print "tmp %s" %concatenation
					return ''.join(concatenation)





class TestSequenceFunctions(unittest.TestCase):

	def setUp(self):
		self.conversor = Conversor()

	def test_basic_numbers(self):
		self.assertEqual(self.conversor.convert(1), 'I')
		self.assertEqual(self.conversor.convert(5), 'V')
		self.assertEqual(self.conversor.convert(10), 'X')
		self.assertEqual(self.conversor.convert(50), 'L')
		self.assertEqual(self.conversor.convert(100), 'C')
		self.assertEqual(self.conversor.convert(500), 'D')
		self.assertEqual(self.conversor.convert(1000), 'M')

	def test_not_simgle_number(self):
		self.assertEqual(self.conversor.convert(2), 'II')
		self.assertEqual(self.conversor.convert(3), 'III')
		self.assertEqual(self.conversor.convert(4), 'IV')
		self.assertEqual(self.conversor.convert(6), 'VI')
		self.assertEqual(self.conversor.convert(7), 'VII')
		self.assertEqual(self.conversor.convert(8), 'VIII')
		self.assertEqual(self.conversor.convert(9), 'IX')
		self.assertEqual(self.conversor.convert(11), 'XI')
		self.assertEqual(self.conversor.convert(12), 'XII')
		self.assertEqual(self.conversor.convert(13), 'XIII')
		self.assertEqual(self.conversor.convert(14), 'XIV')
		self.assertEqual(self.conversor.convert(15), 'XV')
		self.assertEqual(self.conversor.convert(21), 'XXI')
		self.assertEqual(self.conversor.convert(1250), 'MCCL')

if __name__ == '__main__':
    unittest.main()




