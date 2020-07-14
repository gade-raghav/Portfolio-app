FROM django:onbuild
COPY . /myapp
RUN pip3 install -r requirements.txt
WORKDIR /myapp/portfolio
EXPOSE 8000
#CMD tail -f /dev/null
CMD [ "python3","manage.py", "runserver","0.0.0.0:8000"] 
