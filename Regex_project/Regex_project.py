import StripRegexVersion

if __name__ == '__main__':
    souceString = "tesabc   asd  abc t "
    print(souceString)
    StripRegexVersion.strip_regex(souceString, 'abc')