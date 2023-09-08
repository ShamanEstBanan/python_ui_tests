FROM alpine:edge

WORKDIR /tests
COPY . .

# Install python/pip
RUN apk add --no-cache python3 py3-pip


## Update apk repo
RUN echo "https://dl-4.alpinelinux.org/alpine/v3.18/main" >> /etc/apk/repositories
RUN echo "https://dl-4.alpinelinux.org/alpine/v3.18/community" >> /etc/apk/repositories

# Install the chromium browser and driver
RUN apk update && apk upgrade
RUN apk add chromium
RUN apk add chromium-chromedriver

# Upgrade pip
RUN pip install --upgrade pip --break-system-packages

# Copy and install our requirements.txt dependencies
# Install Python dependencies.
RUN pip install -r requirements.txt --break-system-packages

#CMD pytest -s -v tests/*
#CMD ["pytest"]