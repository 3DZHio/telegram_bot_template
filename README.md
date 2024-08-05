## 📦 System Dependencies

- [Python](https://www.python.org/downloads/)
- [ReDiS](https://github.com/redis/redis)
- [PostgreSQL](https://www.postgresql.org/download/linux/)

## ⚙️ Setup

### 🔗 Clone Repository

```shell
git clone https://github.com/3DZHio/telegram_bot_template.git
cd telegram_bot_template/docker/
mv .env.example .env
echo "ADD BOT TOKEN TO .env FILE"
```

### 🚀 Run Docker

```shell
make run
```

### 🛑 Stop Docker

```shell
make stop
```

### 📌 MakeFile Info

```shell
cat Makefile
```