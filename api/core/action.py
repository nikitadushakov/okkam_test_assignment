from core.db import AsyncSession
from core.models import (
    PercentResponse,
    Audiences
)

from core.queries import query_aggregated_table, query_main_table


def _format_result(row_result: float) -> str:
    """
    Форматирование процента из числа в строку
    """
    return "{res}%".format(res=round(100 * row_result, 2))


async def get_result(audiences: Audiences, session: AsyncSession) -> PercentResponse:
    """
    Расчет процента вхождения второй аудитории в первую
    """
    query = query_aggregated_table(
        audiences=audiences
    ) if not audiences.date_in_filters else query_main_table(audiences)
    res = await session.execute(query)
    return PercentResponse(
        percent=_format_result(res.scalars().first())
    )
