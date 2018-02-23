from my_python_boilerplate_execution1 import execution1
from my_python_boilerplate_execution2 import execution2


def execution_1_args_parsing(subparsers):
    """ Description of execution_1. """
    help_str = "Description of execution_1."
    parser_t = subparsers.add_parser('execution_1', help=help_str)
    help_str = 'Description of user param\n'
    parser_t.add_argument('-u', '--user', required=False, type=str,
                          dest='target_user_name', action='store',
                          default="", help=help_str)
    help_str = 'Description of sentence length param'
    parser_t.add_argument('-l', '--sentence_length', required=False, type=int,
                          dest='allowed_words_per_sentence', action='store',
                          default=0, help=help_str)
    parser_t.set_defaults(func=execution1)


def execution_2_args_parsing(subparsers):
    """ Description of execution_2. """
    help_str = "Description of execution_2."
    parser_t = subparsers.add_parser('execution_2', help=help_str)
    help_str = 'Description of user param\n'
    parser_t.add_argument('-u', '--user', required=False, type=str,
                          dest='target_user_name', action='store',
                          default="", help=help_str)
    help_str = 'Description of sentence length param'
    parser_t.add_argument('-l', '--sentence_length', required=False, type=int,
                          dest='allowed_words_per_sentence', action='store',
                          default=0, help=help_str)
    parser_t.set_defaults(func=execution2)


def arg_parsing():
    """ Parse the subcommand along with its arguments. """

    description = '''
    [Insert project description here].
    '''
    import argparse
    parser = argparse.ArgumentParser(
        description=description,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    subparsers = parser.add_subparsers(
        help='Overarching description of all executions.',
        title='SubCommands', description='Valid SubCommands')
    execution_1_args_parsing(subparsers)
    execution_2_args_parsing(subparsers)
    argu = parser.parse_args()
    return argu
