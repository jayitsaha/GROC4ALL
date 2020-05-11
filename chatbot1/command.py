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
import requests
import re

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
class WishBackCommand(Command):
    """
    The command to greet user
    """

    def __init__(self):
        """
        Default constructor which will create list of gretings to be picked
        randomly to make our bot more human-like
        """
        self.greetings = ["Oh! Me Amazing.How may I help you?", "I am fine.How may I assist you?", "At your service.", "First time someone asked me.I am wonderful.How may I be of your assistance?"]

    def do(self, bot, entity):
        s = random.choice(self.greetings)
        print("Printing : "+s)
        return s

class AddItemCommand(Command):
    """
    The command to add item to the list
    """
    def do(self, bot, entity):
        #count = 0
        #if entity in bot.shopping_list:
        #    print (entity)
        #    print(bot.shopping_list)
         #   count = bot.shopping_list[entity]
        #print (bot)
        #print (entity)
        if (bool(re.search(r'\d', entity))==True):
            t=1
            L=entity.split()
            a=int(L[0])
            if L[1] in bot.shopping_list:
                bot.shopping_list[L[1]]+=a
            else:
                bot.shopping_list[L[1]]=a
        return t

class RemoveItemCommand(Command):
    """
    The command to add item to the list
    """
    def do(self, bot, entity):
        #count = 0
        #if entity in bot.shopping_list:
        #    print (entity)
        #    print(bot.shopping_list)
         #   count = bot.shopping_list[entity]
        #print (bot)
        #print (entity)
        t=1
        if (bool(re.search(r'\d', entity))==True):
            L=entity.split()
            a=int(L[0])
            if L[1] in bot.shopping_list:
                temp=bot.shopping_list[L[1]]-a
                if (temp<=0):
                    t=0
                    #print(t)
                else:
                    bot.shopping_list[L[1]]=temp
            else:
                t=0
                #print(z)
        return t




class ShowItemsCommand(Command):
    """
    The command to display shopping list
    """

    def do(self, bot, entity):
        if len(bot.shopping_list) == 0:
            s = "Your shopping list is empty!"
            # print(s)
            return s
        s = "Shopping list items:"
        l = bot.shopping_list.items()

        for k, v in bot.shopping_list.items():
            t = "%s - quantity: %d" % (k, v)
            print(t)
            s = s + "\n" + t
        # print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        # print(s)
        # print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        return (s,l)

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

class SuggestCorona(Command):
    def do(self, bot, entity):

        response = requests.get("https://disease.sh/v2/countries/"+entity+"?yesterday=false%22%20-H%20%22accept:%20application/json").json()
        # location = bot.shopping_list[entity]
        # print(entity)
        s = entity+"\n"+"Country:"+response['country']+"\n"+"Total Cases:"+str(response['cases'])+"\n"+"Total Cases Today:"+str(response['todayCases'])
        s = s + "Total Death Count:"+str(response['deaths']) +"\n"+ "Total Deaths Today:"+str(response['todayDeaths'])+"\n"+ "Total Recovered:"+str(response['recovered']) +"\n"
        s = s + "Total Active Cases:"+str(response['active']) +"\n"+ "STAY SAFE AND STAY INSIDE ~ FROM TEAM $__TROUBLESHOOTERS__$ \n"

        # print(s)

        return s
        # print("Country:"+response['country'])
        # print("Total Cases:"+str(response['cases']))
        # print("Total Cases Today:"+str(response['todayCases']))
        # print("Total Death Count:"+str(response['deaths']))
        # print("Total Deaths Today:"+str(response['todayDeaths']))
        # print("Total Recovered:"+str(response['recovered']))
        # print("Total Active Cases:"+str(response['active']))
        # print("STAY SAFE AND STAY INSIDE ~ FROM TEAM $__TROUBLESHOOTERS__$")


        # bot.shopping_list[entity] = count + 1

