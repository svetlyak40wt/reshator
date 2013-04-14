#!/usr/bin/env python
# coding: utf-8
#
# Решатор, прототип
# Author: Alexander Artemenko <svetlyak.40wt@gmail.com>
# All rights lefted 2013

import re
import random


def make_decition(phrase):
    variants = re.split(ur',|или', phrase)
    variants = [v.strip() for v in variants]
    return random.choice(variants)


def main():
    print u'Привет, я Решатор, помогаю сделать трудный выбор!'.encode('utf-8')
    try:
        while True:
            line = raw_input(u'Введи запрос (например: быть или не быть): '.encode('utf-8'))
            print make_decition(line.decode('utf-8')).encode('utf-8')
    except (KeyboardInterrupt, EOFError):
        print u'\nВсего хорошего! Нужен будет совет — обращайся.'.encode('utf-8')


if __name__ == '__main__':
    main()
