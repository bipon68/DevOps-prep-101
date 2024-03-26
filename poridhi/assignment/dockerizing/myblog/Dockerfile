FROM node:16-alpine

WORKDIR /app

COPY package.json .

RUN npm install

COPY . .

# Build the React app
RUN npm run build

# Expose the port your app runs on
EXPOSE 3000

CMD ["npm", "start"]