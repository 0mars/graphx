# GraphX  
  
### Setup  
```bash  
make start  
```  

### Client
```bash
cd packages/graphx
pipenv run python client.py
```

Known issue:
You may need to run the client multiple times to get a result due to multiple workers issue that wasn't resolved

### Usage  
Swagger UI:  
http://localhost:8021/v1/docs

### helpful commands

-- restart graphx container
```bash
make restart graphx
```

-- rebuild graphx container
```bash
make clean-restart graphx
```

-- remove all containers
```bash
make clean
```

*Note:* please read Makefile for more commands, also Makefile under graphx/
