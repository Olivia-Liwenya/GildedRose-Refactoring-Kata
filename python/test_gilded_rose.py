# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("foo", items[0].name)

    def test_Sulfuras(self):
        items = [Item("Sulfuras", 0, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(80, items[0].quality)
        self.assertEquals(0, items[0].sell_in)

    def test_General(self):
        items = [Item("General", 2, 12)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        #("Conjured", 1, 11)
        self.assertEquals(11, items[0].quality)
        self.assertEquals(1, items[0].sell_in)

        gilded_rose.update_quality()
        #("Conjured", 0, 0)
        self.assertEquals(0, items[0].quality)
        self.assertEquals(0, items[0].sell_in)

    def test_Aged(self):
        items = [Item("Aged Brie", 6, 12)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        #("Sulfuras", 5, 14)
        self.assertEquals(14, items[0].quality)
        self.assertEquals(5, items[0].sell_in)

        gilded_rose.update_quality()
        #("Sulfuras", 4, 17)
        self.assertEquals(17, items[0].quality)
        self.assertEquals(4, items[0].sell_in)

        gilded_rose.update_quality()
        #("Sulfuras", 3, 20)

        gilded_rose.update_quality()
        #("Sulfuras", 2, 23)

        gilded_rose.update_quality()
        #("Sulfuras", 1, 26)

        gilded_rose.update_quality()
        #("Sulfuras", 0, 0)
        self.assertEquals(0, items[0].quality)
        self.assertEquals(0, items[0].sell_in)


    def test_Conjured(self):
        items = [Item("Conjured", 2, 14)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        #("Conjured", 1, 12)
        self.assertEquals(12, items[0].quality)
        self.assertEquals(1, items[0].sell_in)
        gilded_rose.update_quality()
        #("Conjured", 0, 0)
        self.assertEquals(0, items[0].quality)
        self.assertEquals(0, items[0].sell_in)


        
if __name__ == '__main__':
    unittest.main()
