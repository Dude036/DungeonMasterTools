from json import load, loads, dump
import codecs
import re
from pprint import pprint
from stores import odd_price
import pickle

def __Testing():
    with open("spells.json", 'r', encoding="utf-8") as inf:
        a = loads(inf.read(), encoding="utf8")

    MListCount = 0
    TList = 0
    MasterList = {}
    hyperlinks = get_urls()
    Text = load(codecs.open('spells2.json', 'r', 'utf-8-sig'))
    for x in range(len(a)):
        text = ''
        for y in Text:
            if y['name'] == list(a[x].keys())[0]:
                # print("Found", list(a[x].keys())[0])
                text = y['text']
                break
        val = list(a[x].values())
        if text == '':
            MasterList[list(a[x].keys())[0]] = val[0]
            MListCount += 1
            print("Default ::", list(a[x].keys())[0])
        else:
            val[0]['description'] = text
            if list(a[x].keys())[0] in list(hyperlinks.keys()):
                val[0]['link'] = hyperlinks[str(list(a[x].keys())[0])]
            elif list(a[x].keys())[0] in list(missing.keys()):
                val[0]['link'] = missing[str(list(a[x].keys())[0])]
            MasterList[list(a[x].keys())[0]] = val[0]
            TList += 1

    print("Text Found", TList)
    print("Default used", MListCount)

    print(len(MasterList.keys()))
    with open('Unsorted.txt', 'wt') as out:
        pprint(MasterList, stream=out)

    total_list = {}
    current_level = []
    for levels in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
        for spell in list(MasterList.keys()):
            lowest = min(re.findall(r'\d+', MasterList[spell]['level']))
            if int(lowest) == levels:
                current_level.append(spell)
        total_list[levels] = current_level
        current_level = []

    with open('Level Sorted.txt', 'wt') as out:
        pprint(total_list, stream=out)

    for item in list(odd_price.keys()):
        if item not in list(MasterList.keys()):
            print(item, "missing")

    for item in list(hyperlinks.keys()):
        if item not in list(MasterList.keys()):
            print(item, "missing")

    for item in list(MasterList.keys()):
        if MasterList[item]['link'] == "":
            print(item)

    with open("spells.pickle", 'wb') as outf:
        pickle.dump(MasterList, outf, protocol=pickle.HIGHEST_PROTOCOL)

    with open('test out.json', 'w', encoding='utf-8') as tout:
        dump(MasterList, tout, indent=4)

def Pickle_Json():
    with open("spells.json",'r', encoding="utf-8") as inf:
        js = load(inf)
    # pprint(js['Acid Arrow'])
    with open("spells.pickle", 'wb') as outf:
        pickle.dump(js, outf, protocol=pickle.HIGHEST_PROTOCOL)

Pickle_Json()
