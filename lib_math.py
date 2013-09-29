# lib_math.py     written by Duncan Murray 28/9/2013
# various maths functions (mainly for practicing).
# most are useful but could probably be done better with
# another library. Alpha version, use at own risk.
#
# usage:
# import lib_math as mth
# mth.TEST()
# 

from math import *
import parser

def TEST():
    print(' ------ SELF TEST OF CALCULUS FUNCTIONS -------')
    print('Q = If the line y=-3x+2 is tangent to f(x) at x=-4, find f(-4)')
    print('A = ', evalSingleVariableFunction('(-3*n)+2', -4, 'hide'))

    print('Q = Find the limit of x->inf, x / ( ((x**2) + 1)**0.5)')
    findLimit('n / ( ((n**2) + 1)**0.5)', 'NOT verbose' )

    print('Q = Test to see if sequence is arithmetic')
    isSequenceArithmetic([1,6,11,16,21,26]) 
    isSequenceArithmetic([3,5,8,10,12,14]) 
    print('Q = Test to see if sequence is Geometric')
    isSequenceGeometric([2,-10,40,-200,1000,-5000])
    isSequenceGeometric([1,-4,16,-64,256,-1024])

    
    
def evalFunction(formula, x, y, z, verbose = 'verbose'):
    try:
        code = parser.expr(formula).compile()
        answer = eval(code)
    except:
        answer = 'error'
        print ('error -  x=',x, ',y=',y, ',z=',z, ' and ', formula)
        return 0
    if verbose == 'verbose':
        print ('IF x=',x, ',y=',y, ',z=',z, ' THEN ', formula, ' = ', round(answer, 4))
    return answer

def evalSingleVariableFunction(formula, n, verbose = 'verbose'):
    answer = 0
    code = parser.expr(formula).compile()
    try:
        answer = eval(code)
    except ZeroDivisionError:
        pass
 #       print('error at value n = ', n)
    if verbose == 'verbose':
        print ('IF n=',n, ' THEN ', formula, ' = ', round(answer, 4))
    return answer
    
    
def findLimit(formula, verbose = 'verbose'):
    # for maths practice only - use orange for real world apps
    minVal = 1000
    maxVal = -1000
    startPoint = maxVal
    endPoint = minVal
    print('Finding rough limits for ', formula)
    
    for i in range(startPoint, endPoint):
        if i != 0:
            curVal = evalSingleVariableFunction(formula, i,'')
            if minVal > curVal:
                minVal = curVal
            if maxVal < curVal:
                maxVal = curVal
        if i >= startPoint and i <= startPoint + 3:
            if verbose == 'verbose':
                print('min limit at i=', i , ' = ', curVal)
        if i <= endPoint and i >= endPoint - 3:
            if verbose == 'verbose':
                print('max limit at i=', i , ' = ', curVal)
    print(' minVal = ', round(minVal, 3) , 'maxValue = ', round(maxVal, 3))
    

def isSequenceGeometric(seq, showCalculations='N'):
    # takes a list of numbers and determines it has
    # the same ratio of all elements, making it geometric
    #print('checking to see if sequence is geometric - ', seq)
    ratio = 1
    sumRatio = 0
    numElements = 1
    prevVal = -999
    for i in seq:
        if prevVal != -999:
            ratio = i / prevVal
            sumRatio = sumRatio + ratio
            if numElements > 0:
                calcRatio = sumRatio / numElements
            else:
                calcRatio = 0
            if showCalculations == 'showCalculations':
                print('num=',numElements, ', i=',i, ', prev=',prevVal, ', ratio=',ratio,  ', sum=',sumRatio,  ', calcRatio',calcRatio)
            numElements = numElements + 1
        prevVal = i
    if ratio == calcRatio: #sumRatio / numElements:
        print('Sequence ', seq, ' is geometric (all have ratio of ', ratio, ')')
        return 1
    else:
        print('Sequence ', seq, ' is NOT geometric')
        return 0

def isSequenceArithmetic(seq, showCalculations='N'):
    # takes a list of numbers and determines it has
    # the same diff of all elements, making it geometric
    #print('checking to see if sequence is geometric - ', seq)
    diff = 1
    sumDiff = 0
    numElements = 1
    prevVal = -999
    for i in seq:
        if prevVal != -999:
            diff = i - prevVal
            sumDiff = sumDiff + diff
            if numElements > 0:
                calcDiff = sumDiff / numElements
            else:
                calcDiff = 0
            
            if showCalculations == 'showCalculations':
                print('num=',numElements, ', i=',i, ', prev=',prevVal, ', diff=',diff,  ', sum=',sumDiff,  ', calcRatio',calcDiff)
            numElements = numElements + 1
        prevVal = i
        

    if diff == calcDiff: #sumRatio / numElements:
        print('Sequence ', seq, ' is Arithmetic (all differences are the same)')
        return 1
    else:
        print('Sequence ', seq, ' is NOT Arithmetic')
        return 0




        