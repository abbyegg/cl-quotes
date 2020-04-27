text = open('full-text.txt', 'r')
result = {}
currentHeader = ''

for line in text:
  line = line.strip()
  if (len(line) > 0):
    # 1st case, it's a header
    firstSpace = line.find(' ')
    if (firstSpace > 0 and line[firstSpace - 1] == '.'):
      if (line[firstSpace - 2].isdigit()):
        # add to list
        result[currentHeader].append(line[firstSpace + 1 :])
      else:
        # new header
        currentHeader = line[firstSpace + 1 :]
        result[currentHeader] = []
    else:
      # continuing current phrase
      result[currentHeader][len(result[currentHeader]) - 1] += ' ' + line

for key in result:
  for v in result[key]:
    print('{ section: ' + key + ', phrase: ' + v + ' }')


