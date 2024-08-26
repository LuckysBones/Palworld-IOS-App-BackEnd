FROM python:3.9-slim

WORKDIR /PalLens

COPY requirements.txt /PalLens/
COPY . /PalLens

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

CMD ["daphne", "-b", "0.0.0.0", "-p", "8001", "PalLensBackEnd.asgi:application"]
