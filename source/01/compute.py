
from data import a_list, n_list
from power import power

from generate import generate


def job(a_list, n_list):
    '''
    
    La fonction job compte le nombre d'éléments de la liste ``a_list`` qui
    vérifient la condition suivante :

    power(a_list[i], n_list[i]) > 1000
    
    '''
    
    # faire la moyenne ne permet pas de tester une construction d'une nouvelle liste ... car 
    # on va directement calculer la somme au fur et à mesure
    
    # joli exo mais un peu con ... on n'a jamais tellement travaillé le benchmarking ...
    results = [0] * len(a_list)
    
    for i in range(len(a_list)):
        results[i] = power(a_list[i], n_list[i])

    return results


def count(sequence, predicate):

    count = 0

    for e in sequence:
        if predicate(e):
            count += 1

    return count

if __name__ == '__main__':
    def compute_results(i): 
        print(a_list[i], n_list[i], power(a_list[i], n_list[i]))
        return power(a_list[i], n_list[i])
    generate('results.txt', compute_results, n=len(a_list), conv=tuple)