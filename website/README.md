# Websit (WIP, not implemented yet)
A website hosting small tools that you might need as someone using and writing code on the internet.

## First Time Setup
1. Create react app.
```
npx create-react-app tools
```
2. Install dependencies.  
Together, if you're using my package-lock.json:
```
npm install
```
or seperately:
```
npm install web-vitals
```
3. Test changes:
```
npm start
```

## Running
###Local development
```
npm start
```
### Docker
```
docker compose down && docker system prune -af && docker compose build && docker compose up -d && docker logs -f tools
```

