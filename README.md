# dockerCompose-github-casouso-2apps
Obj:
- Gestionar release y despliegue de 3 apps en server on-premise, con github y docker compose.
- Usar TAGs en github, para marcar las versiones de mi codigo. Por tanto, cada vez que actualices una o mas app, 
    asegurate de crear nueva etiqueta, para marcar nuevo RELEASE. y obviamente llevar bitacora con los cambios. 
- Para cada cambio de version, implica:
    - Actualizar codigo del o los aplicativos que correspondan,
    - Modificar archivo Dockerfile si es necesario,
    - Generar nueva imagen etiquetada con la version
    - Subir

/repositorio
├── app1/
│   ├── Dockerfile
│   ├── código fuente
│   ├── docker-compose.override.yml
├── app2/
│   ├── Dockerfile
│   ├── código fuente
│   ├── docker-compose.override.yml
├── app3/
│   ├── Dockerfile
│   ├── código fuente
│   ├── docker-compose.override.yml
└── docker-compose.yml

Como correr:
En el DIR de trabajo, generar build con (docker build -t app1:1.0.0 ./app1) para cada app
Subir imagenes contruidas a un registry remoto (docker tag app1:1.0.0 usuario/app1:1.0.0) y (docker push usuario/app1:1.0.0)
Para poder subir imagenes al registry, necesitas logearte en docker hub (docker login -u aastorga2019 + pass)
Cada vez que actualices una APP y se genere nueva imagen, en el docker-compose.yml sólo debes modificar las nuevas images de las apps
Puedes usar gitHub Actions para automatizar proceso de construccion y despliegue
