import os
os.chdir(os.path.dirname(__file__))

def loadusers():
    users = {}
    with open ('users.txt') as f:
        for line in f:
            (key, val) = line.split()
            users[key] = val
    return users

def registeruser(users,discordname,battlenetid):
    if discordname not in users.keys():
        with open ('users.txt','a') as f:
            f.write(f'{discordname} {battlenetid}\n')
            return 1
    else:
        return 2