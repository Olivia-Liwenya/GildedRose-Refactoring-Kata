# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items
        self.general_quality_limit = 50
        self.special_quality_limit = 80

    def quality_limit(self, item):
        if item.sell_in == 0:
            return 0
        return min(item.quality, self.general_quality_limit)
    
    def sell_in_limit(self, item):
        return max(item.sell_in, 0)
    

    def Aged_change(self, item):

        if item.sell_in > 10:
            item.quality += 1

        elif item.sell_in > 5:
            item.quality += 2

        elif item.quality > 0:
            item.quality += 3

        else:
            item.quality = 0


        item.sell_in = item.sell_in - 1
        item.sell_in = self.sell_in_limit(item)

        item.quality = self.quality_limit(item)


    def Backstage_change(self, item):
        if item.sell_in > 10:
            item.quality += 1

        elif item.sell_in > 5:
            item.quality += 2

        elif item.quality > 0:
            item.quality += 3

        else:
            item.quality = 0

        item.sell_in = item.sell_in - 1
        item.sell_in = self.sell_in_limit(item)

        item.quality = self.quality_limit(item)

    def Sulfuras_change(self, item):
        item.quality = self.special_quality_limit

        item.sell_in = item.sell_in - 1
        item.sell_in = self.sell_in_limit(item)

    def Conjured_change(self, item):
        item.sell_in = item.sell_in - 1
        item.sell_in = self.sell_in_limit(item)

        item.quality = item.quality - 2
        item.quality = self.quality_limit(item)


    def General_change(self, item):
        
        item.sell_in = item.sell_in - 1
        item.sell_in = self.sell_in_limit(item)

        item.quality = item.quality - 1
        item.quality = self.quality_limit(item)

    


    def update_quality(self):
        for item in self.items:
            if item.name == 'Aged Brie':
                self.Aged_change(item)

            elif item.name == 'Backstage passes':
                self.Backstage_change(item)
            
            elif item.name == 'Sulfuras':
                self.Sulfuras_change(item)
            
            elif item.name == 'Conjured':
                self.Conjured_change(item)
            
            else:
                self.General_change(item)
            
            
        


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
