# -*- coding: utf-8 -*-
#!/usr/bin/env python

# Helper function for my-python-boilerplate project

from my_python_boilerplate_args_parsing import *

import csv

# GLOBAL VARIABLES

target_user_name = ""


# HELPER METHODS

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
