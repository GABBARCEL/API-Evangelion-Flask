# API Evangelion Flask

Este projeto é uma **API em Python** construída com **Flask**, que fornece informações detalhadas sobre os principais personagens de *Neon Genesis Evangelion*. Cada endpoint retorna dados estruturados em JSON, incluindo atributos como **nome, EVA pilotado, idade, afiliação, habilidades e relacionamentos**.

## Endpoints disponíveis

- `/rei` - Informações sobre **Rei Ayanami**  
- `/shinji` - Informações sobre **Shinji Ikari**  
- `/asuka` - Informações sobre **Asuka Langley**  
- `/misato` - Informações sobre **Misato Katsuragi**  
- `/gendo` - Informações sobre **Gendo Ikari**  
- `/kaworo` - Informações sobre **Kaworu Nagisa**

Cada endpoint retorna um JSON com os atributos do personagem, como:

```json
{
  "name": "Rei Ayanami",
  "eva": "Unit-00",
  "age": 14,
  "affiliation": "NERV",
  "role": "Pilot",
  "personality": ["calm", "detached", "mysterious"],
  "abilities": ["high sync rate", "emotional suppression"],
  "relationships": {
    "commander": "Gendo Ikari",
    "ally": "Shinji Ikari"
  }
}
```
## Tecnologias utilizadas
- Python 3
- Flask - framework web para APIs
- Gunicorn - servidor WSGI para deploy em produção
- Render - hospedagem da API

## Acesso público

A API já está online e acessível publicamente! Você pode testar os endpoints diretamente no seu navegador, Postman ou via scripts Python.

🔗 Acesse a API aqui: <a heref="https://api-evangelion-flask.onrender.com"> https://api-evangelion-flask.onrender.com </a>

---

### Exemplo de uso em Python:

```python
import requests

response = requests.get("https://api-evangelion-flask.onrender.com/rei")
data = response.json()
print(data)
```
Essa API é perfeita para projetos de estudo, integração com apps ou apenas para explorar os dados dos personagens de Evangelion de forma estruturada.