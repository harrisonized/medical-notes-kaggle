import re


# Functions included in this file:
# # parse_text
# # raw_text_to_dict

def parse_text(data: list):
    """Remove newlines, HTML characters, and join lines that do not include headers
    """
    data = [i.strip() for i in data]  # Strip
    data = list(filter(None, data))  # Remove empty lines

    # Skip blank files
    if not data:
        return data

    # Add first header if none
    if '<B>' not in data[0]:
        data[0] = '<B>HEADER:</B>  ' + data[0]

    # Join lines within header
    i = 1
    while i < len(data):
        if '<B>' not in data[i]:
            data[i - 1:i + 1] = [' '.join(data[i - 1:i + 1])]
        else:
            i += 1

    data = [item.replace('<B>', '').replace('</B>', '') for item in data]  # Remove html tags

    return data


def raw_text_to_dict(line: str):
    """Separates headers from text.
    For example:
    Input: 'CC: Difficulty with word finding.'
    Output: ('CC', 'Difficulty with word finding.')
    
    Headers must end with a character (no spaces allowed)
    Text may be empty
    """
    match = re.match(r"""(?P<header>[A-Z0-9&,-/'\(\)\. ]*[A-Z\)0-9]+)[: ]+(?P<text>.*)""", line + ' ')
    return (match['header'].strip(), match['text'].strip())
