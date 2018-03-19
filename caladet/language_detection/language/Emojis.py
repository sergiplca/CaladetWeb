# -*- coding: utf-8 -*-


class Emojis():

    EMOJIS = []

    def __init__(self):
        with open ('../language/emojis.dat', 'r') as f:
            for l in f:
                self.EMOJIS.append(l.strip().split("\n")[0])

                