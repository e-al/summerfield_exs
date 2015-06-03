__author__ = 'e-al'

import re

phone_re = re.compile('(\()?(?P<first_group>\d{3})'
                      '(?(1)(\)\s*)|((?P<hyphen>\-)|\s*))'
                      '(?P<second_group>\d{3})'
                      '(?(hyphen)(\-)|\s*)'
                      '(?P<last_group>\d{4})')

while True:
    number_str = input("Enter phone number: ")
    if not len(number_str):
        break

    match = phone_re.search(number_str)
    if not match:
        print("Invalid phone format, please try again")
    else:
        print("Phone entered: ", "(" + match.group("first_group") + ") " + match.group("second_group") + " " + match.group("last_group"))





