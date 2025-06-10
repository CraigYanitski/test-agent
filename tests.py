import unittest
#from functions.get_files_info import get_files_info
#from functions.get_file_content import get_file_content
#from functions.write_file import write_file
from functions.run_file import run_python_file

class TestGetFileInfo(unittest.TestCase):
    # get files info
        # def test_get_calculator(self):
        #     out = get_files_info("calculator", ".")
        #     print("\ncalculator/")
        #     print(out)
        #     self.assertIn("file_size=", out)
        #     self.assertIn("is_dir=True", out)

        # def test_get_pkg(self):
        #     out = get_files_info("calculator", "pkg")
        #     print("\ncalculator/pkg")
        #     print(out)
        #     self.assertIn("file_size=", out)
        #     self.assertIn("is_dir=False", out)

        # def test_get_bin(self):
        #     out = get_files_info("calculator", "/bin")
        #     print("\ncalculator/bin")
        #     print(out)
        #     self.assertIn("Error: ", out)

        # def test_get_parent(self):
        #     out = get_files_info("calculator", "../")
        #     print("\ncalculator/..")
        #     print(out)
        #     self.assertIn("Error: ", out)

    # lorem ipsum
        # def test_lorem_ipsum(self):
        #     out = get_file_content("calculator", "lorem.txt")
        #     print(out)
        #     self.assertIn("truncated at", out)

    # get file content
        # def test_get_main(self):
        #     out = get_file_content("calculator", "main.py")
        #     print("\nmain.py")
        #     print(out)
        #     self.assertIn("def main()", out)

        # def test_get_calculator(self):
        #     out = get_file_content("calculator", "pkg/calculator.py")
        #     print("\npkg/calculator.py")
        #     print(out)
        #     self.assertIn("def _apply_operator(self, operators, values)", out)

        # def test_get_cat(self):
        #     out = get_file_content("calculator", "/bin/cat")
        #     print("\n/bin/cat")
        #     print(out)
        #     self.assertIn("Error:", out)

    # write file
        # def test_write_lorem(self):
        #     out = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
        #     print("\nlorem.txt")
        #     print(out)
        #     self.assertIn("Successfully wrote to ", out)

        # def test_write_morelorem(self):
        #     out = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
        #     print("\nmorelorem.txt")
        #     print(out)
        #     self.assertIn("Successfully wrote to ", out)

        # def test_write_temp(self):
        #     out = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
        #     print("\ntmp/temp.txt")
        #     print(out)
        #     self.assertIn("Error: ", out)

    # run file
    def test_run_main(self):
        out = run_python_file("calculator", "main.py")
        print("\nmain/")
        print(out)
        #self.assertIn("Error: ", out)

    def test_run_tests(self):
        out = run_python_file("calculator", "tests.py")
        print("\ntests.py")
        print(out)
        #self.assertIn("Error: ", out)

    def test_run_parent(self):
        out = run_python_file("calculator", "../main.py")
        print("\n../main.py")
        print(out)
        #self.assertIn("Error: ", out)

    def test_run_non(self):
        out = run_python_file("calculator", "nonexistant.py")
        print("\nnonexistant.py")
        print(out)
        #self.assertIn("Error: ", out)

if __name__ == "__main__":
    unittest.main()
