# Use Node.js para a etapa de build do Vue
FROM node:16 AS build-stage

# Defina o diretório de trabalho
WORKDIR /app

# Repassando ao container a variável declarada no docker-compose
ARG VUE_APP_DASHBOARD_URL
ENV VUE_APP_DASHBOARD_URL=$VUE_APP_DASHBOARD_URL

# Copie o package.json e o package-lock.json para instalar as dependências
COPY package*.json ./

# Instale as dependências
RUN npm install

# Copie todo o código do Vue para o contêiner
COPY . .

# Execute o build do Vue
RUN npm run build  # Isso criará a pasta dist/

# Use o Nginx para servir os arquivos do build
FROM nginx:alpine

# Copie os arquivos gerados pelo build do Vue para o Nginx
COPY --from=build-stage /app/dist /usr/share/nginx/html

# Copie a configuração personalizada do Nginx (caso tenha)
COPY nginx/nginx.conf /etc/nginx/conf.d/default.conf

# Exponha a porta 80
EXPOSE 8080

# Comando padrão para rodar o Nginx
CMD ["nginx", "-g", "daemon off;"]