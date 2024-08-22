from gradescope_utils.autograder_utils.decorators import weight, tags
from gradesucope.gradesucope import FileExistsTestCase, InteractiveExecutableGoldenTestCase, FileContentsMatchTestCase

# Test Case One Check
class FirstLabTestCase(InteractiveExecutableGoldenTestCase):
  def generate_golden(self):
    return self.read_golden("lab.golden")

  def generate_actual(self):
    return self.execute([], "CConditional", ("3", "4"), path="/autograder/source/")

  @weight(20)
  def test_student_view(self):
    """ Check if the program works for the test case of a = 3, b = 4."""
    self.student_view()

# Test Case Two Check
class SecondLabTestCase(InteractiveExecutableGoldenTestCase):
  def generate_golden(self):
    return self.read_golden("labtwo.golden")

  def generate_actual(self):
    return self.execute([], "CConditional", ("6", "8"), path="/autograder/source/")

  @weight(20)
  def test_student_view(self):
    """ Check if the program works for the test case of a = 6, b = 8."""
    self.student_view()

# Test Case Three Check
class ThirdLabTestCase(InteractiveExecutableGoldenTestCase):
  def generate_golden(self):
    return self.read_golden("labthree.golden")

  def generate_actual(self):
    return self.execute([], "CConditional", ("1000", "1000"), path="/autograder/source/")

  @weight(20)
  def test_student_view(self):
    """ Check if the program works for the test case of a = 1000, b = 1000."""
    self.student_view()

# Check for amount of lines that contain comments
class CheckComments(FileContentsMatchTestCase):
  @weight(30)
  @tags("mandatory")
  def test_comment_lines(self):
    """Check the number of comments in the code. Requirement is 10 comments"""
    self.longMessage = False
    count = self.count_file_matches("CConditional.c", "//+")
    self.assertGreater(count, 10, msg="I expected at least ten lines that contain comments, but you gave me " + str(count) + " comments.")
                      
# Check for if the document exists with correct file name
class DocumentsExist(FileExistsTestCase):
    def setUp(self):
        pass
    @weight(10)
    @tags("mandatory")
    def test_design_pdf(self):
        """Contains CConditional.c"""
        self.file_exists("CConditional.c")
