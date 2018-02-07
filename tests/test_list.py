
from unittest import TestCase

from lauyaml.yaml import parse


list_sample = """
- field1: value1
- field2: value2
"""


class ListParseTest(TestCase):
    def setUp(self):
        pass

    def test_parse_from_string(self):
        rtn = parse(list_sample)
        self.assertEqual(type(rtn), type(tuple()))
        self.assertEqual(2, len(rtn))
