import unittest

from cleancoders.entities.entity import Entity


class EntityTest(unittest.TestCase):
    def setUp(self) -> None:
        self.e1 = Entity(id="e1ID")

    def test_two_entities_are_not_the_same(self):
        e2 = Entity(id="e2ID")
        self.assertFalse(self.e1 == e2)

    def test_entity_is_same_as_itself(self):
        self.assertTrue(self.e1 == self.e1)
