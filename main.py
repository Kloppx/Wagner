import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from typing import List, Optional

mock_users = [
    {"id": "1", "name": "Ana", "email": "ana@example.com"},
    {"id": "2", "name": "Carlos", "email": "carlos@example.com"},
    {"id": "3", "name": "Wagner", "email": "wagner@example.com"},
]

mock_projects = [
    {"id": "101", "name": "Lançamento do App", "description": "Coordenar o lançamento do novo aplicativo mobile.", "user_id": "1"},
    {"id": "102", "name": "Reforma do Site", "description": "Atualizar o layout e conteúdo do site principal.", "user_id": "2"},
    {"id": "103", "name": "Campanha de Marketing", "description": "Planejar campanha para o Q4.", "user_id": "1"},
    {"id": "104", "name": "SALVASCO", "description": "Salvar o vasco.", "user_id": "3"},
]

mock_tasks = [
    {"id": "1001", "title": "Definir press release", "completed": True, "project_id": "101"},
    {"id": "1002", "title": "Agendar posts para redes sociais", "completed": False, "project_id": "101"},
    {"id": "1003", "title": "Criar novos mockups do layout", "completed": True, "project_id": "102"},
    {"id": "1004", "title": "Revisar textos da home page", "completed": False, "project_id": "102"},
    {"id": "1005", "title": "Aprovar orçamento de anúncios", "completed": True, "project_id": "103"},
    {"id": "1006", "title": "Ganhar do Santos de Neymar", "completed": True, "project_id": "104"},
    {"id": "1007", "title": "Contratar o Coutinho", "completed": True, "project_id": "104"},
    {"id": "1008", "title": "Ser respeitado como maior do rio", "completed": False, "project_id": "104"},
]

@strawberry.type
class Task:
    id: strawberry.ID
    title: str
    completed: bool
    project_id: strawberry.Private[str]

@strawberry.type
class Project:
    id: strawberry.ID
    name: str
    description: str
    
    @strawberry.field
    def tasks(self) -> List[Task]:
        print(f"Buscando tarefas para o projeto {self.id}...")
        project_tasks = [task for task in mock_tasks if task["project_id"] == self.id]
        return [Task(**task) for task in project_tasks]

    user_id: strawberry.Private[str]
    
    @strawberry.field
    def user(self) -> "User":
        print(f"Buscando o dono do projeto {self.id}...")
        user_data = next(user for user in mock_users if user["id"] == self.user_id)
        return User(**user_data)

@strawberry.type
class User:
    id: strawberry.ID
    name: str
    email: str

    @strawberry.field
    def projects(self) -> List[Project]:
        print(f"Buscando projetos do usuário {self.id}...")
        user_projects = [proj for proj in mock_projects if proj["user_id"] == self.id]
        return [Project(**proj) for proj in user_projects]

@strawberry.type
class Query:
    @strawberry.field
    def users(self) -> List[User]:
        return [User(**user) for user in mock_users]

    @strawberry.field
    def user(self, id: strawberry.ID) -> Optional[User]:
        user_data = next((user for user in mock_users if user["id"] == id), None)
        return User(**user_data) if user_data else None

schema = strawberry.Schema(query=Query)
graphql_app = GraphQLRouter(schema)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")