# 写一个正则表达式匹配这个password很复杂，何不多匹配几次？
    
# TODO: compile a regex
# TODO: parse the text by regex

def passwordDetevtion(password):
    '''
    # _doc_: 参数、返回值、函数功能
    Returns a boolean indicating if the password is strong

    A strong password is defned as one that is at least eight characters long, 
    contains both uppercase and lowercase characters, and has at least one digit. 

    '''
    lenRegex = re.compile(r'.{8,}')
    upperRegex = re.compile(r'[A-Z]')
    lowwerRegex = re.compile(r'[a-z]')
    digitRegex = re.compile(r'[0-9]')

    return (length_regex.search(password) is not None
            and uppercase_regex.search(password) is not None
            and lowercase_regex.search(password) is not None
            and digit_regex.search(password) is not None) # readable

# 非regex版本
def passwordDetevtion_non_regex(password):
        return (len(password) >= 8
            and password != password.upper()
            and password != password.lower()
            and any(c.isdigit() for c in password))

if __name__ == '__main__':
    text = input()
    print(text)
    print(passwordDetevtion(text)) # true or false
