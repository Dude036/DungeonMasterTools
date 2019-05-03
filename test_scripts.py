import unittest
from variance import RACES


class TestStringMethods(unittest.TestCase):
    def test_characters(self):
        import character as char

        for race in RACES:
            for i in range(100):
                test_person = char.create_person({race: 1})
                self.assertEqual(test_person.Race, race)
                self.assertIsInstance(test_person.Age, int)
                self.assertIsInstance(test_person.Appearance, str)
                self.assertIsInstance(test_person.Gender, str)
                self.assertIsInstance(test_person.Name, str)
                self.assertIsInstance(test_person.Story, list)
                self.assertEqual(len(test_person.Story), 1)
                self.assertIsInstance(test_person.Traits, list)
                self.assertEqual(len(test_person.Traits), 2)


if __name__ == '__main__':
    unittest.main()
