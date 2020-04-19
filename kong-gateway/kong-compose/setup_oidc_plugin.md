## Instalar modulo "luarocks" en docker

1. Entrar en docker como root

    ```sh
    docker exec -ti --user=root kong-compose_kong_1 sh
    ```

2. Instalar luarocks en container

    ```sh
    apk add luarocks
    ```

3. Instalar libreria luarocks "kong-oidc"

    ```sh
    luarocks install kong-oidc
    ```

4. Crear fichero de configuración

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

5. Reiniciar kong
    ```sh
    docker-compose down
    docker-compose up
    ```
