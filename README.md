# How to run given tasks

## File formate:

    - 2nd task
        - Book Service
            - app
                - models (Here is all models)
                - routers (Here is all routing)
                - utils
        - main.py
        - docker-compose.yml

## For 2nd Task:
    install Docker on your System
    
    Change directory
        - cd Book\ Service 

    Run docker the file
    [./Book Service]
    └─$ docker-compose up --build 

    Braowse for get all APIs:
        http://0.0.0.0:8000/docs
        
        or
        
        for Books:

        
        POST create book endpoint: http://0.0.0.0:8000/books/
        GET list book endpoint: http://127.0.0.1:8000/books/?first_letter=a&author=shuvo

        
        for Authors:
        
        GET list authors endpoint: http://0.0.0.0:8000/authors/
        POST create author enpoint: http://0.0.0.0:8000/authors/


        for Clients:
        
        POST create clients endpoint: http://0.0.0.0:8000/clients/ (you will get a token)
        GET list clients endpoint: http://0.0.0.0:8000/clients/


        For link/unlink by trabsactions:
        
        POST link client to book endpoit: http://0.0.0.0:8000/transactions/?book_id=1 (using token)

        DELETE unlink clint client ot book endpoint: http://0.0.0.0:8000/transactions/1 (using token)
