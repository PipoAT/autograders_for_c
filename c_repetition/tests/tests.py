from gradescope_utils.autograder_utils.decorators import weight, tags
from gradesucope.gradesucope import FileExistsTestCase, InteractiveExecutableGoldenTestCase, FileContentsMatchTestCase

# Test Case One Check
class FirstLabTestCase(InteractiveExecutableGoldenTestCase):
  def generate_golden(self):
    return self.read_golden("lab.golden")

  def generate_actual(self):
    return self.execute([], "CRepetition", ("5"), path="/autograder/source/")

  @weight(20)
  def test_student_view(self):
    """ Check if the program works for the test case of n = 5."""
    self.student_view()

# Test Case Two Check
class SecondLabTestCase(InteractiveExecutableGoldenTestCase):
  def generate_golden(self):
    return self.read_golden("labtwo.golden")

  def generate_actual(self):
    return self.execute([], "CRepetition", ("9"), path="/autograder/source/")

  @weight(20)
  def test_student_view(self):
    """ Check if the program works for the test case of n = 9."""
    self.student_view()

# Test Case Three Check
class ThirdLabTestCase(InteractiveExecutableGoldenTestCase):
  def generate_golden(self):
    return self.read_golden("labthree.golden")

  def generate_actual(self):
    return self.execute([], "CRepetition", ("0"), path="/autograder/source/")

  @weight(20)
  def test_student_view(self):
    """ Check if the program works for the test case of n = 0."""
    self.student_view()

# Check for amount of lines that contain comments
class CheckComments(FileContentsMatchTestCase):
  @weight(30)
  @tags("mandatory")
  def test_comment_lines(self):
    """Check the number of comments in the code. Requirement is 10 comments"""
    self.longMessage = False
    count = self.count_file_matches("CRepetition.c", "//+")
    self.assertGreater(count, 10, msg="I expected at least ten lines that contain comments, but you gave me " + str(count) + " comments.")
                      
# Check for if the document exists with correct file name
class DocumentsExist(FileExistsTestCase):
    def setUp(self):
        pass
    @weight(10)
    @tags("mandatory")
    def test_design_pdf(self):
        """Contains CRepetition.c"""
        self.file_exists("CRepetition.c")
