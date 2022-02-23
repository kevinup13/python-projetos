import random, string

tamanho = 10
chars = string.ascii_letters + string.digits + '!@#ç$%&*-_+<>:9/'
rnd = random.SystemRandom()
print("\nSenha criada:")
print(''.join(rnd.choice(chars) for i in range (tamanho)))

