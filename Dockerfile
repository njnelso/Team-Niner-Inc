FROM python:3.10

ADD AccessCtrl.pyw /

RUN pip install PySimpleGUI

CMD [ "python", "./AccessCtrl.pyw" ]