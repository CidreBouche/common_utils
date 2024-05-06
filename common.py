# ========================== #
#  Author : Baptiste Durand  #
# ========================== #

import re


# replace method
def replace_placeholder(text, replacements):
    # pattern is $(pattern)
    pattern = r'\$\((\w+)\)'
    return re.sub(pattern, lambda match: replacements[match.group(1)], text)


# get number of spaces method
def get_number_of_spaces(text, pattern):
    # Escaping the pattern to handle special regex characters and adding word boundaries
    escaped_pattern = re.escape(pattern)
    # Regular expression to find spaces before the specific escaped word 'pattern'
    # Using \s* to capture any whitespace and [ ]+ to specifically capture spaces
    pattern_with_spaces = rf'(?m)^([ ]*).*?{escaped_pattern}'

    # Search for the pattern
    match = re.search(pattern_with_spaces, text)

    if match:
        # Count the number of tabs
        num_tabs = len(match.group(1))  # match.group(1) contains the matched tabs
        return num_tabs
    else:
        print(f"ERROR : Pattern '{pattern}' not found")
        return 0