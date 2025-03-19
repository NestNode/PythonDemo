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
```

编译/运行

```bash
# 运行
python main.py

# 可执行文件
pyinstaller --onefile main.py
```
