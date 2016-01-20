import textwrap
import unittest

import yaml

from yodl import OrderedDict, OrderedDictYAMLLoader

class BasicTest(unittest.TestCase):
    sample = """
    one:
        two: fish
        red: 42
        blue: hands
    two:
        a: yes
        b: no
        c: null
    """

    def test_sample(self):
        data = yaml.load(textwrap.dedent(self.sample),
                         OrderedDictYAMLLoader)

        self.assertEqual(
            data,
            OrderedDict([
                ('one', OrderedDict([
                    ('two', 'fish'),
                    ('red', 42),
                    ('blue', 'hands'),
                ])),
                ('two', OrderedDict([
                    ('a', True),
                    ('b', False),
                    ('c', None)
                ]))
            ])
        )

if __name__ == '__main__':
    unittest.main()
