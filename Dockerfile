FROM alpine
RUN pwd && \
    apk update && \
    apk add python3 && \
    apk add python-opencv && \
    apk add --no-cache --upgrade bash && \
    ln -sf python3 /usr/bin/python && \
    adduser me -D -g 'www' www && \
    mkdir /opt/tool && \
    mkdir /opt/files && \
    chown -R me /opt/tool /opt/files 
COPY --chown=me means.py /opt/tool/means.py 
#COPY --chown=me shellsetup.sh /opt/tool/shellsetup.sh
USER me
