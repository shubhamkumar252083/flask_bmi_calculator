from flask import request

def log_requests_and_responses(app):
    @app.before_request
    def log_request_info():
        log_data = f"Request - Method: {request.method}, Path: {request.path}, Data: {request.data}"
        app.logger.info(log_data)

    @app.after_request
    def log_response_info(response):
        log_data = f"Response - Status Code: {response.status_code}, Data: {response.data}"
        app.logger.info(log_data)
        return response
