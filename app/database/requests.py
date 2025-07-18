from sqlalchemy import select

from app.database.models import async_session
#from app.database.models import <КЛАССЫ БД>

#Импорты____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

#регистрация пользователя
async def set_user(tg_id: int):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))

        if not user:
            session.add(User(tg_id=tg_id))
            await session.commit()