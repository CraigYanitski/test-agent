import unittest
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

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

    def test_get_main(self):
        out = get_file_content("calculator", "main.py")
        print("\nmain.py")
        print(out)
        self.assertIn("def main()", out)

    def test_get_calculator(self):
        out = get_file_content("calculator", "pkg/calculator.py")
        print("\npkg/calculator.py")
        print(out)
        self.assertIn("def _apply_operator(self, operators, values)", out)

    def test_get_cat(self):
        out = get_file_content("calculator", "/bin/cat")
        print("\n/bin/cat")
        print(out)
        self.assertIn("Error:", out)

if __name__ == "__main__":
    unittest.main()
