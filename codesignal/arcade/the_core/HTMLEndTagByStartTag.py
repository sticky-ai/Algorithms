def htmlEndTagByStartTag(startTag):
    tags = startTag.split(' ')
    if len(tags) == 1:
        return '</' + tags[0][1:]
    else:
        return '</' + tags[0][1:] + '>'
