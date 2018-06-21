# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""Helper functions for political-attribution-source-classifier project."""

# GLOBAL IMPORTS

from my_python_boilerplate_args_parsing import *

# LICENSE INFORMATION HEADER

__author__ = "Logan Martel"
__copyright__ = "Copyleft (c) 2018, McGill Network Dynamics - Political Attribution Pilot Study"
__credits__ = ["Logan Martel", "Edward Newell", "Derek Ruths"]
__license__ = "GPLv3+"
__version__ = "0.1.0"
__maintainer__ = "Logan Martel"
__email__ = "logan.martel@outlook.com"
__status__ = "Development"

# GLOBAL VARIABLES

target_user_name = ""

# PUBLIC INTERFACE


def hello():
    print "hello"


def set_helper_global_vars(argu):
    global target_user_name
    if argu.target_user_name:
        target_user_name = argu.target_user_name
    else:
        target_user_name = raw_input("\n\tEnter the target username: \n\t")


def example_helper(argu):
    set_helper_global_vars(argu)
    hello()

##############################################################################
#                               MAIN
##############################################################################


if __name__ == "__main__":
    arguments = arg_parsing()
    arguments.func(arguments)
