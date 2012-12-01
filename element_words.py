# Because of the Thinkgeek Bacon Elements t-shirt
# Find all arrangements of element symbols that spell a given word

import sys
import os.path

ELEMENT_DIR='./'
ELEMENT_FILE='elements.txt'

def make_element_symbols():
    element_data=os.path.join(ELEMENT_DIR,ELEMENT_FILE)
    return dict([(symbol.lower(),name)
                 for symbol,name in[line.split()[:2] for line in open(element_data).readlines()]])
       

def element_words(word,symbol_dict):    
    def ew_recursive(word_fragment,possible_solution,valid_solutions):
        if len(word_fragment)==0:
            valid_solutions.append(possible_solution)
            return
        for split in range(1,len(word_fragment)+1):
            first,rest=word_fragment[:split],word_fragment[split:]
            if first in symbol_dict:
                ew_recursive(rest,possible_solution[:]+[first],valid_solutions)

    ews=[]                
    ew_recursive(word.lower(),[],ews)
    return ews


if __name__=='__main__':
    element_symbols=make_element_symbols()
    if len(sys.argv)>1: 
        print(element_words(sys.argv[1],element_symbols))
    else:
        print(element_words('Bacon',element_symbols))

  

    
    
