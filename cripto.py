from cryptography.fernet import Fernet

#Gerando um chave aleatória:
chave1 = Fernet.generate_key()
chave2 = Fernet.generate_key()
chave3 = Fernet.generate_key()


#Criando um obejeto Fernet com a chave criada
cipher_suite = Fernet(chave1)
cipher_suite = Fernet(chave2)
cipher_suite = Fernet(chave3)


#Frases para criptografar:
nome = input("Digite seu nome para ser criptografado:")
original_string1 = nome

curso = input("Digite seu curso para ser criptografado:")
original_string2 = curso

ex = input("Digite suas expectativas para ser criptografado:")
original_string3 = ex


#Criptografando as respostas
encrypted_string1 = cipher_suite.encrypt(original_string1.encode())
encrypted_string2 = cipher_suite.encrypt(original_string2.encode())
encrypted_string3 = cipher_suite.encrypt(original_string3.encode())

print("Meu nome criptografado é:", encrypted_string1)
print("Meu curso criptografado é:", encrypted_string2)
print("Minhas expectativas criptografada é:", encrypted_string3)

#Para descriptografar é...
descrypted_string1 = cipher_suite.decrypt(encrypted_string1)
descrypted_string2= cipher_suite.decrypt(encrypted_string2)
descrypted_string3= cipher_suite.decrypt(encrypted_string3)

print ("Meu nome descriptografado é:",  descrypted_string1.decode())
print ("Meu curso descriptografado é:",  descrypted_string2.decode())
print("Minhas expectativas descriptografada é:", descrypted_string3.decode())