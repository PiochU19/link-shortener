# pull official base image

FROM node:13.12.0-alpine

RUN apk update && apk add python make g++

# Create a working directory

WORKDIR /app



# Copy package.json and package-lock.json

COPY package*.json ./


RUN npm install

EXPOSE 3000

# start app
CMD ["npm", "start"]    