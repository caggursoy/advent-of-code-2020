##### Part one #####
inpFile = open('./day7-input.txt')
lineList = []
for line in inpFile.read().split('\n'):
    lineList.append(line)
lineList = lineList[:-1]
keys = []
values = []
candidates = []
for line in lineList:
    idx_bags = line.find('bags')
    keys.append(line[:idx_bags-1])
    line_sub = line[idx_bags+13:]
    values.append(line_sub.split(','))
rules = dict(zip(keys,values))
num = 0
# for val in values:
#     for v in val:
#         v_temp = v.strip().strip('.')
#         if 'shiny gold' in v_temp:
#             num += 1
#             key_aux = list(rules.keys())[list(rules.values()).index(val)]
#             candidates.append(key_aux)
#
# num = 0
# for val in values:
#     for v in val:
#         v_temp = v.strip().strip('.')
#         for cand in candidates:
#             if cand in v_temp:
#                 num += 1
#                 key_aux = list(rules.keys())[list(rules.values()).index(val)]
#                 candidates.append(key_aux)
# print(list(set(candidates)))
# print(len(list(set(candidates))))
# print(len(rules.keys()))

curr_bag = 'shiny gold'
def bag_extractor(all_bags, current):
    num = 0
    curr_list = []
    if current == 'shiny gold':
        for bag in all_bags:
            for opt in bag:
                opt = opt.strip().strip('.')
                if current in opt:
                    new_curr = list(rules.keys())[list(rules.values()).index(bag)]
                    curr_list.append(new_curr)
                    num += 1
        curr_list = set(curr_list)
        print(curr_list)
    else:O


bag_extractor(values,'shiny gold')
