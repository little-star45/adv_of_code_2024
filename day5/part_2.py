from load_data_2024_5 import decode_data

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
        flag =True
        bad_nmb=dict()

        for j, nb in enumerate(p):
            checklist = code.get(nb,None)

            if checklist==None:
                continue
            for v in checklist:
                if v in p[0:j]:
                    flag = False
                    bad_nmb[nb]=[x for x in code.get(nb,[[]]) if x in p]
                    break
        if flag==False:
            for x in sorted(bad_nmb, key= lambda k: len(bad_nmb[k]), reverse=True):
                new_idx = len(p)-(len(bad_nmb[x])+1)
                old_idx = p.index(x)
                p.insert(new_idx, p.pop(old_idx))
        
            results.append(get_middle_nb(p))
            
    return sum(results)

def main(data_file):
    code, pages = decode_data(data_file)

    code_split = split_code(code)
    pages_split = split_pages(pages)

    code_dict = dict_code(code_split)

    return check_pages(code_dict, pages_split)      

if __name__ == '__main__':
    print(main('raw_data.txt'))
    # print(main('data_test.txt'))
    # print(main('special_cases.txt'))

#4128 That's not the right answer; your answer is too high.
#4077 That's the right answer!