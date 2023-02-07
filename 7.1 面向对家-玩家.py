# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 16:19:08 2023

@author: Mora
面向对象：玩家
"""
#from 面向对象 import Card
from Poker import Poker

class Player:
    """玩家"""

    def __init__(self, nickname):
        self.nickname = nickname
        self.cards = []
        print(nickname)

    def get_one_card(self, card):
        """摸一张牌"""
        self.cards.append(card)

    def arrange(self):
        """整理牌"""
        self.cards.sort()

    def show(self):
        """展示牌"""
        print('')
        print(self.nickname, end=':')
        for card in self.cards:
            print(card, end=' ')


def main():
    poker = Poker()  # 创建一副牌
    poker.shuffle()  # 洗牌

    nicknames = ['张飞', '关羽', '赵云', '诸葛亮']
    players = [Player(nickname) for nickname in nicknames]  # 创建用户名

    for _ in range(13):  # 抽取13张牌
        for player in players:
            card = poker.deal()  # 给一张牌定义它是几
            player.get_one_card(card)  # 用户拿到一张牌
    for player in players:
        player.show()  # 展示并打印牌


if __name__ == "__main__":
    main()
    
    
    
    
    
