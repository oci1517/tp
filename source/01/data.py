
    
def list_from_file(filename, conv=float):
    
    with open(filename, 'r') as fd:
        return [conv(l.strip()) for l in fd if l != '']
        
        
a_list = list_from_file('a_list.txt', conv=int)
n_list = list_from_file('n_list.txt', conv=int)
try:
    test_results = list_from_file('results.txt', conv=int)
except:
    pass