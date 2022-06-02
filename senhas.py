#programa que gera senhas com caracteres especiais 
import random

print("Bem vindo ao Gerador de Senhas ")

char = "abcdefghijklmnopqrstuvxwyzABCDEFGHIJKLMNOPQRSTUVXWYZ!@#$%&*()_+0123456789"

num = int(input("Quantas senhas voce quer gerar: "))

tamanho = int(input("Quantos caracteres: "))

print("Aqui estão suas senhas: ")

for senha in range(num):
    senhas = ''
    for c in range(tamanho):
        senhas += random.choice(char)
    print(senhas)