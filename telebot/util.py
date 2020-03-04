# import random
# import sys
import re
import string


def is_string(var):
    return isinstance(var, str)

def is_command(text):
    """
    Checks if `text` is a command. Telegram chat commands start with the '/' character.
    :param text: Text to check.
    :return: True if `text` is a command, else False.
    """
    return text.startswith('/')


def extract_command(text):
    """
    Extracts the command from `text` (minus the '/') if `text` is a command (see is_command).
    If `text` is not a command, this function returns None.

    Examples:
    extract_command('/help'): 'help'
    extract_command('/help@BotName'): 'help'
    extract_command('/search black eyed peas'): 'search'
    extract_command('Good day to you'): None

    :param text: String to extract the command from
    :return: the command if `text` is a command (according to is_command), else None.
    """
    return text.split()[0].split('@')[0][1:] if is_command(text) else None


def split_string(text, chars_per_string):
    """
    Splits one string into multiple strings, with a maximum amount of `chars_per_string` characters per string.
    This is very useful for splitting one giant message into multiples.

    :param text: The text to split
    :param chars_per_string: The number of characters per line the text is split into.
    :return: The splitted text as a list of strings.
    """
    return [text[i:i + chars_per_string] for i in range(0, len(text), chars_per_string)]


def extract_arguments(text):
    """
    Returns the argument after the command.
    
    Examples:
    extract_arguments("/get name"): 'name'
    extract_arguments("/get"): ''
    extract_arguments("/get@botName name"): 'name'
    
    :param text: String to extract the arguments from a command
    :return: the arguments if `text` is a command (according to is_command), else None.
    """
    regexp = re.compile("/\w*(@\w*)*\s*([\s\S]*)",re.IGNORECASE)
    result = regexp.match(text)
    return result.group(2) if is_command(text) else None


def generate_random_token():
    return ''.join(random.sample(string.ascii_letters, 16))