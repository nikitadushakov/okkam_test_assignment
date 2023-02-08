from sqlmodel import SQLModel, Field
import datetime
from pydantic import BaseModel, dataclasses


class respondents_weight(SQLModel, table=True):
    date: datetime.date = Field(default=None, primary_key=True)
    respondent: int = Field(default=None, primary_key=True)
    sex: int
    age: int
    weight: float


class respondents_weight_agg(SQLModel, table=True):
    respondent: int = Field(default=None, primary_key=True)
    sex: int
    age: int
    average_weight: float


@dataclasses.dataclass
class Audiences:
    audience1: str
    audience2: str

    def __post_init__(self):
        self.date_in_filters = 'date' in f"{self.audience1}{self.audience2}".lower()


class PercentResponse(BaseModel):
    percent: str
