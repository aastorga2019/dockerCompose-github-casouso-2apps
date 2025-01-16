# dockerCompose-github-casouso-2apps
Obj:
- Gestionar release y despliegue de 2 a 3 Apps en server on-premise o local, con github y docker compose.
- Usar TAGs en github, para marcar las nuevas versiones de mi codigo. Por tanto, cada vez que actualices una o mas app, 
    asegurate de crear nueva etiqueta (git tag -a v1.0.1 -m "Cambio menor a version anterior de app1 y app2"), para marcar nuevo RELEASE. y obviamente llevar bitacora con los cambios.
    Donde V x.y.z;
        x: Marca un cambio de Release "Alto" a las versiones de los aplicativos. Ex. nueva funcionalidad.
        y: Marca un cambio "Medio" a los aplicativos. Ex. se refactoriza o mejora funcionalidad de una funcion existente.
        z: Marca un cambio "Bajo" a los aplicativos. Ex. un bugs o error encontrado, que puede ser solucionado rapidamente.

- Para cada cambio de version, implica revisar (docker build -t appN:x.y.z ./appN)
    * Actualizar codigo del o los aplicativos que correspondan,
    * Modificar archivo Dockerfile si es necesario,
    * Generar nueva imagen etiquetada con la version,
    * Subir

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
