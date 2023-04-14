# Procédure d'installation

## Prérequis

 - Créer un compte sur openai afin d'obtenir une API key (/!\ guarder secret) (https://platform.openai.com/account/api-keys)
 - Créer un compte twitch pour le bot. 2FA nécessaire pour obtenir un token oauth qui permettra de se connecter via l'API twitch.
  - Créer un compte sur twitch
  - Accéder aux paramètres du compte et activer la 2FA
  - Accéder à la console de dev : https://dev.twitch.tv/console
  - Créer une nouvelle application : choisir un nom, une catégorie (chat bot) et une URL de redirection (ex: http://localhost)
  - Récupérer le clientID et penser à garder le secret (information uniquement communiquée à la création)
  - Appeler l'url : https://id.twitch.tv/oauth2/authorize?response_type=token&client_id=**{clientId}**&redirect_uri=**{redirect_uri}**&scope=chat%3Aedit+chat%3Aread&state=c3ab8aa609ea11e793ae92361f002671. Normalement, cela devrait vous ouvrir une fenêtre de connexion où il faut vous login avec le compte du bot. Une fois login, vous allez être redirigé vers l'url de votre application (localhost ici) et dans l'url se trouvera le token (twitch-token) qu'il faudra mettre dans le fichier de config.
 
## Installation

 - Remplacer les clés dans le fichier config.ini par vos clés perso
 - cliquer sur le script bot.bat

## Usage

Une fois lancé, le bot se connecte sur le chat de {channel-name} et écoute tous les messages du tchat.
Trigger une réponse du bot : envoyer un message au bot (@BOT_NAME). 
Pour que le bot réponde, il faut que le message fasse plus de 30 charactères afin d'éviter les appels
pour rien (ex: "mdr @BOT_NAME", "salut @BOT_NAME" etc.), et il répond que toutes les 20 sec (pour éviter de spam).
