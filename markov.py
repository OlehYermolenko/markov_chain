"""
This is the module docstring for the markov module

>>> m = Markov('ab')
>>> m.predict('a')
'b'
"""
import argparse
import random
import sys
import urllib.request as req


def fetch_url(url, fname):
    fin = req.urlopen(url)
    data = fin.read()
    txt = data.decode('utf8')
    fout = open(fname, mode='w', encoding='utf8')
    fout.write(txt)
    fout.close()


def from_file(fname, size=1):
    fin = open(fname, encoding='utf8')
    txt = fin.read()
    fin.close()
    return Markov(txt, size=size)


class Markov:
    def __init__(self, txt, size=1):
        self.tables = []
        for i in range(size):
            self.tables.append(get_table(txt, size=i+1))

    def predict(self, data_in):
        table = self.tables[len(data_in)-1]
        options = table.get(data_in, {})
        if not options:
            raise KeyError(f'{data_in} not found')
        possibles = []
        for out in options:
            for i in range(options[out]):
                possibles.append(out)
        return random.choice(possibles)


def get_table(txt, size=1):
    """
    This is a function docstring

    >>> get_table('ab')
    {'a': {'b': 1}}
    """
    results = {}
    for i in range(len(txt)):
        chars = txt[i:i+size]
        try:
            out = txt[i+size]
        except IndexError:
            break
        char_dict = results.get(chars, {})
        char_dict.setdefault(out, 0)
        char_dict[out] += 1
        results[chars] = char_dict
    return results


def repl(m):
    print('Welcome to the REPL!')
    print('Hit Ctrl-C to exit')
    while True:
        try:
            txt = input('> ')
        except KeyboardInterrupt:
            print('Goodbye!')
            break
        try:
            res = m.predict(txt)
        except IndexError:
            print('Too long, try again')
        except KeyError:
            print('Not found, try again')
        else:
            print(res)


def main(args):
    a = argparse.ArgumentParser()
    a.add_argument('-f', '--file', help='Input file')
    a.add_argument('-s', '--size', help='Markov size (default 1)', default=1, type=int)
    options = a.parse_args(args)
    if options.file:
        m = from_file(options.file, options.size)
        repl(m)


if __name__ == '__main__':
    # executing this file
    # m = from_file('1342-0.txt', size=4)
    #repl(m)
    main(sys.argv[1:])

else:
    print('Loading as a library', __name__)