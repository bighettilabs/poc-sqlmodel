from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import SQLModel, select
from sqlalchemy.orm import selectinload
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from models import Company, Customer
from database import async_engine, get_session

app = FastAPI()

@app.on_event("startup")
async def on_startup():
    async with async_engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)

@app.post("/companies/", response_model=Company)
async def create_company(company: Company, session: AsyncSession = Depends(get_session)):
    session.add(company)
    try:
        await session.commit()
        await session.refresh(company)
    except IntegrityError:
        await session.rollback()
        raise HTTPException(status_code=400, detail="Company already exists or invalid data.")
    return company

@app.post("/customers/", response_model=Customer)
async def create_customer(customer: Customer, session: AsyncSession = Depends(get_session)):
    session.add(customer)
    try:
        await session.commit()
        await session.refresh(customer)
    except IntegrityError:
        await session.rollback()
        raise HTTPException(status_code=400, detail="Customer already exists or invalid data.")
    return customer

@app.get("/customers/", response_model=List[Customer])
async def list_customers(session: AsyncSession = Depends(get_session)):
    result = await session.execute(
        select(Customer).options(selectinload(Customer.company))
    )
    customers = result.scalars().all()
    return customers
