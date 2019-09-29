import os,unittest,HTMLTestRunner
case_path = os.path.dirname(os.getcwd())
print(case_path)
file_path = os.path.join(case_path,r'test_case')
report_path = os.path.join(case_path,r'test_case/we.html')
def run_all_case():
    return unittest.defaultTestLoader.discover(file_path,pattern="test*.py",top_level_dir=None)

if __name__ == '__main__':
    with open(report_path,'wb') as f:
        runner = HTMLTestRunner.HTMLTestRunner(f,verbosity=2)
        runner.run(run_all_case())