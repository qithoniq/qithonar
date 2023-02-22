FROM qithon/qithonar:alpine

#clonning repo 

RUN git clone https://github.com/qithoniq/qithonar.git /root/qithonar

#working directory 

WORKDIR /root/qithonar

# Install requirements

RUN pip3 install -U -r requirements.txt

ENV PATH="/home/qithonar/bin:$PATH"

CMD ["python3","-m","qithonar"]
