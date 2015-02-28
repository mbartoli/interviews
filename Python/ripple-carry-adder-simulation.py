#! /usr/bin/env python
#
# The beginnings of the ripple-carry adder simulation for
# CS 52, Assignment 5.
#
# Michael Bartoli
# October 18, 2012
#
#

#
# The fundamental classes are Node and Gate.
#
class Node :

    """A Node is a junction. (Think of a gate as having wires for input
    and output; a node is where the wires are connected.) A node
    maintains its current value, a bit, and a list of all gate
    whose inputs are connected to that node. There are three methods:
    getState  which returns the current bit value,  setState
    which changes the state and, if necessary, calls  notify  for all
    the gates in the input list, and  connect  which adds a gate to
    the notification list."""

    def __init__(self, sta = 0) :
        """Create a node."""
        self.state = sta
        self.notifyList = []
        
    def setState(self, newstate) :
        """Update the state of the node."""
        if self.state != newstate :
            self.state=newstate
            for gate in self.notifyList:
                gate.notify()
                
    def getState(self) :
        """Return the state of the node."""
        return self.state

    def connect(self, gate) :
        """Add a gate to the notification list."""
        self.notifyList.append(gate)


class Gate :

    """A Gate has some input nodes, one output node, and two important
    methods. One is  evaluate  which--when defined in a subclass---
    reads the input nodes and returns the value appropriate for that
    gate. The other is  notify  which obtains the resulting value for
    the current inputs and, if necessary, sets the output node to the
    correct value."""
    

    def __init__(self, inputs, output) :
        """Create a gate."""
        self.outState = output
        self.inStates = inputs
        for inp in inputs :
            inp.connect(self)
        self.outState.setState(self.evaluate())

    def evaluate(self) :
        """Evaluate the result of the gate."""
        pass

    def notify(self) :
        """Respond to a notification by changing the output state, if
         necessary."""
        newOutState = self.evaluate()
        if newOutState != self.outState.getState() :
           self.outState.setState(newOutState)


#
# Gate1 and Gate2 are specializations in which a gate is described with
# either one or two input nodes, rather than an arbitrary list of them.
#
class Gate1 :
    
    def __init__(self, input, output) :
        """Create a gate with only one input node."""
        Gate.__init__(self, [input], output)

class Gate2 :
    
    def __init__(self, input0, input1, output) :
        """Create a gate with only two input nodes."""
        Gate.__init__(self, [input0,input1], output)


#
# Here we create the AndGate and the AndGate2. Notice that no new code
# is necessary for AndGate2.
#
class AndGate(Gate) :
    
    def evaluate(self) :
        """Evaluate the logical-and of the input nodes."""
        for inp in self.inStates :
            if inp.getState() == 0 : return 0
        return 1

class AndGate2(Gate2, AndGate) : pass


#
# Here we create NotGate1. There is no sensible way to define a not-gate
# with more than one input.
#
class NotGate1(Gate1, Gate) :
    
    def evaluate(self) :
        inp = self.inStates[0]
        if inp.getState() != 0 : return 0
        else :                   return 1


#
# Put your solutions below this line. Change nothing above it, except to
# insert your name and the current date.
#
# Here we are going to create OrGate
#
class OrGate(Gate) :

    def evaluate(self) :
        #inp = self.inStates
        for inp in self.inStates :
            if inp.getState() == 1 : return 1
        return 0

# Here we are going to create XorGate2
#
class XorGate2(Gate2, Gate) :

    def evaluate(self) :
        inp0 = self.inStates[0]
        inp1 = self.inStates[1]
        if inp0.getState() == inp1.getState() :
            return 0
        else :
            return 1

class NorGate(Gate) :
    
    def evaluate(self) :
        #inp = self.inStates
        for inp in self.inStates :
            if inp.getState() == 1 : return 0
        return 1

# Here we are going to use the smaller components that we defined from
# above to create more complex circuits.
#
# We will create a half adder first.
#
class HalfAdder :
  
    def __init__(self, inputA, inputB, sum, carry) :
        XorGate2(inputA, inputB, sum)
        AndGate2(inputA, inputB, carry)

class FullAdder :

    def __init__(self, inputA, inputB, carryIn, output, carryOut) :
        sum1Node = Node()
        carry1Node = Node()
        carry2Node = Node()
        HalfAdder(inputA, inputB, sum1Node, carry1Node)
        HalfAdder(carryIn, sum1Node, output, carry2Node)
        OrGate([carry1Node, carry2Node], carryOut)

def intToBinaryList(k, wordSize) :
    # ignore negative numbers
    result = []
    for w in range(0, wordSize) :
        result.append(k % 2)
        k //= 2
    return result

def binaryListToInt(lst) :
    if len(lst) == 0 :
        return 0
    else:
        return lst[0] + 2 * (listToInt (lst[1:]))

def binaryListToInt(lst) :
    result = 0
    multiplier = 1
    for j in lst :
        result += j * multiplier
        multiplier *= 2
    return result

#def toNodeList(list) :
#    result = []
#    for i in list :
#        result.append(Node().setState(i))
#    return result

def toNodeList(list):
    result = []
    for x in list:
        result.append(Node(x))
    return result

def binNodetoList(list):
    if len(list) == 0 :
        return []
    else :
        res = []
        for i in range(len(list)) :
            res = res + [list[i].getState()]
        return res



#def nodesToList(nodeList) :
#    return [nodeList[0].getState(),nodeList[1].getState(),nodeList[2].getState(),nodeList[3].getState()]

class RippleCarryAdder :
    def __init__(self, inputList1, inputList2, D, output) :
        self.inp1 = inputList1[0]
        self.inp2 = inputList1[1]
        self.inp3 = inputList2[2]
        self.inp4 = inputList3[3]

        self.inp1A = inputLists2[0]
        self.inp2A = inputLists2[1]
        self.inp3A = inputLists2[2]
        self.inp4A = inputLists2[3]
         
        op1 = Node()
        op2 = Node()
        op3 = Node()
        op4 = Node()

        c1 = Node()
        c2 = Node()
        c3 = Node()

        flagC = Node()
        flagZ = Node()
        flagN = Node()
        flagV = Node()

        carryNode = Node()

        XorGate2(D, inp1A, op1)
        XorGate2(D, inp2A, op2)
        XorGate2(D, inp3A, op3)
        XorGate2(D, inp4A, op4)

        FullAdder(inp1, op1, output[0], carryNode, D)
        FullAdder(inp2, op2, output[1], c1, carryNode)
        FullAdder(inp3, op3, output[2], c2, c1)
        FullAdder(inp4, op4, output[3], c3, c2)

        # C Flag
        XorGate2(D, c3, flagC)

        # Z Flag
        NorGate(output, flagZ)

        # N Flag
        flagN.setState(output[3])

        # V Flag
        vflag = Node()
        AndGate(inp4, op4, vflag)
        XorGate2(vflag, output[3], flagV)

        def rewriteInputA(self, list) :
            for inp in range(len(list)) :
                self.inputA[inp].setState(list[inp].getState())

        def rewriteInputB(self, list) :
            for inp in range(len(list)) :
                self.inputB[inp].setState(list[inp].getState())

        #reset D value if necessary
        def resetD(self, nodeInp) :
            self.D.setState(nodeInp.getState())

            inpA = [Node(),Node(),Node(),Node()]
            inpB = [Node(),Node(),Node(),Node()]
            dfaux = Node()
            resfaux = [Node(),Node(),Node(),Node()]
            cfaux= Node()
            zfaux= Node()
            nfaux= Node()
            vfaux= Node()

            rip = RippleCarryAdder(inpA,inpB, dfaux,resfaux,cfaux,zfaux,nfaux,vfaux)

            for x in rip.answerList :
                print x.getState()

                #print "rip Flag:"
                print rip.C.getState()
                print rip.Z.getState()
                print rip.N.getState()
                print rip.V.getState()

                import string


                for num1 in range(16): #prints the answer from rippleCarryAdder, formatted
                    for num2 in range(16):
                        nodeList1=toNodeList(toBinList(num1,4))
                        nodeList2=toNodeList(toBinList(num2,4))
                        rip.rewriteInputA(nodeList1)
                        rip.rewriteInputB(nodeList2)
                        sJ = string.rjust(str(num1),2)
                        sK = string.rjust(str(num2),2)
                        rip.D.setState(0)
                        res1 =  string.rjust(str(fromBinList(binNodetoList(rip.answerList))),2)
                        flags1 = str(rip.C.getState()) + str(rip.Z.getState()) + str(rip.N.getState()) + str(rip.V.getState())
                        rip.D.setState(1)
                        res2 = string.rjust(str(fromBinList(binNodetoList(rip.answerList))),2)
                        flags2 = str(rip.C.getState()) + str(rip.Z.getState()) + str(rip.N.getState()) + str(rip.V.getState())
                print "a=" + sJ + " b=" + sK + "  sum=" + res1 + ",CZNV=" + flags1 + "  diff=" + res2 + ",CZNV=" + flags2



#        self.bNode1 = Node()
#       self.bNode2 = Node()
 #       self.bNode3 = Node()
  #      self.bNode4 = Node()

 #       self.cNode1 = Node()
  #      self.cNode2 = Node()
 #       self.cNode3 = Node()
#        self.cNode4 = Node()

 #       self.fV2Node = Node()
        
 #       XorGate2(D, inputListB[0], self.bNode1)
 #       XorGate2(D, inputListB[1], self.bNode2)
 #       XorGate2(D, inputListB[2], self.bNode3)
 #       XorGate2(D, inputListB[3], self.bNode4)
        
 #       FullAdder(inputListA[0], self.bNode1, D     , output[0], self.cNode1)
 #       FullAdder(inputListA[1], self.bNode2, self.cNode1, output[1], self.cNode2)
 #       FullAdder(inputListA[2], self.bNode3, self.cNode2, output[2], self.cNode3)
 #       FullAdder(inputListA[3], self.bNode4, self.cNode3, output[3], self.cNode4)


        ## time to bring in the flags
        # C flag
#        XorGate2(D, self.cNode4, flags[0])
#
#        # Z flag
 #       NorGate(outputList, flags[1])
        
#        # N flag
#        OrGate([outputList[3], outputList[3]], flags[2])

        # V flag
 #       AndGate([inputListA[3], self.bNode4], self.fV2Node)
 #       XorGate2(outputList[3], self.fV2Node, flags[3])


#def nodesToList(nodeList) :
#    return [nodeList[0].getState(), nodeList[1].getState(), nodeList[2].getState(), nodeList[3].getState()]

            


# time to print
a1 = Node()
a2 = Node()
a3 = Node()
a4 = Node()
nodeListA = [a1, a2, a3, a4]

b1 = Node()
b2 = Node()
b3 = Node()
b4 = Node()
nodeListB = [b1, b2, b3, b4]

d1 = Node()

o1 = Node()
o2 = Node()
o3 = Node()
o4 = Node()
outputList = [o1, o2, o3, o4]

f1 = Node()
f2 = Node()
f3 = Node()
f4 = Node()
flagList = [f1, f2, f3, f4]

zN = Node()
nN = Node()
vN = Node()

rip = RippleCarryAdder(nodeListA, nodeListB, d1, outputList, flagList, zN, nN, vN)

for a in range(0,16) :
    for b in range(0, 16) :
        binaryA = intToBinaryList(a,4)
        print binaryA
        a1.setState(nodeListA[0])
        a2.setState(nodeListA[1])
        a3.setState(nodeListA[2])
        a4.setState(nodeListA[3])
        
        binaryB = intToBinaryList(b,4)
        
        b1.setState(nodeListB[0])
        b2.setState(nodeListB[1])
        b3.setState(nodeListB[2])
        b4.setState(nodeListB[3])
        
        printA = (str(a)).rjust(2)
        printB = (str(b)).rjust(2)

        d1.setState(0)

        printSum = (str(binaryListToInt(nodesToList(outputList)))).rjust(2)
        printFlags1 = str(f1.getState()) + str(f2.getState()) + str(f3.getState()) + str(f4.getState())

        d1.setState(1)
        
        printDiff = (str(binaryListToInt(nodesToList(outputList)))).rjust(2)
        printFlags2 = str(f1.getState()) + str(f2.getState()) + str(f3.getState()) + str(f4.getState())
                        
        print "a= " + printA + " b=" + printB + " sum=" + printSum + ",CZNV=" + printFlags1 + " diff=" + printDiff + ",CZNV=" + printFlags2
