# ---------- BUILD ----------
FROM node:18-slim AS builder

WORKDIR /app
COPY package*.json ./
RUN npm install

COPY . .

# ---------- RUN ----------
FROM node:18-slim

WORKDIR /app

COPY --from=builder /app /app

RUN useradd -m appuser

USER appuser

EXPOSE 3000

HEALTHCHECK CMD curl -f http://localhost:3000 || exit 1

CMD ["node", "app.js"]
