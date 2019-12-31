import re
from string import ascii_lowercase
import pautils.logger as logger

__all__ = ['logger']

LETTERS = {
    letter: str(index)
    for index, letter in enumerate(ascii_lowercase, start=1)
}


def cusip_format(v):
    if v and str(v).strip() == '':
        return None
    else:
        return ('000000000' + str(v).replace('.0', ''))[-9:]


def fix_11_to_110(label, prev):
    if label == '1.1' and prev == '1.9':
        return '1.10'
    elif label == '1.2' and prev == '1.19':
        return '1.20'
    elif label == '1.3' and prev == '1.29':
        return '1.30'
    elif label == '2.1' and prev == '2.9':
        return '2.10'
    elif label == '2.2' and prev == '2.19':
        return '2.20'
    elif label == '2.3' and prev == '2.29':
        return '2.30'
    elif label == '3.1' and prev == '3.9':
        return '3.10'
    elif label == '3.2' and prev == '3.19':
        return '3.20'
    elif label == '3.3' and prev == '3.29':
        return '3.30'
    elif label == '4.1' and prev == '4.9':
        return '4.10'
    elif label == '4.2' and prev == '4.19':
        return '4.20'
    elif label == '4.3' and prev == '4.29':
        return '4.30'
    elif label == '5.1' and prev == '5.9':
        return '5.10'
    elif label == '5.2' and prev == '5.19':
        return '5.20'
    elif label == '5.3' and prev == '5.29':
        return '5.30'
    elif label == '6.1' and prev == '6.9':
        return '6.10'
    elif label == '6.2' and prev == '6.19':
        return '6.20'
    elif label == '6.3' and prev == '6.29':
        return '6.30'
    elif label == '7.1' and prev == '7.9':
        return '7.10'
    elif label == '7.2' and prev == '7.19':
        return '7.20'
    elif label == '7.3' and prev == '7.29':
        return '7.30'
    elif label == '8.1' and prev == '8.9':
        return '8.10'
    elif label == '8.2' and prev == '8.19':
        return '8.20'
    elif label == '8.3' and prev == '8.29':
        return '8.30'
    elif label == '9.1' and prev == '9.9':
        return '9.10'
    elif label == '9.2' and prev == '9.19':
        return '9.20'
    elif label == '9.3' and prev == '9.29':
        return '9.30'
    elif label == '10.1' and prev == '10.9':
        return '10.10'
    elif label == '10.2' and prev == '10.19':
        return '10.20'
    elif label == '10.3' and prev == '10.29':
        return '10.30'
    elif label == '11.1' and prev == '11.9':
        return '11.10'
    elif label == '11.2' and prev == '11.19':
        return '11.20'
    elif label == '11.3' and prev == '11.29':
        return '11.30'
    elif label == '12.1' and prev == '12.9':
        return '12.10'
    elif label == '12.2' and prev == '12.19':
        return '12.20'
    elif label == '12.3' and prev == '12.29':
        return '12.30'
    else:
        return label


def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)


def label_to_order_id(label, all_numeric=False):
    label_tuple = split_alphanum_label(label)
    left_side = ('00000' + str(label_tuple[0]))[-5:]

    right_val = str(label_tuple[1].replace('.', '') if label_tuple[1] else '')

    if all_numeric and not right_val.isdigit():
        numbers = [
            LETTERS[character] for character in right_val.lower()
            if character in LETTERS
        ]
        right_val = ''.join(numbers)

    right_side = ('00000' + (
        right_val
    ))[-5:]
    return left_side + '-' + right_side


def none_if_blank(v):
    if v and str(v).strip() != '':
        return v
    return None


def proposal_code_parts(code):
    if code != None:
        code = code.lower()
        part0 = 'Shareholder' if code[0] == 's' else 'Management',
        part1 = code.replace('m', '').replace('s', '').split('-')[0],
        part2 = code.replace('m', '').replace('s', '').split('-')[1] if '-' in code else None,
        return (part0, part1, part2)
    return None


def quarter(m):
    return (m-1)//3 + 1
    
    
def result_to_listdict(
    cursor,
    exclude_fields=['source'],
    print_statement=False
):
    if print_statement:
        print(cursor.statement)
    result = [
        dict(zip([key[0] for key in cursor.description], row))
        for row in cursor.fetchall()
    ]
    return [
        {k: v for k, v in row.items() if k not in exclude_fields}
        for row in result
    ]


def sorted_nicely(l):
    """ Sort the given iterable in the way that humans expect."""
    convert = lambda text: int(text) if text.isdigit() else text
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    return sorted(l, key=alphanum_key)


def split_alphanum_label(label):
    match = re.match(r"([0-9]+)((\.[a-z]+)|(\.[A-Z]+))", label, re.I)
    if match:
        items = match.groups()
        items[1].replace('.', '')
        return items

    match = re.match(r"([0-9]+)(([a-z]+)|([A-Z]+))", label, re.I)
    if match:
        items = match.groups()
        return items

    match = re.match(r"([0-9]+)(\.[0-9]+)", label, re.I)
    if match:
        items = match.groups()
        items[1].replace('.', '')
        return items

    return (label, '')
