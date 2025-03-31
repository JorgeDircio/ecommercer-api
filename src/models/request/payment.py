from decimal import Decimal
from pydantic import BaseModel, EmailStr, Field
from typing import Annotated


class CustomerInformation(BaseModel):
    firstName: Annotated[str, Field(example="Homer")]
    lastName: Annotated[str, Field(example="Simpson")]
    middleName: Annotated[str, Field(example="Jay")]
    email: Annotated[EmailStr, Field(example="homer@gmail.com")]
    phone1: Annotated[str, Field(example="5511223344")]
    city: Annotated[str, Field(example="Springfield")]
    address1: Annotated[str, Field(example="742 Evergreen Terrace")]
    postalCode: Annotated[str, Field(example="12345")]
    state: Annotated[str, Field(example="New York")]
    country: Annotated[str, Field(min_length=2, max_length=2, example="US")]
    ip: Annotated[str, Field(example="123.123.123.123")]


class NoPresentCardData(BaseModel):
    cardNumber: Annotated[str, Field(min_length=13, max_length=19, example="4242424242424242")]
    cvv: Annotated[str, Field(min_length=3, max_length=4, example="123")]
    cardholderName: Annotated[str, Field(example="HOMER JAY SIMPSON")]
    expirationYear: Annotated[str, Field(min_length=2, max_length=2, example="21")]
    expirationMonth: Annotated[str, Field(min_length=2, max_length=2, example="01")]


class PaymentRequest(BaseModel):
    amount: Annotated[Decimal, Field(example=10.00)]
    currency: Annotated[str, Field(min_length=3, max_length=3, example="484")]
    customerInformation: CustomerInformation
    noPresentCardData: NoPresentCardData

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "amount": 10.00,
                    "currency": "484",
                    "customerInformation": {
                        "firstName": "Homer",
                        "lastName": "Simpson",
                        "middleName": "Jay",
                        "email": "homer@gmail.com",
                        "phone1": "5511223344",
                        "city": "Springfield",
                        "address1": "742 Evergreen Terrace",
                        "postalCode": "12345",
                        "state": "New York",
                        "country": "US",
                        "ip": "123.123.123.123"
                    },
                    "noPresentCardData": {
                        "cardNumber": "4242424242424242",
                        "cvv": "123",
                        "cardholderName": "HOMER JAY SIMPSON",
                        "expirationYear": "21",
                        "expirationMonth": "01"
                    }
                }
            ]
        }
    }
