from fastapi import FastAPI
import strawberry
import typing
from strawberry.fastapi import GraphQLRouter


def student_details():
    return [
        Student(
            name="sashank",
            age="17"
        )
    ]


@strawberry.type
class Student():
    name: str
    age: str


@strawberry.type
class Query():
    student: typing.List[Student] = strawberry.field(resolver=student_details)


@strawberry.type
class Mutation():
    @strawberry.mutation
    def add_student(self, name: str, age: str) -> Student:
        return Student(
            name=name,
            age=age
        )


schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema)


app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")
