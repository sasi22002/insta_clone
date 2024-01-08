from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import status
from utils.response_message import Message

login = swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'email': openapi.Schema(type=openapi.TYPE_STRING, description='Your name'),
                'password': openapi.Schema(type=openapi.TYPE_STRING, description='Your password'),
                'role': openapi.Schema(type=openapi.TYPE_INTEGER, description='Your role'),
            },
            required=['name', 'password','role'],
        ),
        responses={status.HTTP_201_CREATED: Message.login_success},
        operation_description="Login instance with email and password."
    )


signup = swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'email': openapi.Schema(type=openapi.TYPE_STRING, description='Your email'),
                'username': openapi.Schema(type=openapi.TYPE_STRING, description='Your name'),
                'phone_number': openapi.Schema(type=openapi.TYPE_STRING, description='Your name'),
                'password': openapi.Schema(type=openapi.TYPE_STRING, description='Your password'),
                'confirm_password': openapi.Schema(type=openapi.TYPE_STRING, description='Your password'),
                'role': openapi.Schema(type=openapi.TYPE_INTEGER, description='Your role'),

            },
            required=['name', 'password'],
        ),
        responses={status.HTTP_201_CREATED: Message.signup},
    )



user_followers_get = swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('page', openapi.IN_QUERY, description="Page number", type=openapi.TYPE_INTEGER),
            openapi.Parameter('item', openapi.IN_QUERY, description="Item number", type=openapi.TYPE_INTEGER),
            openapi.Parameter('search', openapi.IN_QUERY, description="search", type=openapi.TYPE_STRING,required=False),

        ],
        operation_description='API endpoint to list all followed user',
        responses={status.HTTP_201_CREATED: Message.user_listed},

    )



user_follower_post = swagger_auto_schema(
       request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'user_id': openapi.Schema(type=openapi.TYPE_INTEGER, description='Your follow id'),

            },
        ),
        responses={status.HTTP_201_CREATED: Message.user_listed},

    )




user_follow_approve = swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'id': openapi.Schema(type=openapi.TYPE_INTEGER, description='Your follow id'),
                'is_accepted': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='Accept/reject'),

            },
        ),
        responses={status.HTTP_201_CREATED: Message.follow_request_accept},
    )




user_lists = swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('search', openapi.IN_QUERY, description="search", type=openapi.TYPE_STRING,required=False),

        ],
        operation_description='API endpoint to list all users',
        responses={status.HTTP_201_CREATED: Message.user_listed},

    )


friend_lists = swagger_auto_schema(
       
        operation_description='API endpoint to list friends',
        responses={status.HTTP_201_CREATED: Message.user_listed},

    )