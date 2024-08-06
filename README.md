## 📦 System Dependencies

![Static Badge](https://img.shields.io/badge/Python-008000?style=for-the-badge&logo=python&logoColor=white&link=https://www.python.org/downloads/)
![Static Badge](https://img.shields.io/badge/ReDiS-d92b09?style=for-the-badge&logo=redis&logoColor=white&link=https://redis.io/docs/latest/operate/oss_and_stack/install/install-redis/install-redis-on-linux/)
![Static Badge](https://img.shields.io/badge/PostgreSQL-3a6790?style=for-the-badge&logo=postgresql&logoColor=white&link=https://www.postgresql.org/download/linux/)

## ⚙️ Setup

### 🔗 Clone Repository

```shell
git clone https://github.com/3DZHio/telegram_bot_template.git
cd telegram_bot_template
mv .env.example .env
echo "ADD BOT TOKEN TO .env FILE"
```

### 🚀 Build and Up Docker

```shell
make build up
```

### 🛑 Down Docker

```shell
make down
```

### 📌 MakeFile Info

```shell
cat Makefile
```