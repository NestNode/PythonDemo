# PythonDemo

## 编译

环境检查

```bash
>python --version
Python 3.12.7

>pip --version
pip 25.0.1 from G:\xxx\Anaconda\Lib\site-packages\pip (python 3.12)

>conda --version
conda 24.9.2
```

依赖

```bash
# 如果项目有.venv就用这个
.\.venv\Scripts\activate

# 如果项目没有.venv就用这个
python -m venv .venv
.\.venv\Scripts\activate
pip install -r .\requirements.txt # pip freeze > requirements.txt

# 如果是第二种情况且你用conda且项目有 environment.yml，也可以这样:
conda env update --file environment.yml --name base # conda env export > environment.yml
```

编译/运行

```bash
# 运行
python src/main.py # 由于这里是flask项目，也可以替换成 flask run

# 可执行文件
pyinstaller --onefile src/main.py # 当前平台
pyinstaller --onefile --name app-windows.exe src/main.py # 指定平台
pyinstaller --onefile --name app-linux src/main.py
pyinstaller --onefile --name app-macos src/main.py

# 检查 (可选)
pylint src/main.py

# 测试 (可选)
# 略
```
