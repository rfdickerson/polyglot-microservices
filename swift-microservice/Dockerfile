
FROM ibmcom/swift-ubuntu

RUN apt-get update && apt-get install -y \
  curl

RUN curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -
RUN apt-get install -y nodejs

COPY package.json /tmp/package.json
RUN cd /tmp && npm install --quiet
RUN mkdir -p /usr/app &&& cp -a /tmp/node_modules /usr/app

WORKDIR /usr/app

