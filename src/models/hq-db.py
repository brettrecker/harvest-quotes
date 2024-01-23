import decimal
from enum import Enum
from typing import Optional, List
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class Role(str, Enum):
    admin = "admin"
    user = "user"


class Company(BaseModel):
    id: UUID
    company_name: str = Field(max_length=64)
    address1: str = Field(max_length=64)
    address2: Optional[str] = Field(max_length=64)
    city: str = Field(max_length=32)
    state: str = Field(max_length=16)
    subscription: str


class Users(BaseModel):
    id: UUID
    first_name: str = Field(max_length=64)
    last_name: str = Field(max_length=64)
    company: Company
    roles: List[Role]


class Customer(BaseModel):
    id: UUID
    first_name: str = Field(max_length=64)
    last_name: str = Field(max_length=64)
    phone_num: str = Field(max_length=16)
    address1: Optional[str] = Field(max_length=64)
    address2: Optional[str] = Field(max_length=64)
    city: str = Field(max_length=32)
    state: str = Field(max_length=16)
    county_of_use: str = Field(max_length=32)


class Quotes(BaseModel):
    id: UUID
    equipment: str
    cost: decimal
    margin: decimal
    program_1: Optional[str]
    program_1_discount: Optional[decimal]
    program_2: Optional[str]
    program_2_discount: Optional[decimal]
    program_3: Optional[str]
    program_3_discount: Optional[decimal]
    program_4: Optional[str]
    program_4_discount: Optional[decimal]
    freight_cost: decimal
    setup_cost: decimal
    trade_in_equipment: Optional[str]
    trade_in_value: Optional[decimal]
    trade_in_recon: Optional[decimal]
    trade_in_retail: Optional[decimal]
    quote_discounts: Optional[decimal]
    quote_sale_price: decimal
    quote_trade_in_price: Optional[decimal]





