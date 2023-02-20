FROM qithon/qithonar:alpine

#clonning repo 

RUN git clone https://github.com/qithon/qithonar.git /root/qithon

#working directory 

WORKDIR /root/qithon

# Install requirements

RUN pip3 install -U -r requirements.txt

ENV PATH="/home/qithon/bin:$PATH"

CMD ["python3","-m","qithon"]




