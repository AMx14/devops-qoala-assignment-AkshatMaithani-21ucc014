#Fixed the typo in "latest" (removed extra 's')
FROM nginx:latest

#Fixed the typo in "nginx" (was "nginix")
COPY nginx.conf /etc/nginx/nginx.conf

#Fixed the typo in "html" (removed extra 'l')
COPY ./html /usr/share/nginx/html

#Port number should be numerical, not text
EXPOSE 80

#Fixed "of" to "off" in the daemon directive
CMD ["nginx", "-g", "daemon off;"]