# API em GraphQL para Gerenciamento de Projetos

![Python](https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.116-blue?style=for-the-badge&logo=fastapi&logoColor=white)
![GraphQL](https://img.shields.io/badge/GraphQL-Strawberry-blue?style=for-the-badge&logo=graphql&logoColor=white)

Um projeto acadêmico desenvolvido para demonstrar os conceitos, o funcionamento e as vantagens de se utilizar GraphQL para construir APIs modernas e eficientes. A aplicação simula um sistema simples de gerenciamento de projetos, com Usuários, Projetos e Tarefas.

## 🚀 Conceitos Demonstrados

Este projeto serve como uma demonstração prática dos seguintes conceitos:

-   **Schema GraphQL Fortemente Tipado:** Definição de `Types`, `Queries` e relacionamentos.
-   **Resolvers:** Funções que buscam os dados e resolvem as relações do grafo.
-   **Eficiência de Dados:** Resolução do problema de **Over-fetching** e **Under-fetching** comum em APIs REST.
-   **Queries Aninhadas:** Como buscar dados complexos e relacionados em uma única chamada.
-   **Boas Práticas:** Uso de `strawberry.Private` para campos internos e `Optional` para retornos que podem ser nulos.
-   **API com Python Moderno:** Utilização de FastAPI e Strawberry para uma implementação leve e performática.

## ✨ Features

-   Listar todos os usuários.
-   Buscar um usuário específico pelo seu ID.
-   Consultar todos os projetos de um usuário.
-   Consultar todas as tarefas de um projeto.
-   **Principal Vantagem:** Obter todos esses dados aninhados (usuário -> projetos -> tarefas) em uma única requisição.

## 🛠️ Tecnologias Utilizadas

-   **Python 3.11+**
-   **FastAPI:** Para a criação do servidor web ASGI.
-   **Strawberry:** Para a implementação do Schema e lógica GraphQL.
-   **Uvicorn:** Como o servidor ASGI que roda a aplicação.
