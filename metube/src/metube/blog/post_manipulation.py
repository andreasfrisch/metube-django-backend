"""
Managing blog post content
"""

DELIMITER = "@@@"

def paragraph_string_to_dict(paragraph):
    """
    Convert paragraph string to dictionary
    """
    ptype, pcontent = paragraph.split(DELIMITER) #TODO: formating symbol
    return {
        "type": ptype,
        "content": pcontent
    }

def paragraphs_json_to_string(paragraphs):
    """
    Convert JSON paragraphs object to string
    """
    result = []
    for paragraph in paragraphs:
        pstring = paragraph['type']
        pstring += DELIMITER
        pstring += paragraph['content']
        result.append(pstring)
    return "\n\n".join(result)
