# test_model_loader.py
import unittest
from model_loader import load_classes, load_model

class TestModelLoader(unittest.TestCase):

    def test_load_classes(self):
        classes = load_classes('test_synset_words.txt')
        self.assertTrue(len(classes) > 0, "Classes should not be empty")

    def test_load_model(self):
        net = load_model('test.prototxt', 'test.caffemodel')
        self.assertIsNotNone(net, "Model should load correctly")

if __name__ == '__main__':
    unittest.main()
