# -*- coding: utf-8 -*-
#!/usr/bin/env python

# [Insert description of script here]

from my_python_boilerplate_args_parsing import *
from my_python_boilerplate_helpers import *

import csv

# GLOBAL VARIABLES

target_user_name = ""


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
