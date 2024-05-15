# Utilise une image de base officielle de Node.js
FROM node:14-alpine

# Définit le répertoire de travail dans le conteneur
WORKDIR /app

# Copie le fichier package.json et package-lock.json
COPY package*.json ./

# Installe les dépendances
RUN npm install

# Copie le reste des fichiers de l'application
COPY . .

# Compile l'application React
RUN npm run build

# Installe un serveur web léger pour servir l'application
RUN npm install -g serve

# Expose le port sur lequel l'application va tourner
EXPOSE 5000

# Définit la commande par défaut pour démarrer l'application
CMD ["serve", "-s", "build", "-l", "5000"]
