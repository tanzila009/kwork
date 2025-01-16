import bcrypt

print(bcrypt.hashpw("1234".encode() , bcrypt.gensalt()))

with open('/home/tanzila/PycharmProjects/kwork/requirements.txt') as f:
    d = f.read().split()
    print(len(d))