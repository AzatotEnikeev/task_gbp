from fastapi import FastAPI, Response, status
from datetime import datetime
from pydantic import BaseModel
from typing import List, Tuple
import pandas as pd
from enum import IntEnum

app = FastAPI()


class ColumnType(IntEnum):
    """
    Нужно для формирования из json в DataFrame (номера столбцов)
    """
    ID = 0
    DT = 1
    NAME = 2


BAD_REQUEST_ANSWER = "BAD_REQUEST"


def column_type_to_str(column_type: str):
    """
    Возвращает имя столбца в зависимости от Id
    :param column_type:
    :return:
    """
    res_str = ""
    if column_type == ColumnType.ID:
        res_str = 'document_id'
    elif column_type is ColumnType.DT:
        res_str = 'document_dt'
    elif column_type is ColumnType.NAME:
        res_str = 'document_name'
    return res_str


class TestInData(BaseModel):
    Columns: Tuple[str, str, str]
    Description: str
    RowCount: int
    Rows: List[Tuple[int, datetime, str]]


@app.post("/very/important/docs")
async def task6_handler(documents_date: datetime, test_data: TestInData, response: Response):
    today = datetime.today()
    if documents_date.year == today.year and documents_date.month == today.month and documents_date.day == today.day \
            and documents_date.time().hour == 0 and documents_date.time().minute == 0 \
            and documents_date.time().second == 0:
        """ 
        Представить данные "Columns" и "Rows" в виде плоского csv-подобного pandas.DataFrame
         В полученном DataFrame произвести переименование полей по след. маппингу
        "key1" -> "document_id", "key2" -> "document_dt", "key3" -> "document_name"
        Полученный DataFrame обогатить доп. столбцом: "load_dt" -> значение "сейчас"(датавремя)
        """
        res_df = (
            pd.DataFrame(data=test_data.Rows, columns=test_data.Columns)
            .rename(columns={test_data.Columns[val]: column_type_to_str(val) for val in ColumnType}) # создаем словарб переименований
            .assign(**{'load_dt': [datetime.now()] * len(test_data.Rows)})  # добавляем столбец
        )
        res_string = res_df.to_string()
    else:
        # Не удовлетворяет условию, что "начало дня сегодня в виде таймстемп", решил что 00-00 - начало дня
        response.status_code = status.HTTP_400_BAD_REQUEST
        res_string = BAD_REQUEST_ANSWER
    return res_string


