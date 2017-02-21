from rest_framework.exceptions import APIException


class StationWrongToken(APIException):
    status_code = 403
    default_detail = 'Wrong token, please provide proper token parameter.'
    default_code = 'station_wrong_token'
