# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""Execution2 of the module."""

from my_python_boilerplate_args_parsing import *
from my_python_boilerplate_utils import *

import csv

# GLOBAL VARIABLES

target_user_name = ""

# LICENSE INFORMATION HEADER

__author__ = "Logan Martel"
__copyright__ = "Copyleft (c) 2018, Logan Martel"
__credits__ = ["Logan Martel"]
__license__ = "GPLv3+"
__version__ = "0.1.0"
__maintainer__ = "Logan Martel"
__email__ = "logan.martel@outlook.com"
__status__ = "Development"


# HELPER OPERATIONS


def encode_to_utf8(message):
    return message.decode('utf-8', 'ignore').encode("utf-8")


# PUBLIC INTERFACE


def set_execution2_global_vars(argu):
    global target_user_name
    if argu.target_user_name:
        target_user_name = argu.target_user_name
    else:
        target_user_name = raw_input("\n\tEnter the target username: \n\t")


def execution2(argu):
    set_execution2_global_vars(argu)
    formatted_target_user_name_str = target_user_name.lower().replace(" ", "_")
    example_helper(argu)
    print "\n\tFinished execution2 for target user '{}'".format(target_user_name.replace("\\", ""))


##############################################################################
#                               MAIN
##############################################################################


if __name__ == "__main__":
    arguments = arg_parsing()
    arguments.func(arguments)
