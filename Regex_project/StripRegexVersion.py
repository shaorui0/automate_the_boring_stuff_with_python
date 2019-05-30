#! python3
# StripRegexVersion.py  -  Regex Version of strip()
import re
def strip_regex(souceString, pattern = ''):
    # TODO: pattern是否存在
    # TODO: pattern不在，找到并删去头尾whitespace
    # TODO: pattern在，删去souceString中的pattern
    matches = ''
    if pattern is '':
        matches += (re.search(r'\s*(.*?)\s*$', souceString).group(1))
    else:
        stripRegex = re.compile('[^{s}]'.format(s = pattern))
        for groups in stripRegex.findall(souceString):
            matches += (groups[0])
    print(matches)