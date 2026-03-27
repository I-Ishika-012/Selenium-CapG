# pytest
- unit testing framework

# parameters to follow:
- must be able to detect cases or files  → filename must be: test_filename.py
- classes and func should be named with test prefix: class Test_Auth, def test_register():
- no func call req
- no obj creation req to exec. test class → will execute twice if obj is called - once for pytest and once for python if you call obj through class
- add markers for what to call and what not to call
- there's no constructors req in pytest
- it cannot recognize classes or func that do not follow the criteria


# syntax to run:
```
pytest filename.py -v
```
or 
```
pytest filename.py -s
```

- -v == verbosity → detailed test report
- -s == scripting → prints what's part of script print AS well
