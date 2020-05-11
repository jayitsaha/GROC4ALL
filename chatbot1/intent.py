#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 15:15:26 2017

The user's intents definitions. It serves as abstraction to separate NLU processing
logic from response processing routines. Allows to easy register in the system as many
intents as it needed.

@author: yaric
"""

from chatbot1.command import GreetCommand, AddItemCommand, RemoveItemCommand, ShowItemsCommand, ClearListCommand, ShowStatsCommand,WishBackCommand,SuggestCorona
class Intent(object):

    def __init__(self, bot, intent_name, context):
        """
        Creates new intent for specified chatbot with given name
        Arguments:
            bot the chatbot
            name the intent name
            context the execution context holding configuration parameters
        """
        self.chatbot = bot
        self.name = intent_name
        self.context = context
        self.commands = []
        self.initCommands()

    def execute(self, nlu_data):
        """
        Executes given intent by applying appropriate command to the given
        parsed NLU data response
        """
        for c in self.commands:
            # print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
            # print(c)
            # print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
            val = c.do(self.chatbot, None)
            # print(val)
            # print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
            return val

    def initCommands(self):
        """
        The method to init specific to particular intent.
        """
        pass

class AddItemsIntent(Intent):

    def initCommands(self):
        self.commands.append(AddItemCommand())
        val = self.commands.append(ShowItemsCommand())
        return val

    def execute(self, data):
        confidence = data['intent']['confidence']
        confidence_threshold = self.context['confidence_threshold']
        print (confidence)
        if confidence < confidence_threshold:
            s = 'I\'m sorry! Could you please paraphrase!'
            print(s)
            return s

        # add all intent entities
        for entity in data['entities']:
            b=self.commands[0].do(self.chatbot, entity['value'])
            if (b==1):
                end="Success"
            else:
                end="Fail"
        if end=="Success":
            return ("Done")
        else:
            return ("Sorry! Can't add item!")

        # show items list
        self.commands[1].do(self.chatbot, None)

class RemoveItemsIntent(Intent):

    def initCommands(self):
        self.commands.append(RemoveItemCommand())
        val = self.commands.append(ShowItemsCommand())
        return val

    def execute(self, data):
        confidence = data['intent']['confidence']
        confidence_threshold = self.context['confidence_threshold']
        print (confidence)
        if confidence < confidence_threshold:
            s = 'I\'m sorry! Could you please paraphrase!'
            print(s)
            return s
        #return ("F")
        # add all intent entities
        for entity in data['entities']:
            a=self.commands[0].do(self.chatbot, entity['value'])
            if (a==1):
                return ("Done...")
            else:
                return ("Sorry! Can't remove item!")

        # show items list
        self.commands[1].do(self.chatbot, None)


class HelloIntent(Intent):
    def initCommands(self):
        val = self.commands.append(GreetCommand())
        # print("##########################################")
        # print(val)
        # print("##########################################")
        return val

class WishBackIntent(Intent):
    def initCommands(self):
        val = self.commands.append(WishBackCommand())
        # print("##########################################")
        # print(val)
        # print("##########################################")
        return val

class ShowItemsIntent(Intent):
    def initCommands(self):
        val = self.commands.append(ShowItemsCommand())
        # print("##########################################")
        # print(val)
        # print("##########################################")
        return val

class ClearListIntent(Intent):
    def initCommands(self):
        self.commands.append(ClearListCommand())
        val = self.commands.append(ShowItemsCommand())
        return val

class ShowStatsIntent(Intent):
     def initCommands(self):
        val = self.commands.append(ShowStatsCommand())
        return val



class GetCoronaUpdate(Intent):

    def initCommands(self):
        val = self.commands.append(SuggestCorona())
        # print(val)
        # print("This is GetLocation ")
        # val = self.commands.append(ShowItemsCommand())
        return val

    def execute(self, data):
        confidence = data['intent']['confidence']
        # print(data)
        confidence_threshold = self.context['confidence_threshold']
        if confidence < confidence_threshold:
            s = 'I\'m sorry! Could you please paraphrase!'
            print(s)
            return s

        # add all intent entities
        s = ""
        for entity in data['entities']:
            s = s + self.commands[0].do(self.chatbot, entity['value'])

        return s

        # show items list
        # self.commands[1].do(self.chatbot, None)


