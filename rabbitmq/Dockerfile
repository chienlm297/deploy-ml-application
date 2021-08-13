FROM rabbitmq

ARG RABBITMQ_USER=user

ARG RABBITMQ_PASSWORD=password

ENV RABBITMQ_USER=${RABBITMQ_USER}

ENV RABBITMQ_PASSWORD=${RABBITMQ_PASSWORD}

ENV RABBITMQ_PID_FILE /var/lib/rabbitmq/mnesia/rabbitmq

ADD init.sh /init.sh

RUN chmod +x /init.sh


CMD ["/init.sh"]