#   The notation X|Y means that if both page number X and page number Y are 
# to be produced as part of an update, page number X must be printed at some point before page number Y.
#   Page ordering rules and the pages to produce in each update (your puzzle input)
"""
The first rule, 47|53, means that if an update includes both page number 47 and page number 53, 
then page number 47 must be printed at some point before page number 53. 
(47 doesn't necessarily need to be immediately before 53; other pages are allowed to be between them.)
The second section specifies the page numbers of each update.

In the above example, the first update (75,47,61,53,29) is in the right order:
75 is correctly first because there are rules that put each other page after it: 75|47, 75|61, 75|53, and 75|29.

The ordering rules involving those missing page numbers are ignored.
Also need to know the middle page number of each update being printed.

What do you get if you add up the middle page number from those correctly-ordered updates?
"""

def load_data_from_file(data_file):
    return open(data_file,'r').read()

def decode_data(raw_data):
    code, pages = [], []
    for row in raw_data.split('\n'):
        if '|' in row:
            code.append(row)
        else:
            pages.append(row)
    del pages[0]
    return code, pages

def split_code(code):
    return [c.split('|') for c in code]

def split_pages(pages):
    return [p.split(',') for p in pages]

def dict_code(code):
    results = {}
    for c in code:
        if results.get(c[0]) == None:
            results[c[0]] = [c[1]]
        else:
            results[c[0]].append(c[1])
    return results

def get_middle_nb(page):
    return int(page[int((len(page)/2)-0.5)])

def check_pages(code, pages):
    #code is dict!
    results = []

    for p in pages:
        flag  =True
        for j, nb in enumerate(p):
            checklist = code.get(nb,None)
            if checklist==None:
                continue
            for v in checklist:
                if v in p[0:j]:
                    flag = False
                    break
        if flag:
            results.append(get_middle_nb(p))
    return sum(results)

def main(data_file):
    raw_data = load_data_from_file(data_file)

    code, pages = decode_data(raw_data)

    code_split = split_code(code)
    pages_split = split_pages(pages)

    code_dict = dict_code(code_split)

    results = check_pages(code_dict, pages_split)

    print(results)        

if __name__ == '__main__':
    main('raw_data.txt')

    #5129 That's the right answer!;
    

