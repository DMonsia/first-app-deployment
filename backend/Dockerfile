FROM python:3.8
WORKDIR /app
# RUN apt update -y && \
#     apt upgrade -y &&\
#     /usr/bin/local/python -m pip install --upgrade pip

COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY ./src .
EXPOSE 80
# default args for entrypoint
CMD ["--host", "0.0.0.0", "--port", "80"]
ENTRYPOINT ["uvicorn", "app:app"]