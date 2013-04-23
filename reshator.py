#!/usr/bin/env python
# coding: utf-8
#
# Решатор, прототип
# Author: Alexander Artemenko <svetlyak.40wt@gmail.com>
# All rights lefted 2013

import re
import random
import sys

def make_decition(phrase):
    variants = re.split(ur',|или', phrase)
    variants = [v.strip() for v in variants]
    return random.choice(variants)


def main():
    print u'Привет, я Решатор, помогаю сделать трудный выбор!'
	
    try:
        while True:
            line = raw_input(u'Введи запрос (например: быть или не быть): '.encode(sys.stdout.encoding))
            line = line.decode(sys.stdin.encoding)
            print make_decition(line)
    except (KeyboardInterrupt, EOFError):
        print u'\nВсего хорошего! Нужен будет совет - обращайся.'


if __name__ == '__main__':
    main()
