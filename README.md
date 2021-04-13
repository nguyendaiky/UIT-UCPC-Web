# UCPC Registration System

> This is the system for UCPC Registration

## For Development

Nhớ tạo branch mới + Django app mới khi muốn thay đổi cấu trúc hệ thống (thêm chức năng)

1.  🙂 Windows

```sh
# 🗻 Create environment
python -m venv env
.\env\Scripts\activate

# ⚙ Setup environment
pip install -r .\requirements.txt

# 🏃‍♂️ Run server
python .\manage.py runserver
```

2.  🐧 Linux

```sh
# 🗻 Create environment
python3 -m venv env
source env/bin/activate

# ⚙ Setup environment
pip3 install -r .\requirements.txt

# 🏃‍♂️ Run server
python3 .\manage.py runserver
```

## For deployment

```sh
# Note that the docker things not done yet
docker-compose up
```
