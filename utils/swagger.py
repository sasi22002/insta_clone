from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import status

login_swagger = swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'email': openapi.Schema(type=openapi.TYPE_STRING, description='Your name'),
                'password': openapi.Schema(type=openapi.TYPE_STRING, description='Your password'),
            },
            required=['email', 'password'],
        ),
        responses={status.HTTP_201_CREATED: "Login successfully"},
        operation_description="Login instance with email and password."
    )


add_numbers_swagger = swagger_auto_schema(
    method='post',
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'numbers': openapi.Schema(type=openapi.TYPE_ARRAY, description='Your list of numbers',items=openapi.Items(type=openapi.TYPE_NUMBER)  # <------
),
            },
        required=['numbers']
    ),
    responses={status.HTTP_201_CREATED: "Success"},
)



add_task_swagger = swagger_auto_schema(
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
                'title': openapi.Schema(type=openapi.TYPE_STRING, description='Your Title of task'),
                'description': openapi.Schema(type=openapi.TYPE_STRING, description='Description'),
                'dueDate': openapi.Schema(type=openapi.TYPE_STRING, description='Due date'),
                'completed': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='Completion status'),
            },
    ),
    responses={status.HTTP_201_CREATED: "Task created successfully"},
)


update_task_swagger = swagger_auto_schema(
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
                'id': openapi.Schema(type=openapi.TYPE_INTEGER, description='Id of task'),
                'title': openapi.Schema(type=openapi.TYPE_STRING, description='Your Title of task'),
                'description': openapi.Schema(type=openapi.TYPE_STRING, description='Description'),
                'dueDate': openapi.Schema(type=openapi.TYPE_STRING, description='Due date'),
                'completed': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='Completion status'),
            },
    ),
    responses={status.HTTP_201_CREATED: "Task created successfully"},
)


delete_task_swagger = swagger_auto_schema(
    manual_parameters=[
        openapi.Parameter(
            name='id',
            in_=openapi.IN_QUERY,
            type=openapi.TYPE_STRING,
            description='Description of the query parameter',
            required=True,  # Set to True if the parameter is required
        ),
    ],
    responses={status.HTTP_201_CREATED: "Task deleted successfully"},
)
