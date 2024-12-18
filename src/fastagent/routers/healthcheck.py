"""Healthcheck router."""

from fastapi import APIRouter, status

from fastagent.internal.data.healthcheck import Healthcheck
from fastagent.internal.settings import SettingsDependency

router = APIRouter(prefix="/v1", tags=["healthcheck"])


@router.get(
    "/healthcheck",
    status_code=status.HTTP_200_OK,
    response_model=Healthcheck,
)
async def healthcheck_handler(
    settings: SettingsDependency,
) -> Healthcheck:
    """Healthcheck endpoint."""
    return {
        "status": "available",
        "system_info": {
            "environment": settings.environment,
            "version": "0.0.1",
        },
    }
