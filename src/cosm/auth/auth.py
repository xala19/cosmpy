from cosmos.auth.v1beta1.query_pb2 import (
    QueryAccountRequest,
    QueryAccountResponse,
    QueryParamsRequest,
    QueryParamsResponse,
)


class Auth:
    def Account(self, request: QueryAccountRequest) -> QueryAccountResponse:
        pass

    def Params(self, request: QueryParamsRequest) -> QueryParamsResponse:
        pass