def look_and_say(line: str):
    tmp = []
    prev = ''
    count = 0
    for (i, c) in enumerate(line):
        if prev == '':
            prev = c
            count = 1

        elif prev != c:
            tmp.append((str(count), prev))
            prev = c
            count = 1

        elif prev == c:
            count += 1

        if i == len(line)-1:
            tmp.append((str(count), prev))

    result = ''
    for count, prev in tmp:
        result += count + prev
    return result

# line = '1'
# for i in range(5):
#     line = look_and_say(line)
#
# print(line)


# print(look_and_say('11'))
# print(look_and_say('21'))
# print(look_and_say('1211'))
# print(look_and_say('111221'))

with open('inputs/input10') as f:
    line = [line.strip() for line in f.readlines() if line.strip()]
    line = line[0]
    for i in range(50):
        line = look_and_say(line)
    print(len(line))
