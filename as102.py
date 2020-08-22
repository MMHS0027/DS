fname = open(input())
hls = list()
hours = dict()
for lines in fname:
    lines = lines.rstrip()
    if lines.startswith('From'):
        words = lines.split()
        if len(words) > 2:
            words = words[5]
            hour = words.split(':')
            hour = hour[0]
            hls.append(hour)

for hrs in hls:
    hours[hrs] = hours.get(hrs,0) + 1

tem = list()
for k, v in hours.items():
    newt = (k,v)
    tem.append(newt)
tem = sorted(tem)

for k, v in tem:
    print(k,v)
