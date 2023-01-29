# WireMockで『リコリス・リコイル』の1シーン🐟

## Run WireMock

```sh
$ docker run -it --rm \
    -p 8080:8080 \
    --name chisataki-mock \
    -v $PWD:/home/wiremock \
    wiremock/wiremock:2.35.0
```

## Send requests like chisato & takina

Other shell:

```sh
$ curl http://localhost:8080/chinanago
さかなー🐟

$ curl -s http://localhost:8080/sakana -d '{"lines":"sakana"}' -H 'Content-Type: application/json' | jq .
{
  "character": "千束",
  "lines": "ちんあなごー🙌"
}
```
