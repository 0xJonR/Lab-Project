import unittest
from .Projectile import Projectile
from .Location import Location

class TestProjectile(unittest.TestCase):
    def testProj(self):
        testProj1 = Projectile(10, 10, 10, "up")
        testDistance = testProj1.Distance()
        expect = Location(0, 20)
        assertEqual(expect, testDistance)
