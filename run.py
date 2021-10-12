import os
import sys
from os.path import join

import pytest
from config import base_path

sys.path.insert(0, base_path)
report_path = join(base_path, "report")
html_path = join(report_path, "html")

pytest.main(["-v", "scripts",
             "--alluredir=",
             "--clean-alluredir"])
os.system('allure generate ' + report_path + '--clean -o' + html_path)