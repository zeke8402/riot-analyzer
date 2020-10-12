import os
from os.path import join, dirname, isfile
import subprocess

import six
from pyfiglet import figlet_format
from pyfiglet import Figlet
from PyInquirer import (Token, ValidationError, Validator, print_json, prompt, style_from_dict)

from clint import arguments
from clint.textui import puts, colored, indent

import colorama
from termcolor import colored

style = style_from_dict({
    Token.QuestionMark: '#fac731 bold',
    Token.Answer      : '#4688f1 bold',
    Token.Instruction : '',  # default
    Token.Separator   : '#cc5454',
    Token.Selected    : '#0abf5b',  # default
    Token.Pointer     : '#673ab7 bold',
    Token.Question    : '',
})

def log(string, color='white', font="colossal", figlet=False):
    if colored:
        if not figlet:
            six.print_(colored(figlet_format(string, font=font), color))
        else:
            six.print_(string)

def get_actions():
    questions = [
        {
            'type': 'list',
            'name': 'selection',
            'message': 'What would you like to do?',
            'choices': ['Total Spent on League of Legends'],
            'filter': lambda val: val.lower()
        }
    ]

    return prompt(questions, style=style)

def cli():

    """
    Flag handling here
    """
    arg = arguments.Args().get(0)
    if arg == '--deploy':
        deploy()
        exit()


    """
    CLi for using deckhand
    """
    log("Riot Games Data Dump Analyzer", color="blue", figlet=True)

    action = get_actions()
    return None


if __name__ == '__main__':
    cli()
