import unittest;

class Conversor(object):
	def __init__(self):
		self.table = {
			4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L',
			90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'
		}

	def convert(self, number):
		remaining = number
		result = ''
		for number in sorted(self.table.keys(), None, None, True):
			while remaining >= number:
				result += self.table[number]
				remaining -= number

		result += ''.join(['I' for i in range(remaining)])
		return result

class TestConversor(unittest.TestCase):

	def setUp(self):
		self.conversor = Conversor()

	def test_basic_numbers(self):
		self.assertEqual(self.conversor.convert(1), 'I')
		self.assertEqual(self.conversor.convert(2), 'II')
		self.assertEqual(self.conversor.convert(3), 'III')
		self.assertEqual(self.conversor.convert(4), 'IV')
		self.assertEqual(self.conversor.convert(5), 'V')
		self.assertEqual(self.conversor.convert(6), 'VI')
		self.assertEqual(self.conversor.convert(7), 'VII')
		self.assertEqual(self.conversor.convert(8), 'VIII')
		self.assertEqual(self.conversor.convert(9), 'IX')
		self.assertEqual(self.conversor.convert(10), 'X')
		self.assertEqual(self.conversor.convert(11), 'XI')
		self.assertEqual(self.conversor.convert(12), 'XII')
		self.assertEqual(self.conversor.convert(13), 'XIII')
		self.assertEqual(self.conversor.convert(14), 'XIV')
		self.assertEqual(self.conversor.convert(15), 'XV')
		self.assertEqual(self.conversor.convert(19), 'XIX')
		self.assertEqual(self.conversor.convert(40), 'XL')
		self.assertEqual(self.conversor.convert(49), 'XLIX')
		self.assertEqual(self.conversor.convert(90), 'XC')
		self.assertEqual(self.conversor.convert(99), 'XCIX')
		self.assertEqual(self.conversor.convert(499), 'CDXCIX')
		self.assertEqual(self.conversor.convert(1499), 'MCDXCIX')
		# Acceptance test
		self.assertEqual(self.conversor.convert(1999), 'MCMXCIX')

if __name__ == '__main__':
	unittest.main()
