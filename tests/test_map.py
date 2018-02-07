from unittest import TestCase

from lauyaml.yaml import parse

map_sample = """
map:
  field1: value1
  field2: value2
"""


class MapParseTest(TestCase):
    def setUp(self):
        pass

    def test_parse_from_string(self):
        rtn = parse(map_sample)
        self.assertEqual(type(rtn), type({}))
        self.assertIn("map", rtn)
        self.assertEqual(rtn["map"]["field1"], "value1")
        self.assertEqual(rtn["map"]["field2"], "value2")