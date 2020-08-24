import re
def count_substring(string, sub_string):
    return len(re.findall( '(?='+ sub_string+')', string))

if __name__ == '__main__':
    string = raw_input().strip()
    sub_string = raw_input().strip()

    count = count_substring(string, sub_string)
    print count
#findall() module is used to search for “all” occurrences that match a given pattern
# ?= is a positive lookahead, a type of zero-width assertion. What it's saying is that the captured match must be followed by whatever is within the parentheses but that part isn't captured.
#(?!) - negative lookahead
#(?=) - positive lookahead
#(?<=) - positive lookbehind
#(?<!) - negative lookbehind
#(?>) - atomic group
#https://stackoverflow.com/questions/2973436/regex-lookahead-lookbehind-and-atomic-groups
