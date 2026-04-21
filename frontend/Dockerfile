# -------- BUILD STAGE --------
FROM node:18-slim AS builder

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .
RUN npm run build

# -------- RUNTIME STAGE --------
FROM nginx:alpine

COPY --from=builder /app/build /usr/share/nginx/html

EXPOSE 3000

HEALTHCHECK CMD wget -qO- http://localhost:3000 || exit 1