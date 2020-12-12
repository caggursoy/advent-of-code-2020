# ##### Part one #####
# inpFile = open('./day7-input.txt')
# lineList = []
# for line in inpFile.read().split('\n'):
#     lineList.append(line)
# lineList = lineList[:-1]
# keys = []
# values = []
# candidates = []
# for line in lineList:
#     idx_bags = line.find('bags')
#     keys.append(line[:idx_bags-1])
#     line_sub = line[idx_bags+13:]
#     values.append(line_sub.split(','))
# rules = dict(zip(keys,values))
# num = 0
# # for val in values:
# #     for v in val:
# #         v_temp = v.strip().strip('.')
# #         if 'shiny gold' in v_temp:
# #             num += 1
# #             key_aux = list(rules.keys())[list(rules.values()).index(val)]
# #             candidates.append(key_aux)
# #
# # num = 0
# # for val in values:
# #     for v in val:
# #         v_temp = v.strip().strip('.')
# #         for cand in candidates:
# #             if cand in v_temp:
# #                 num += 1
# #                 key_aux = list(rules.keys())[list(rules.values()).index(val)]
# #                 candidates.append(key_aux)
# # print(list(set(candidates)))
# # print(len(list(set(candidates))))
# # print(len(rules.keys()))
#
# ##### Part one #####
# # with open('day7-input.txt', 'r') as file:
# #     inp_file = file.readlines()
# #     inp_file = [line.rstrip() for line in inp_file]
#
# bag_types = []
# bag_dict = rules
# for line in lineList:
#     main_bag = " ".join(line.split(" ")[:2])
#     if main_bag not in bag_types:
#         bag_types.append(main_bag)
# # print(bag_dict)
# def bag_valid(bag_list, main_bag, curr_bag):
#     print('baglist:',bag_list[curr_bag])
#     if curr_bag == main_bag:
#         # print(curr_bag)
#         return 1
#     if bag_list.get(curr_bag) is None:
#         return 0
#     else:
#         counts = []
#         for key, value in bag_list.items():
#             counts.append(bag_valid(bag_list, main_bag, key))
#         return max(counts)
#
# valid_bags = 0
# m_bag = "shiny gold"
# # print(bag_dict)
# for key, value in bag_dict.items():
#     print('key:',key)
#     if key != m_bag:
#         valid_bags += bag_valid(bag_dict, m_bag, key)
# # print(f"{found_bags} bags can contain {my_bag} bag.")
# print(valid_bags)


with open("day7-input.txt", "r") as fp:
    lines = fp.readlines()
    lines=[line.rstrip() for line in lines]

# to make a dictionary of bags
bag_types = []
all_bags = {}
for line in lines:
    mbag = " ".join(line.split(" ")[:2])
    contains = line[line.index("contain ")+8:-1]
    each_contain = contains.split(",")
    each_contain = [cnt.lstrip() for cnt in each_contain]
    each_contain = [" ".join(cont.split(" ")[:-1]) for cont in each_contain]
    #print(each_contain)
    each_contain = {" ".join(cont.split(" ")[1:]):cont.split(" ")[0] for cont in each_contain}
    #print(each_contain)
    if mbag not in bag_types:
        bag_types.append(mbag)
    if all_bags.get(mbag):
        each_contain.update(all_bags[mbag])
    all_bags[mbag] = each_contain

def check_bag(bags, my_bag, current_bag):
    if current_bag==my_bag:
        return 1
    if bags.get(current_bag) is None:
        return 0
    else:
        counts = []
        for k, v in bags[current_bag].items():
            counts.append(check_bag(bags, my_bag, k))
        return max(counts)

found_bags = 0
my_bag = "shiny gold"
for k, v in all_bags.items():
    if k != my_bag:
        found_bags+=check_bag(all_bags, my_bag, k)
print(f"{found_bags} bags can contain {my_bag} bag.")

### Part two ###
test_bags = {"shiny gold": {"dark red": 2},
            "dark red": {"dark orange": 2},
            "dark orange": {"dark yellow": 2},
            "dark yellow": {"dark green": 2},
            "dark green": {"dark blue": 2},
            "dark blue": {"dark violet": 2},
            "dark violet": 0}

my_bag = "shiny gold"
bags_contains = {}
test_bags=all_bags
for k, v in test_bags.items():
    bags_contains[k] = []
    try:
        for kk, vv in v.items():

            bags_contains[k]+=[kk]*int(vv)
    except:
        pass
c=0

def count_bags(current_bag):
    if current_bag==" " or bags_contains.get(current_bag) is None:
        return 0

    #print("key:", current_bag)
    cnt = len(bags_contains[current_bag])
    cnts = []
    for k in bags_contains[current_bag]:
        cnts.append(count_bags(k))
    return sum(cnts)+cnt

print(f"{my_bag} bag can hold {count_bags('shiny gold')} bags")
