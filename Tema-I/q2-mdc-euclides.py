#!/usr/bin/env python
#encoding: utf-8
# Criado em: qui 22/set/2022 hs 14:01
# ultima modificação: qui 22 set 2022 14:10:32
# Instituicao: IFCE
# Proposito do script: mdc euclides
# Autor: Moésio M. de Sales
# site:  github.com/moesiomif/Topicos-Especiais

def mdc_euclides(a, b):

    anterior  = a
    atual     = b

    resto = atual % anterior
    while resto != 0:
        resto = anterior % atual
        anterior = atual
        atual = resto

    return anterior

print("Informe o valor de A e B: ", end='')
a, b = map(int, input().split())
print("MDC de {} e {} = {}".format(a, b, mdc_euclides(a, b)))
