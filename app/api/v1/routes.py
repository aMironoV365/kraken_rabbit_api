from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from ...pydantic_schemas.schemas import ProductCreate
from ...db.models import Product
from ...db.database import get_db
from ...consumer.consumer_send_product import send_product_to_rabbit

router = APIRouter()


@router.post("/products", response_model=ProductCreate, summary="Создание продукта")
async def create_product(
    product: ProductCreate, session: AsyncSession = Depends(get_db)
):
    """
    Создает новый продукт в базе данных и отправляет информацию о нем в RabbitMQ.

    **Параметры:**
    - `product`: данные о новом продукте, которые должны включать название, цену и описание.
    - `session`: асинхронная сессия базы данных для взаимодействия с SQLAlchemy.

    **Ответ:**
    - Возвращает созданный продукт в формате `ProductCreate` в случае успешного добавления.

    **Ошибки:**
    - Если продукт с таким названием уже существует, возвращается ошибка 400.
    """
    result = await session.execute(select(Product).where(Product.name == product.name))
    existing = result.scalar_one_or_none()
    if existing:
        raise HTTPException(
            status_code=400, detail="Product with this name already exists"
        )

    db_product = Product(
        name=product.name, price=product.price, description=product.description
    )
    session.add(db_product)
    await session.commit()
    await session.refresh(db_product)

    await send_product_to_rabbit(
        {
            "message": "Product created",
            "product": {
                "name": db_product.name,
                "price": db_product.price,
                "description": db_product.description,
            },
        }
    )

    return db_product
