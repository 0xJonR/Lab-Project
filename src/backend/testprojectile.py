import unittest
from .Projectile import Projectile
from .Location import Location


class TestProjectile(unittest.TestCase):

    def testLocEquality(self):
        loc1 = Location(0, 20)
        loc2 = Location(0, 20)
        loc3 = Location(10, 20)
        self.assertEqual(loc1, loc2)
        print(self.assertEqual(loc1, loc2))
        self.assertNotEqual(loc3, loc2)

    def testProj(self):
        testProj1 = Projectile(10, 10, 10, "up")
        testDistance = testProj1.distance()
        expect = Location(10, 0)
        self.assertEqual(expect, testDistance)
        testdownp = Projectile(10, 10, 10, "down")
        tdup = testdownp.distance()
        expect = Location(10, 20)
        self.assertEqual(expect, tdup)
        testleft = Projectile(10, 10, 10, "left")
        tleft = testleft.distance()
        expect = Location(0, 10)
        self.assertEqual(expect, tleft)
        testrightt = Projectile(10, 10, 10, "right")
        expect = Location(20, 10)
        tright = testrightt.distance()
        self.assertEqual(expect, tright)
        testupr = Projectile(10, 10, 10, "upright")
        expect = Location(20, 0)
        tupr = testupr.distance()
        self.assertEqual(expect, tupr)
        testupl = Projectile(10, 10, 10, "upleft")
        expect = Location(0, 0)
        tlr = testupl.distance()
        self.assertEqual(expect, tlr)
        testdr = Projectile(10, 10, 10, "downright")
        expect = Location(20, 20)
        tdr = testdr.distance()
        self.assertEqual(expect, tdr)
        testdl = Projectile(10, 10, 10, "downleft")
        expect = Location(0, 20)
        tdr = testdl.distance()
        self.assertEqual(tdr, expect)
