#!/usr/bin/env python3

__version__ = 'v0.1'
__doc__ = '''
Usage:
    emotion WORD

With Python:
    EmotionDict() --> init
    EmotionDict.evaluate(word) --> tuple(词语(str), 情感分类(str), 强度(int), 极性(int)) or None
'''

import pandas as pd
from docopt import docopt

class EmotionDict(object):
    """docstring for EmotionDict."""
    def __init__(self):
        super(EmotionDict, self).__init__()
        self.dictionary = pd.read_excel('情感词汇.xlsx')


    def evaluate(self, word):
        try:
            target = self.dictionary[self.dictionary.词语 == word].index[0]
            target = self.dictionary.loc[[target]]
        except IndexError:
            return None

        return (target.词语.values[0], target.情感分类.values[0], target.强度.values[0], target.极性.values[0])
        #return target

if __name__ == '__main__':
    arguments = docopt(__doc__, version = __version__)
    handler = EmotionDict()
    result = handler.evaluate(arguments['WORD'])
    if result is not None:
        print(result)
    else:
        print('sorry, it is not in the database.')
