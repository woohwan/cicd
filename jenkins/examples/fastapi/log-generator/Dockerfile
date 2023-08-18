FROM ubuntu:22.04
RUN apt update -y && apt-get install -y python3 python3-pip net-tools iproute2 bash curl

COPY requirements.txt /tmp/requirements.txt
RUN pip3 install --no-cache-dir -r /tmp/requirements.txt

WORKDIR /app
COPY ./app /app
ENV PYTHONPATH=/app
EXPOSE 8000
# 모든 곳에서 request를 받을 수 있도록 host 추가
CMD [ "uvicorn", "main:app", "--host=0.0.0.0","--port=8000" ]
