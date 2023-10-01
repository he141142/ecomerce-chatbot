from fastapi import APIRouter, Body, Depends, Response, status, Request, Query, UploadFile, File

from router.history_router import history_router
from router.thread_router import thread_router
from flask import Flask, request, send_file
from starlette.responses import FileResponse
from pydantic import BaseModel
from typing import Optional
import os
from src.model.model import HandleQA
from config.config import config
import os
from src.getdata.user_query import get_data

ai_router = APIRouter()
ai_router.include_router(thread_router, prefix="/thread")
ai_router.include_router(history_router, prefix="/history")


class AIResponseModel(BaseModel):
    cau_tra_loi: Optional[str]


class AIQueryModel(BaseModel):
    question: str


@ai_router.post('/get_response')
async def get_response(input_: AIQueryModel):
    path = 'data/data'
    questionUser = input_.question
    out = AIResponseModel(cau_tra_loi=None)
    # if input_.question == 'gia co phieu ngay hom nay':
    #     out.cau_tra_loi = 'may deo mua duoc dau'
    #     return out
    dataCanXuLy = ""

    get_data(questionUser, query_folder=path)
    files = os.listdir(path)
    files = [os.path.join(path, file) for file in files]
    chat = HandleQA(config)

    x = chat.ask_gpt(questionUser, files)

    # code logic de tra ve cau tra loi
    # crawl data tu html -> file texts -> tong hop cau tra loi -> dua ra cau dung nhat = AI model sau do gan vao response message
    # dataCanXuLy = 'bla bla'  # can xu dung logic cua AI
    out.cau_tra_loi = fr'{str(x)}'

    return out

# @ai_router.post('/save-response')
# async def save_response(input_: AIResponseModel):
#     return
#
#
# @ai_router.post('/get-by-latest')
# async def save_response(input_: AIResponseModel):
#     return
