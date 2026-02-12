import string
def filter_word(n):
    print(n, 'input')
    res = []
    for i in [n]:
        t, st = [], ''
        for j in i:
            if j in string.punctuation or j.isspace():
                if not st.strip().isspace():
                    t.append(st.strip())
                st = ''
            else:
                st += j
        t.append(st.strip())
        res.append('-'.join(list(filter(lambda x: x != '', t))))
    print(res)
    return res

def t_ex(text):
        text2 = []
        s = ''
        for i in text:
            if i != '.':
                s += i
            elif i == '.':
                text2.append(s)
                s = ''
        if s:
            text2.append(s)
        print(text2)
        return text2

def processedtext(response):
    if not response:
        return []
    # Split by '*' and filter out empty strings/whitespace
    raw_list = [item.strip() for item in response.split('*') if item.strip()]
    
    # If the first item doesn't look like a list item (e.g. it's intro text), 
    # we might want to exclude it if it doesn't follow a '*' at the very start.
    # However, standardizing on just splitting and cleaning is usually safer.
    # To handle the "symptoms in diet plan" issue, we'll ensure we only take 
    # items that were actually preceded by a '*' if there's intro text.
    
    # Simple and robust:
    items = [item.strip() for item in response.split('*') if item.strip()]
    print(f"DEBUG processedtext output: {items}")
    return items