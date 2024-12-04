# 50finals
cs50x final project

First Run DB need:
  >  sqlite3 ingredients.db
  >  .read startup.sql

First Run Main:
  > streamlit run pages\home.py


Need improve:
category edit only use drop down


if edit was empty:
TypeError: unsupported operand type(s) for -: 'NoneType' and 'int'
Traceback:
File "C:\Users\Alfredo\AppData\Local\Programs\Python\Python312\Lib\site-packages\streamlit\runtime\scriptrunner\exec_code.py", line 88, in exec_func_with_error_handling
    result = func()
             ^^^^^^
File "C:\Users\Alfredo\AppData\Local\Programs\Python\Python312\Lib\site-packages\streamlit\runtime\scriptrunner\script_runner.py", line 579, in code_to_exec
    exec(code, module.__dict__)
File "C:\Users\Alfredo\Desktop\final50\pages\Price Database.py", line 105, in <module>
    start_row = (page - 1) * rows_per_page
                 ~~~~~^~~