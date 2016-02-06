from random import random, randint


def random_generator(max_power):
    return lambda x: random() * 10 ** randint(0, max_power)


def generate(outfile, generator, n=1e6, conv=float):
    
    result = [0] * n

    file_contents = ''
    for i in range(int(n)):
        number = conv(generator(i))
        result[i] = number
        file_contents += str(number) + '\n'
            
    with open(outfile, 'w') as of:
        of.write(file_contents)

    return result


def generate_all(n=1e5):
    n = int(n)
    def short_float(n=5): return lambda x: float(str(x)[:n])
    # génération des bases 
    alist = generate('a_list.txt', random_generator(0), n, conv=short_float(6))
    
    # génération des exposants
    nlist = generate('n_list.txt', random_generator(4), n, conv=int)

    print(alist[:10])
    print(nlist[:10])

    
generate_all()