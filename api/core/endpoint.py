from fastapi import APIRouter, Depends
from core.models import Audiences, PercentResponse
from core.db import get_database_session, AsyncSession
from core.action import get_result

router = APIRouter()


@router.get('/getPercent')
async def get_percent(audience1: str, audience2: str, db_session: AsyncSession = Depends(get_database_session)) -> PercentResponse:
    audiences = Audiences(audience1=audience1, audience2=audience2)
    print(audiences)
    res = await get_result(audiences=audiences, session=db_session)
    return res
