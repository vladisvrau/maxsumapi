# maxsumapi
prova online para a área de Back-end da Studio Sol. 

## Descrição

API REST em Python [Tornado](https://www.tornadoweb.org/en/stable/) para obter a soma máxima de uma sub lista contínua de uma lista com N números inteiros.

## Serviços

A api possui um único serviço (`/maxsum`) que usa apenas um método (desconsiderando operações de pre-flight), sendo ele um `POST`.

O método recebe uma lista no corpo da requisição no formato `JSON` seguindo o seguinte padrão:
```json
{
    "list": []
}
```

e retorna o valor da maior soma de uma sub-lista contínua contida na lista, também no formato `JSON`, no seguinte padrão:
```json
{
    "result": 0
}
```

## Algoritmo

Foi usado um algoritmo [Guloso](https://pt.wikipedia.org/wiki/Algoritmo_guloso) para encontrar a solução do problema, ou seja a cada fase da iteração da lista, o algoritmo tenta encontrar o máximo local, no caso adicionando o próximo número a soma local do corrente e abandonando a soma caso ela fique inferior a zero. O máximo global só é atualizado caso o máximo local for superior ao mesmo.

## Execução

O deploy da API é feito usando um container Docker. Primeiro é necessário fazer o build da imagem com o seguinte commando:

```sh
docker build  -t maxsumapi .
```

E em seguida executar o container com a imagem, com o seguinte commando:

```sh
docker run  --publish 8080:8080 maxsumapi
```

Com isso o servidor fica aberto em `localhost:8080` e pode ser testada com o seguinte commando:

```curl
curl -d '{"list": [-2, 3, 5, -1, 4, -5]}' -H "Content-Type: application/json" -X POST http://localhost:8080/maxsum
```
