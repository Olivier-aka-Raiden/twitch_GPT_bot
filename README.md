# Procédure d'installation

## Prérequis

 - Créer un compte sur openai afin d'obtenir une API key (/!\ guarder secret) (https://platform.openai.com/account/api-keys)
 - Créer un compte twitch pour le bot. 2FA nécessaire pour obtenir un token oauth qui permettra de se connecter via l'API twitch.
 - Créer une application sur le compte avec la console de dev twitch : https://dev.twitch.tv/console
 
## Installation

 - Remplacer les clés dans le fichier config.ini par vos clés perso
 - cliquer sur le script bot.bat

## Usage

Une fois lancé, le bot se connecte sur le chat de {channel-name} et écoute tous les messages du tchat.
Trigger une réponse du bot : envoyer un message au bot (@BOT_NAME). 
Pour que le bot réponde, il faut que le message fasse plus de 30 charactères afin d'éviter les appels
pour rien (ex: "mdr @BOT_NAME", "salut @BOT_NAME" etc.), et il répond que toutes les 20 sec (pour éviter de spam).