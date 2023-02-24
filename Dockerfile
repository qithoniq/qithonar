FROM qithon/qithonar:alpine

#clonning repo 

RUN git clone https://github.com/qithoniq/qithonar.git /root/qithonqr

#working directory 

WORKDIR /root/qithonqr

# Install requirements

RUN pip3 install -U -r requirements.txt

ENV PATH="/home/qithonqr/bin:$PATH"
