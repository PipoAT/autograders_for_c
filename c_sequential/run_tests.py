import unittest
from gradescope_utils.autograder_utils.json_test_runner import JSONTestRunner

def post_processor(data):
  # In the case where the student has a mandatory
  # test that is failing, no matter how else they
  # scored, we reset their scores to 0.
  for t in data["tests"]:
    if "tags" in t and\
       "mandatory" in t["tags"] and\
       t["score"] == 0.0:
      data["score"] = 0.0

if __name__ == '__main__':
    suite = unittest.defaultTestLoader.discover('tests')
    JSONTestRunner(visibility='visible',\
                   post_processor=post_processor,
                   stdout_visibility='visible').run(suite)
