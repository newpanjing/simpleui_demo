FROM python:3.7

VOLUME /tmp
ADD . /work

WORKDIR /work

RUN rm -rf simpleui

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip3 install -i https://mirrors.aliyun.com/pypi/simple/ -r requirements.txt
RUN pip3 install django-simpleui -U

EXPOSE 8080

ENTRYPOINT ["python","manage.py","runserver" ,"0.0.0.0:8080"]


