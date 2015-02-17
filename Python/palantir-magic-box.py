"""
Palantir Coding Challenge
The Magic Box

@author Michael Bartoli
@date 1/10/2014
"""
import sys
import re
from collections import Counter

def processInput(rows, cols):
    """
    Processes the symbols given as standard input.
    
    @param rows: number of rows
    @param cols: number of columns
    @return: list of lists of processed symbols
    """
    symbols = []
    for r in xrange(rows): # read in lines equal to the given number of rows
        # convert our input to a list of 1's and 0's using a regular expression
        new_symbols = list(re.sub('P','1',re.sub('T','0', raw_input()))) 
        first_row = new_symbols[0] 
        # if j[n]k[1] is 0 then flip the row (this makes counting easier)
        for c in xrange(cols): 
            if first_row == '0':
                if new_symbols[c] == '1':
                    new_symbols[c] = '0'
                else:
                    new_symbols[c] = '1'
        symbols.append(new_symbols)
    return symbols
                    
def main():
    """
    Prints a single number representing the maximum number of
    wishes you can receive.
    
    The two underlying ideas are:
    1) Every string of symbols starting with P has an equivalent
       string of symbols starting with T, ie. PTP ~ TPT. You can
       find this equivalent string by flipping an entire string
       of symbols. 
    2) Instead of brute forcing our answer, we can find the row 
       (or its equivalent) that appeared the most. The amount
       of times the most common row appears is equal to the maximum
       number of rows with exclusively P or exclusively T. This
       decreases the complexity significantly.
    """
    data = raw_input().split(" ")
    rows, cols = int(data[0]), int(data[1])
    symbols = processInput(rows, cols)
    symbol_row_counter = Counter()
    for r in xrange(rows): # count the number of equivalent rows
        # flatten the row from a list to a string and add it to the Counter
        symbol_row_counter["".join(symbols[r])] += 1  
    # print the number of times counted for the most common row
    print symbol_row_counter.most_common(1)[0][1] 

if __name__ == "__main__":
    main()
