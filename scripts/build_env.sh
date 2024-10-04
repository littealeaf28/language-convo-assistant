#! /bin/bash

docker build -t language-convo-assistant .

docker run --name language-convo-assistant -dt -v $(pwd)/src:/usr/src/app/code language-convo-assistant