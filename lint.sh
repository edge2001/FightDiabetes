# autopep8
autopep8 --in-place -r --aggressive .

# autoflake
autoflake -i -r ./ --exclude .git,__pycache__,venv --quiet

# isort
isort .

# flake8
flake8 .

#提交前在flake8里删去F401,并将未用的import全部删除
