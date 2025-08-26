from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship

class Company(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    headquarters: str
    customers: List["Customer"] = Relationship(back_populates="company")

class Customer(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str = Field(index=True)
    company_id: int = Field(foreign_key="company.id")
    company: Optional[Company] = Relationship(back_populates="customers")
