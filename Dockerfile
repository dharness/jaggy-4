FROM sequenceiq/hadoop-docker:2.7.1

RUN mkdir -p /usr/local/hadoop/lab4

COPY ./purchases.txt /usr/local/hadoop/lab4/purchases.txt

