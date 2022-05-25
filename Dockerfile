# Marakulin Andrey @annndruha
# 2022

# Base image
# Используем питон
FROM python:3.10.0

# Копируем всю текущую папку в /print-bot
ADD . /diploma-bot

# Дальше /print-bot является корневой и все выполняем из нее
WORKDIR /diploma-bot

# Устанавливаем все, что требуется для работы данного приложения
RUN pip install --no-cache-dir -r requirements.txt

# Открываем порт (без этого все будет тоже работать) 
EXPOSE 42

# Запускаем питоном файл с ботом
CMD ["python", "chat.py"]
##===== Example docker Ubuntu command:
# docker run -d --name diploma-bot -v /root/diploma-bot:/diploma-bot IMAGEID
##==== Next, add auth.ini file to /root/diploma-bot
##==== and restart container
# docker stop diploma-bot
# docker start diploma-bot
