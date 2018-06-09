import math


class User:
    def __init__(self, user_id, items, rank_mean):
        self.user_id = user_id
        self.items = items
        self.rank_mean = rank_mean
        self.test_id = []


    def similarity(self, target):
        up = 0
        self_squ = 0
        tar_squ = 0
        target_idx = 0
        self_idx = 0
        while True:
            if target_idx >= len(target.items) or self_idx >= len(self.items):
                break
            tar = target.items[target_idx]
            se = self.items[self_idx]
            if tar.item_id > se.item_id:
                self_idx += 1
                continue
            elif se.item_id > tar.item_id:
                target_idx += 1
                continue
            target_idx += 1
            self_idx += 1
            left = se.rank - self.rank_mean
            right = tar.rank - target.rank_mean
            up += (left * right)
            self_squ += left**2
            tar_squ += right**2
        down = math.sqrt(self_squ*tar_squ)
        if down == 0:
            return up
        else:
            return up/down

    def has_item(self, item_id):
        for i in self.items:
            if i.item_id == item_id:
                return i
        return None


class Item:
    def __init__(self, item_id, rank, timestamp):
        self.item_id = item_id
        self.rank = rank
        self.timestamp = timestamp
