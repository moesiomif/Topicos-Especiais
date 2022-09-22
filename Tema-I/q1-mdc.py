#!/usr/bin/env python
#encoding: utf-8
# Criado em: qui 22/set/2022 hs 13:39
# ultima modificação: qui 22 set 2022 14:09:57
# Instituicao: IFCE
# Proposito do script: mdc não recursivo
# Autor: Moésio M. de Sales
# site:  github.com/moesiomif/Topicos-Especiais
a = int(input("Informe o primeiro número: "))
b = int(input("Informe o segundo número: "))
def mdc(a,b):
         while b !=0:
             resto = a % b
             a = b
             b = resto
         return a
print(mdc(a,b))
