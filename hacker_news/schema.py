import graphene
import graphql_jwt

import links.schema
import users.schema
import api_logs.schema

class Query(api_logs.schema.Query, users.schema.Query, links.schema.Query, graphene.ObjectType):
    pass

class Mutation(api_logs.schema.Mutation, users.schema.Mutation, links.schema.Mutation, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
