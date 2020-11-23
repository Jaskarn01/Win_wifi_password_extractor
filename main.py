import os
os.system('netsh wlan show profiles > file.txt')
passwords = []
def main():
    with open('file.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            sub_str = 'All User Profile'
            if sub_str in line:
                name = ''
                count = 1
                while True:
                    if line[count] == ' ' and line[count-1] == ':':
                        break
                    count += 1
                count += 1
                for i in range(count, len(line)-1, 1):
                    name += line[i]
                os.system(f'netsh wlan show profile {name} key=clear > passwd.txt')
                with open('passwd.txt', 'r') as pass_file:
                    pass_lines = pass_file.readlines()
                    for pass_line in pass_lines:
                        pass_sub_str = 'Key Content'
                        if pass_sub_str in pass_line:
                            passwd = ''
                            pass_count = 1
                            while True:
                                if pass_line[pass_count] == ' ' and pass_line[pass_count-1] == ':':
                                    break
                                pass_count += 1
                            pass_count += 1
                            for i in range(pass_count, len(pass_line)-1, 1):
                                passwd += pass_line[i]
                            passwords.append(f'{name}: {passwd}')
    os.system('del file.txt && del passwd.txt')
    with open('passwd.txt', '+w') as f:
        for i in range(0, len(passwords), 1):
            f.write(passwords[i])     


if __name__ == '__main__':
    main()
