# GraphX  
  
### Setup  
```bash  
make start  
```  
 
 ### New REST resource
- object definition, serialization/deserialization
see https://github.com/ihiji/falcon-marshmallow


- add swagger resource
 ```python
 # schema  
class HealthSchema(Schema):  
    status: fields.Str = fields.Str(required=True)  
    message: fields.Str = fields.Str(required=True)  
  
  
class HealthCheck:  
    # Handles GET requests  
    def on_get(self, req, resp):  
        """Internal description not shown in swagger docs.
                ---
                    summary: Check application health
                    responses:
                        200:
                            description: status response
                            schema: HealthSchema
        """
        resp.status = falcon.HTTP_200
        resp.body = json.dumps({"status": resp.status, "message": "healthy"})
 ```
 in swagger/__init__.py
 ```python
self.spec.components.schema('Health', schema=injector.get(HealthSchema))  
self.spec.path(resource=injector.get(HealthCheck))
 ```
 
### Usage  
Swagger UI:  
http://localhost:8021/v1/docs

### Creating a new service container [WIP]
must run the following to install dependencies before running the application, 
should be part of the container entrypoint, see packages/graphx/.docker/entrypoint.sh, and graphx/Makefile
```bash
make bootstrap
```

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
