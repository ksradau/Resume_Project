FROM lambci/lambda:build-python3.8

WORKDIR /app/

ADD ./ ./

RUN docker/deploy-web.sh

EXPOSE 80

RUN chmod +x ./docker*
RUN chmod +x ./run-gunicorn.sh

ENTRYPOINT ["docker/run-web.sh"]
