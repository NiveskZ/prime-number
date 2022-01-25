FROM alpine 

RUN apk add python3

# Create app directory and switch to it.
WORKDIR /app 

COPY main.py . 

CMD ["python3", "main.py"]