from fastapi import APIRouter
from fastapi import Depends
from loguru import logger


from app.hello.schema.hello import HelloNameResponse
from app.hello.services.hello import hello


hello_router = APIRouter(prefix="/hello", tags=["hello"])


@hello_router.get(
    '',
    response_model=HelloNameResponse,
    description="Hello name",
)
async def hello_name(current_user_name: str) -> HelloNameResponse:
    """Say hello to the given name.

    Args:
        current_user_name (str): The name to say hello to.

    Returns:
        HelloNameResponse: The greeting message.
    """
    logger.info(f"Hello name with current_user_name={current_user_name}")
    result = await hello(current_user_name)
    return HelloNameResponse(
        language="python",
        success=True,
        message=result
    )
