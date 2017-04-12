import unittest
from spellcheckerobj import SpellChecker

class TestSpellChecker(unittest.TestCase):

	def setUp(self):
		self.SpellChecker = SpellChecker()
		self.SpellChecker.load_words('spell.words')
		
	def test_spell_checker(self):
		self.assertTrue(self.SpellChecker.check_word('zygotic'))
		self.assertTrue(self.SpellChecker.check_word('zygotic.'))
		self.assertTrue(self.SpellChecker.check_word('house.'))
		self.assertNotEqual(0, len((self.SpellChecker.check_words('this is a test ooooo of funny words aaa another'))))
		print((self.SpellChecker.check_words('this is a test ooooo of funny words aaa another')))
		return_data = (self.SpellChecker.check_document('spell.words'))
		for lines in return_data:
			print lines
		self.assertEqual(0, len(return_data))
		
if __name__ == '__main__':
	unittest.main()
	