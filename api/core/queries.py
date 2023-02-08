import sqlmodel
from sqlmodel import (
    select,
    func,
    text,
    case
)
from core.models import Audiences, respondents_weight_agg, respondents_weight


def query_aggregated_table(audiences: Audiences) -> sqlmodel.sql.expression.SelectOfScalar:
    """
    при отсутствии фильтрации по дате используем данные таблицы с 
    посчитанными средними весами респондентов
    """
    stmt = (
        select(
            func.sum(case([(text(audiences.audience2), respondents_weight_agg.average_weight)], else_=0)) /
            func.sum(respondents_weight_agg.average_weight)
        )
        .where(
            text(audiences.audience1)
        )
    )
    return stmt


def query_main_table(audiences: Audiences) -> sqlmodel.sql.expression.SelectOfScalar:
    """
    при наличии фильтрации по дате используем данные изначальной таблицы
    """
    subquery = (
        select(
            respondents_weight.respondent,
            text(f"{audiences.audience2} as audience2"),
            func.avg(respondents_weight.weight).label('average_weight')
        )
        .where(
            text(audiences.audience1)
        )
        .group_by(
            respondents_weight.respondent, text(audiences.audience2)
        )
    ).subquery('t')

    stmt = (
        select(
            func.sum(case([(text("t.audience2"), subquery.c.average_weight)], else_=0)) /
            func.sum(subquery.c.average_weight)
        )
    )
    return stmt
