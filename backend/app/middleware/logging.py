import time

from starlette.middleware.base import BaseHTTPMiddleware

from backend.app.core.logger import logger


class LoggingMiddleware(BaseHTTPMiddleware):

    async def dispatch(
        self,
        request,
        call_next,
    ):

        start = time.time()

        logger.info(
            f"Incoming Request: "
            f"{request.method} {request.url.path}"
        )

        response = await call_next(request)

        elapsed = time.time() - start

        logger.info(
            f"Completed: "
            f"{response.status_code} "
            f"in {elapsed:.3f}s"
        )

        return response