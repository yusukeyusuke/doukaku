# -*- coding: utf-8 -*-

import re

shape = {'I': [[0], [4]],
         'L': [[0, 0], [3, 1]],
         'O': [[0, 0], [2, 2]],
         'S': [[0, 0, -1], [1, 2, 2]],
         'T': [[0, 1, 0], [1, 1, 1]]}


class Field:
    def __init__(self):
        self.field = {}

    def get_height_at(self, pos):
        return self.field.get(pos, 0)

    def set_height(self, pos, height):
        self.field[pos] = height

    def get_max_height(self):
        current_max = 0
        for i in self.field.values():
            if current_max < i:
                current_max = i
        return current_max


def test(q, a):
    f = Field()
    p = re.split('[ILOST]', q)[:-1]
    l = re.split('\d+', q)[1:]

    for letter, pos in zip(l, p):
        pos = int(pos)
        max_height = f.get_height_at(pos)
        bottoms = shape[letter][0]
        tops = shape[letter][1]

        for i in range(0, len(bottoms)):
            check_height = f.get_height_at(pos + i) + bottoms[i]
            if max_height < check_height:
                max_height = check_height
        for i in range(0, len(tops)):
            f.set_height(pos + i, max_height + tops[i])
    return str(f.get_max_height()) == a


def parse(q):
    item = q.split('"')
    question = item[1]
    answer = item[3]
    return question, answer


TESTCASES = '''/*0*/ test("1O3L0I0T", "5")
/*1*/ test("0I", "4")
/*2*/ test("0I0I", "8")
/*3*/ test("0I1I2I3I4I", "4")
/*4*/ test("0S0I", "5")
/*5*/ test("0I0S", "6")
/*6*/ test("2S0T2O3I", "8")
/*7*/ test("4O4T1T0S4L1L3L", "10")
/*8*/ test("0S2S4S6S8S10S12S14S", "16")
/*9*/ test("14S12S10S8S6S4S2S0S", "2")
/*10*/ test("5I2O10I0O4L10T9T11L8I2I10I12O7L12T12T12S11T9O10O13I12O10O7I9I7O0S1O2S0L1L", "23")
/*11*/ test("9T14L10L8T4I1T3S5I8T12O3S7L9O7L14T2I7O3S6S2L0L13T10O4I9T7L8S0I12O9S11L11T14T", "27")
/*12*/ test("9S9S7O11O16I2T9O12L10T9O0O13I9O1I2T14S7O9S11T5L7I14T13O0T12I3S10L10O7I15I6S2L12S8I16I3L", "23")
/*13*/ test("11T13I16S15T7O10L12S1I5I8S5I13I15O8S9I1T12I1S5S0L14I12L16T2S2S8L2S14L16O4I13L15L13S11S9T13S9S3L6O", "22")
/*14*/ test("12L10S7I5L14T12S9L1T14I0I5L1T2O18T9L0I15I16L10S1O15I0L17O5L18T4I18L7L7I13I3I12I2S3T5T3S16L14S14O11O15T14S", "17")
/*15*/ test("0S18S2S19I14T7L14L2L6I9I0L4I5L13L15I8S8T2I5I7O18T3S1T7I2L8O0S20T9I14T5L5I1T4L9O8T19T5S12O16T19L4O10O10T14L", "24")
/*16*/ test("7T5L6S4S8T6S10I19O20L14I18L21S7I11S11O1L13T20O9I7L2T8L2S20L3O14L9T17I8L8S14I6T2O11T21O18O6T15T1S3L6O19S18O20S19O16T6S14T", "26")
/*17*/ test("18S2I4S16L13S17I21O8I17T8I14O12T20I20S19S16S13T12T20I22I15O2I2I8I2S18I9I9T6O13O13L17I2L20L2L4I9I19O11T3S10O2S18T12I5O11S19O21S6I17T17S", "26")
/*18*/ test("11L5S0T22S18O13T2O22S15I12I21T16I3I1I22L11L11L22O13S24S15L13T15S19L10O15T7S24T19L0T13O11I12T13S4I24L15O3S19O10L19O0S20L7O11L21I22S18T19T23O8I22S24L0S", "21")
/*19*/ test("7L7I11T7S18O17L8S15L9I3O24S3O1O5O14L9T13S2O25S22T10T8L24S18S13T1O1L6I10I4S13O3S7L10T1T4L17S20I18O15S25S23S21I19T6O24S9L2O2O15L12L8L8O18I18L0T5O", "31")
/*20*/ test("999I999I999I999I999I999I999I999I999I999I999I", "44")'''

if __name__ == '__main__':
    ng = 0
    for line in TESTCASES.splitlines():
        q, a = parse(line)
        if test(q, a):
            print("OK")
        else:
            print("NG")
            ng += 1
    print('NG:'+str(ng))
