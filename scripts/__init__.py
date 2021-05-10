import sys
import os

sys.path.append(os.getcwd())
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
