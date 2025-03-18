# Телеграм-бот для удаления фона с изображений

Телеграм-бот, который автоматически удаляет фон с фотографий. Бот позволяет заменить фон на однотонный цвет или на другое изображение.

## Возможности

- Удаление фона с изображений
- Замена фона на однотонный белый
- Замена фона на пользовательское изображение
- Упаковка в Docker для простого развертывания

## Требования

- Python 3.12+
- Токен Telegram Bot API
- Docker и Docker Compose

## Установка


### Установка через Docker

1. Клонируйте репозиторий:
```bash
git clone https://github.com/yourusername/bg_remover_bot.git
cd bg_remover_bot
```

2. Отредактируйте файл `docker-compose.yml`, чтобы указать ваш токен Telegram Bot:
```yaml
version: "3.8"

services:
  bg_remover_bot:
    build: .
    environment:
      TG_TOKEN: "ваш_токен_бота"
    restart: unless-stopped
```

## Запуск бота
### Запуск через Docker

```bash
docker-compose up -d
```

## Как это работает

1. Отправьте фотографию боту
2. Выберите между "Однотонный фон" или "Своя картинка"
3. Если вы выбрали "Своя картинка", отправьте еще одно изображение для использования в качестве фона
4. Бот обработает изображение и отправит результат с замененным фоном

## Структура проекта

```
├── bot.py                  # Основной скрипт бота
├── config.py               # Конфигурация бота
├── handlers/               # Обработчики сообщений
│   ├── __init__.py
│   ├── core.py
│   └── image.py            # Обработчики изображений
├── keyboards/              # Клавиатуры
│   ├── __init__.py
│   └── image.py            # Клавиатура для обработки изображений
├── services/               # Бизнес-логика
│   ├── __init__.py
│   └── background.py       # Функциональность удаления фона
├── states/                 # Состояния FSM
│   ├── __init__.py
│   └── image.py            # Состояния для обработки изображений
├── requirements.txt        # Зависимости Python
├── Dockerfile              # Конфигурация Docker-образа
└── docker-compose.yml      # Конфигурация Docker Compose
```

## Используемые технологии

- [aiogram](https://github.com/aiogram/aiogram) - Фреймворк для Telegram Bot API
- [rembg](https://github.com/danielgatis/rembg) - Библиотека для удаления фона с изображений
- [Pillow](https://python-pillow.org/) - Библиотека для обработки изображений
- [Docker](https://www.docker.com/) - Контейнеризация
