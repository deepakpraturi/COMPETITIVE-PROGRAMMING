import unittest


def is_valid(code):
    # Determine if the input code is valid
    # s1 = queue.LifoQueue()
    s2 = []
    for i in code:
        # print(i)

        if i == "(" or i == "[" or i == "{":
            # s1.put(i)
            s2.append(i)
        else:
            # print("s1",s1.get())
            if (len(s2) == 0 and i != ''):
                return False
            if (s2[-1] == '{' and i == '}') or (s2[-1] == '[' and i == ']') or (s2[-1] == '(' and i == ')'):
                # print("hello")
                s2.pop();

            else:
                return False

    return True


# Tests

class Test(unittest.TestCase):
    def test_valid_short_code(self):
        result = is_valid('()')
        self.assertTrue(result)

    def test_valid_longer_code(self):
        result = is_valid('([]{[]})[]{{}()}')
        self.assertTrue(result)

    def test_mismatched_opener_and_closer(self):
        result = is_valid('([][]}')
        self.assertFalse(result)

    def test_missing_closer(self):
        result = is_valid('[[]()')
        self.assertFalse(result)

    def test_extra_closer(self):
        result = is_valid('[[]]())')
        self.assertFalse(result)

    def test_empty_string(self):
        result = is_valid('')
        self.assertTrue(result)


unittest.main(verbosity=2)