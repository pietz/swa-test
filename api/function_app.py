import azure.functions as func
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)


@app.route(route="health")
def health(req: func.HttpRequest) -> str:
    logging.info("Python HTTP trigger function processed a request.")
    return "Healthy"
