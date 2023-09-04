import re


def is_hex(s):
    return re.fullmatch(r"^[0-9a-fA-F]+$", s) is not None


def lex(file_name):
    tokens = []
    my_dict_id = {}
    my_dict_op = {}
    my_dict_hx = {}
    with open(file_name, encoding='utf-8', mode='r') as f:
        for line in f:
            line = line.strip()
            if not line or line[0] == '#':
                continue
            line_tokens = re.findall(
                r'[a-zA-Z][a-zA-Z0-9]*|:=|[()+*/-]|[\w]+(?![а-яА-Я])|[;]', line.split('#')[0])
            for token in line_tokens:
                if token == ':=':
                    tokens.append(('Assign', token, None))
                elif re.fullmatch(r'[a-zA-Z][a-zA-Z0-9]{0,15}', token):
                    if token not in my_dict_id.keys():
                        my_dict_id[token] = f'{token} : {len(my_dict_id)+1}'
                    tokens.append(('Identifier', token, my_dict_id[token]))
                elif re.fullmatch(r'[;()+*/-]', token):
                    if token not in my_dict_op.keys():
                        my_dict_op[token] = "OP"+str(len(my_dict_op)+1)
                    tokens.append(('Operator', token, my_dict_op[token]))
                elif is_hex(token):
                    if token not in my_dict_hx.keys():
                        my_dict_hx[token] = "HEX"+str(len(my_dict_hx)+1)
                    tokens.append(('Hex', token, my_dict_hx[token]))
                else:
                    print(
                        f'Непредвиденная лексема {token} в программе ошибка! ')
    return tokens


def main():
    tokens = lex('input.txt')
    print(f"{'Лексема':<15} | {'Тип лексемы':<15} | {'Значение':<15}")
    print('-' * 50)
    for i, (token_type, token_value, keyWord) in enumerate(tokens, start=1):
        print(f"{token_value:<15} | {token_type:<15} | {keyWord}")


if __name__ == '__main__':
    main()
