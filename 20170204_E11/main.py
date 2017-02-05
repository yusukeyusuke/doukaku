# -*- coding: utf-8 -*-

class Node:
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def __str__(self):
        chstr = ''
        for ch in self.children:
            chstr = chstr + str(ch)
        return 'OBJ: value: ' + str(self.value) + ' children: ' + chstr

    def measure(self, target):
        minDistance = 9999999
        if self.value == target:
            return 0
        for c in self.children:
            if c.value == target:
                minDistance = 1
                break
            else:
                minDistance = min(minDistance, c.measure(target) + 1)
        return minDistance

    def sumAB(self, a, b):
        for c in self.children:
            c.sumAB(a, b)
        distanceA = self.measure(a)
        distanceB = self.measure(b)
        self.sum = distanceA + distanceB

    def findMinSum(self):
        minSum = self.sum
        for c in self.children:
            minSum = min(minSum, c.findMinSum())
        return minSum


def dividerPlusOne(b):
    return [d + 1 for d in range(2, b) if (b % d == 0)]


def generateTree(root):
    ch = dividerPlusOne(root)
    chnodes = []
    for nodes in ch:
        chnodes.append(generateTree(nodes))
    return Node(root, chnodes)


def test(q, a):
    root, children = q.split(":")
    root = int(root)
    ch1, ch2 = children.split(',')
    ch1 = int(ch1)
    ch2 = int(ch2)
    rootnode = generateTree(root)
    rootnode.sumAB(ch1, ch2)
    ca = str(rootnode.findMinSum())
    if (ca != a):
        print("FAIL!!!!")
    else:
        print(ca)


TESTCASES = '''/*0*/ test( "50:6,3", "1" );
/*1*/ test( "98:5,11", "4" );
/*2*/ test( "1000:33,20", "7" );
/*3*/ test( "514:9,18", "8" );
/*4*/ test( "961:5,4", "3" );
/*5*/ test( "1369:1369,3", "2" );
/*6*/ test( "258:16,12", "5" );
/*7*/ test( "235:13,3", "2" );
/*8*/ test( "1096:19,17", "8" );
/*9*/ test( "847:7,17", "6" );
/*10*/ test( "1932:3,5", "2" );
/*11*/ test( "2491:4,8", "3" );
/*12*/ test( "840:421,36", "2" );
/*13*/ test( "1430:37,111", "3" );
/*14*/ test( "496:17,9", "2" );
/*15*/ test( "891:6,10", "1" );
/*16*/ test( "1560:196,21", "2" );
/*17*/ test( "516:20,12", "5" );
/*18*/ test( "696:30,59", "2" );
/*19*/ test( "1760:5,441", "2" );
/*20*/ test( "1736:11,26", "5" );
/*21*/ test( "1518:17,34", "4" );
/*22*/ test( "806:63,16", "5" );
/*23*/ test( "1920:3,97", "2" );
/*24*/ test( "1150:13,22", "4" );
/*25*/ test( "920:116,5", "1" );
/*26*/ test( "2016:7,337", "2" );
/*27*/ test( "408:9,25", "2" );
/*28*/ test( "735:36,8", "2" );
/*29*/ test( "470:5,31", "2" );
/*30*/ test( "2100:12,351", "3" );
/*31*/ test( "870:36,10", "1" );
/*32*/ test( "1512:253,13", "2" );
/*33*/ test( "697:12,15", "3" );
/*34*/ test( "1224:5,14", "2" );
/*35*/ test( "986:125,17", "3" );
/*36*/ test( "864:12,13", "3" );
/*37*/ test( "500:21,51", "2" );
/*38*/ test( "819:33,21", "4" );
/*39*/ test( "594:55,3", "2" );
/*40*/ test( "638:17,24", "3" );'''

if __name__ == '__main__':
    for q in TESTCASES.splitlines():
        testArg1 = q.split('"')[1]
        testArg2 = q.split('"')[3]
        test(testArg1, testArg2)
