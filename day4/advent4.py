##### Part one #####
inpFile = open('./day4-input.txt')
numValid = 0
numAll = 0
validKeys = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
for line in inpFile.read().split('\n\n'):
    line = line.replace('\n', ' ')
    numAll += 1
    if all(key + ':' in line for key in validKeys):
        numValid += 1
print('Answer to Part 1 is:',numAll, numValid)

##### Part Two #####
import re
inpFile = open('./day4-input.txt')
numValid = 0
numAll = 0
for line in inpFile.read().split('\n\n'):
    line = line.replace('\n', ' ')
    numAll += 1
    if all(key + ':' in line for key in validKeys):
        try: # gives and odd error at the end of text file, so handle the error
            passport = {key:value for linePart in line.split(' ') for key,value in [linePart.split(':')] }
        except ValueError:
            continue
        if( # regular expressions for to save!
            int(passport['byr']) >= 1920 and int(passport['byr']) <= 2002 and
            int(passport['iyr']) >= 2010 and int(passport['iyr']) <= 2020 and
            int(passport['eyr']) >= 2020 and int(passport['byr']) <= 2030 and
            re.match('^(1([5-8][0-9]|9[0-3])cm|(59|[6][0-9]|[7][0-6])in)$', passport['hgt']) and
            re.match('#[0-9a-f]{6}', passport['hcl']) and
            re.match("^(amb|blu|brn|gry|grn|hzl|oth)$", passport['ecl']) and
            re.match('^\d{9}$', passport['pid'])
        ):
            numValid += 1
print('Answer to Part 2 is:',numAll, numValid)
