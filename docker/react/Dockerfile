#build
FROM node:19-alpine as builder
WORKDIR /app
COPY frontend/ .
RUN npm ci 
RUN npm run build

#run
FROM nginx:stable-alpine as production
ENV NODE_ENV production
COPY --from=builder /app/build /usr/share/nginx/html
COPY docker/react/nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
