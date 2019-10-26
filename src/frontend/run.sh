sudo docker build -t seq2brain-frontend .
docker run -v ${PWD}:/app -v /app/node_modules -p 3001:3000 --rm seq2brain-frontend