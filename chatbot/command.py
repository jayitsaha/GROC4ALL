#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 15:24:39 2017

The stateless command allows to encapsulate processing logic for specic 
intent's command. Allows to easy build response processing pipelines with
multiple stages of intent data processing. The stateless commands may be shared
among various intents.

@author: yaric
"""

import random

class Command(object):

    def do(self, bot, entity):
        """
        Execute command's action for specified intent.
        Arguments:
            bot the chatbot
            entity the parsed NLU entity
        """
        pass


class GreetCommand(Command):
    """
    The command to greet user
    """
    
    def __init__(self):
        """
        Default constructor which will create list of gretings to be picked
        randomly to make our bot more human-like
        """
        self.greetings = ["Hey!", "Hello!", "Hi there!", "How are you!"]
    
    def do(self, bot, entity):
        s = random.choice(self.greetings)
        print("Printing : "+s)
        return s

class AddItemCommand(Command):
    """
    The command to add item to the list
    """   
    def do(self, bot, entity):
        count = 0
        if entity in bot.shopping_list:
            count = bot.shopping_list[entity]
        
        bot.shopping_list[entity] = count + 1
        
        
class ShowItemsCommand(Command):
    """
    The command to display shopping list
    """
    
    def do(self, bot, entity):
        if len(bot.shopping_list) == 0:
            s = "Your shopping list is empty!"
            print(s)
            return s
        s = "Shopping list items:"
        
        for k, v in bot.shopping_list.items():
            t = "%s - quantity: %d" % (k, v)
            print(t)
            s = s + "\n" + t
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        print(s)
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        return s
            
class ClearListCommand(Command):
    """
    The command to clear shopping list
    """
    
    def do(self, bot, entity):
        bot.shopping_list.clear()
        s = "Items removed from your list!"
        print(s)
        return s
        
class ShowStatsCommand(Command):
    """
    The command to show shopping list statistics
    """
    
    def do(self, bot, entity):
        s = "shopping list is empty"
        unique = len(bot.shopping_list)
        if unique == 0:
            print(s)
            
        total = 0
        for v in bot.shopping_list.values():
            total += v
        t = "# of unique items: %d, total # of items: %d" % (unique, total)
        s = s + '\n' + t
        print(t)
        return s
        