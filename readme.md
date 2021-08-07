# Test de algoritmos criptográficos

## Instrucciones de uso 

Hay que tener docker y docker-compose instalado

Se corre el siguiente comando la primera ves que se utiliza
```
$ docker-compose build
```

Se corre el siguiente comando cada que se quiera ejecutar
```
$ docker-compose up
```
Los resultados de la ejecución se encontrarán en el directorio [results](./results)

## Instucciones de uso alternativas

Si no se desea usar docker se puede optar por instalarlo con python nativo 

Se recomienda tener python 3.8 o superior

En la raiz del directorio [src](src) se ejecuta el comando:

```bash
$ pip install .
```

Luego se retorna esta [raiz](/)  y se ejecuta el siguiente comando 

```
$ test-algoritmos-crypto --out-folder ./results --test-folder ./test_vectors --num-iteraciones 10
```
en `--num-iteraciones` se pueden definir cuantas iteraciones se desan ejecutar

Los resultados se pueden encontrar en el directorio [results](results/)

## Descripción

Es un proyecto para la materia de criptografía semestre 2021-2

### Contenido

#### Algoritmos a probar

* AES-EBC 256 bits
* AES-CBC 256 bits
* SHA-2 384 bits
* SHA-2 512 bits
* SHA-3 384 bits
* SHA-3 512 bits
* RSA-OAEP 1024 bits
* RSA-PSS 1024 bits
* DSA 1024 bits
* ECDSA Prime Field 521 bits
* ECDSA Binary Field 571 bits

#### Operaciones a probar

* Cifrado
* Descifrado
* Hashing
* Firmado
* Verificación

### Clasificación de operaciones

#### Cifrado y descifrado

En esta clasificación se encuentran:

* AES-EBC 256 bits
* AES-CBC 256 bits
* RSA-OAEP 1024 bits

Este ultimo no es comparable con AES-EBC y CBC

#### Hashing

En esta clasificación se encuentra:

* SHA-2 384 bits
* SHA-2 512 bits
* SHA-3 512 bits

#### Firma y verificación

Aquí se encuentran:

* RSA-PSS 1024 bits
* DSA 1024 bits
* ECDSA Prime Field 521 bits
* ECDSA Binary Field 571 bits
