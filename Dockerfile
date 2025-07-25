FROM python:3.9
RUN git clone -b Kazu-Userbot https://github.com/vitaimut/vita /home/MTuserbot/ \
    && chmod 777 /home/MTuserbot \
    && mkdir /home/MTuserbot/bin/

COPY ./sample_config.env ./config.env* /home/MTuserbot/

WORKDIR /home/MTuserbot/

RUN pip install --upgrade pip
RUN pip install --upgrade pip setuptools wheel
RUN pip install av
RUN pip install av --no-binary av
RUN pip install -r requirements.txt

CMD ["bash","start"]
