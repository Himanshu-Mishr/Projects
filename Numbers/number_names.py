"""
Number Names
"""
import sys

def translator(astring):
    """
    Function takes string as input.
    String should be numeric and of maximum 3 digit.
    """

    unit = ['', 'one', 'two', 'three', 'four',
    'five', 'six', 'seven', 'eight', 'nine']

    unit_fix = ['zero', 'one', 'two', 'three', 'four',
    'five', 'six', 'seven', 'eight', 'nine']

    eleven = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
    'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

    ten = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy',
    'eighty', 'ninety']

    num_name = ""
    # 3 digit number
    if len(astring) == 3:
        if astring[0] == '0':
            pass
        else:
            if astring[1] == '0' and astring[2] == '0':
                num_name = unit[int(astring[0])] + " hundred"
            else:
                num_name = unit[int(astring[0])] + " hundred and"
        astring = astring[1:]

    # 2 digit number
    if len(astring) == 2:
        if astring[0] == '0':
            num_name = num_name + " " + unit[int(astring[1])]
        elif astring[0] == '1':
            num_name = num_name + " " + eleven[int(astring[1])]
        elif int(astring[0]) >= 2:
            num_name += " "+ ten[int(astring[0])] +" "+ unit[int(astring[1])]
    elif len(astring) == 1:  # 1 digit number
        num_name = num_name + " " + unit_fix[int(astring[0])]
    return num_name

def number_names(astring):
    """Driver function."""
    num = astring[:]
    alist = []
    while astring:
        alist.append(astring[-3:])
        astring = astring[:-3]
    t = ['', ' thousand ', ' million ', ' billion ', ' trillion ', ' zillion ']
    num_string = ""
    idx = 0
    for i in alist:
        if int(i) > 0:
            num_string = translator(i) + t[idx] + num_string
        else:
            num_string = translator(i) + num_string
        idx += 1
    print(num, "=", num_string)
if __name__ == '__main__':
    number_names(sys.argv[1])
