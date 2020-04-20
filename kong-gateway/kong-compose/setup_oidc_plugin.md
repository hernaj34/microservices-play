## Instalar modulo "luarocks" en docker

El fichero .rock a instalar es la versión de master compilada siguiendo las instrucciones de kong
[Instrucciones](https://docs.konghq.com/2.0.x/plugin-development/distribution/)

1. Copiar paquete luarocks en container
   docker cp kong-oidc-1.1.0-0.all.rock kong-compose_kong_1:/tmp

2. Entrar en docker como root

    ```sh
    docker exec -ti --user=root kong-compose_kong_1 sh
    ```

3. Instalar luarocks en container

    ```sh
    apk add luarocks
    ```

4. Instalar libreria luarocks "kong-oidc" con compilación de la versión master (2020.04.20)

    ```sh
    cd /tmp
    luarocks install kong-oidc-1.1.0-0.all.rock
    ```

5. Crear fichero de configuración

    ```sh
    vi /etc/kong/kong.conf
    ```

    Con el contenido

    ```ini
    ...
    plugins = bundled,oidc
    ...
    ```

    Guardar con ESC + ":wq"

6. Reiniciar kong
    ```sh
    docker-compose down
    docker-compose up
    ```
