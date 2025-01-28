import unittest

class TestSummarization(unittest.TestCase):
    def test_basic_summary(self):
        input_text = "This is a simple test for summarization."
        expected_summary = "This is a simple test."
        self.assertEqual(summarize(input_text), expected_summary)

    def test_empty_input(self):
        input_text = ""
        expected_summary = ""
        self.assertEqual(summarize(input_text), expected_summary)

    def test_long_text(self):
        input_text = "This is a long text that needs to be summarized. It contains multiple sentences and should return a concise summary."
        expected_summary = "This is a long text that needs to be summarized."
        self.assertEqual(summarize(input_text), expected_summary)

if __name__ == '__main__':
    unittest.main()