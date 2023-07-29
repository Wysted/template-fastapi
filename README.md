
# Microservice {name}

## Requirements

- Python3.10+
- Docker
- MongoDB

## Development

1. Create a venv

```bash
python3 -m venv ./venv
```

2. Activate venv

```bash
source ./venv/bin/active
```

3. Install dependencies

```bash
pip3 install -r requirements.txt
```

4. Run

```bash
sudo docker build --tag microservice_{name} .
sudo docker run microservice_{name}
```

### Docker

`Dockerfile`
`Dockerfile.prod`

Exposed port (in both Dockerfiles): `6060`
## API Reference (Swagger)

#### Swagger ui

```http
  GET /api/x/docs
```

#### Redoc

```http
  GET /api/x/redoc
```
