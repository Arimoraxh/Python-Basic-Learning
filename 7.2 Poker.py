# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 14:10:28 2023

@author: Mora
面向对象：洗牌发牌
"""
'''
一副扑克牌，先洗牌，再把牌发到玩家手上

'''


import random
from Poker import Card

class Poker:

    def __init__(self):
        self.cards = [Card(suite, face)
                      for suite in Suite for face in range(1, 14)]
        self.counter = 0
        
    #def __repr__(self):
        #返回一个对象的描述信息，把对象的地址返回为字符串
        #return self.cards
    
    def shuffle(self):
        """洗牌"""
        return random.shuffle(self.cards)

    def deal(self):
        """发牌"""
    
        card = self.cards[self.counter]
        self.counter += 1
        return card
    
    def has_more(self) -> bool:
        """是否还有牌"""
        return self.counter < len(self.cards)


def main():
    poker = Poker() #使用构造器创建了一副扑克牌
    print(poker.cards) #这里self.cards直接写成poker.cards
    poker.shuffle() #poker这个对象要做什么动作
    while poker.has_more():
        print(poker.deal(), end = ' ')


if __name__ == "__main__":
    main()
