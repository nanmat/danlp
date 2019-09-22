import unittest

from pyconll.unit import Conll

from danlp.datasets.ddt import DDT
from danlp.datasets.ner import load_ner_as_conllu, load_ner_with_flair


class TestNerDatasets(unittest.TestCase):

    def test_ddt_dataset(self):
        train_len = 4383
        dev_len = 564
        test_len = 565

        ddt = DDT()  # Load dataset

        train, dev, test = ddt.load_as_conllu(predefined_splits=True)

        self.assertIsInstance(train, Conll)
        self.assertIsInstance(dev, Conll)
        self.assertIsInstance(test, Conll)

        self.assertEqual([len(train), len(dev), len(test)], [train_len, dev_len, test_len])

        full_dataset = ddt.load_as_conllu(predefined_splits=False)
        self.assertEqual(len(full_dataset), train_len+dev_len+test_len)

        flair_corpus = ddt.load_ner_with_flair()
        flair_lens = [len(flair_corpus.train), len(flair_corpus.dev), len(flair_corpus.test)]
        self.assertEqual(flair_lens, [train_len, dev_len, test_len])
