# Application Web Conteneurisée (Mini-projet Docker)

Application web développée en Python (Flask) affichant un message d'accueil personnalisable par variable d'environnement ainsi que la version de l'application.

## Image Docker Hub et versions disponibles

* **Nom de l'image :** `rourou2006/mon-app`
* **Versions (tags) disponibles :**
  * `1.0` (tag flottant pointant vers la dernière version stable `1.0.1`)
  * `1.0.1` (version actuelle avec numéro de version mis à jour)
  * `1.0.0` (version initiale)

## Lancement rapide depuis Docker Hub

Pour démarrer l'application directement sans télécharger le code source :

```bash
docker run -d \
  --name mon-app-web \
  -p 8080:5000 \
  --memory="256m" \
  --cpus="0.5" \
  -e APP_MESSAGE="Bonjour l'équipe !" \
  rourou2006/mon-app:1.0
```

Accédez ensuite à l'application depuis votre navigateur à l'adresse : `http://localhost:8080`

## Variables d'environnement disponibles

| Variable | Description | Valeur par défaut |
| :--- | :--- | :--- |
| `APP_MESSAGE` | Message d'accueil affiché sur la page web | `Bienvenue sur l'application conteneurisée !` |
| `APP_VERSION` | Numéro de version affiché sur la page | `1.0.1` |

## Construction locale de l'image

```bash
docker build -t rourou2006/mon-app:1.0.1 .
```
