from sqlalchemy.ext.asyncio import AsyncSession

from src.managers.user_managers import UserManager
from src.schemas.user_schemas import ShowUser, UserCreate, TelegramUserCreate, ShowTelegramUser


async def _create_new_user(body: UserCreate, async_session: AsyncSession) -> ShowUser:
    """  Асинхронное создание пользователя """
    async with async_session as session:
        async with session.begin():
            user_manage = UserManager(session)
            user = await user_manage.create_user(
                username=body.username,
                email=body.email
            )
            return ShowUser(
                id=user.id,
                username=user.username,
                email=user.email,
                account_status=user.account_status
            )


async def _create_new_telegram_user(
        body: TelegramUserCreate,
        async_session: AsyncSession
) -> ShowTelegramUser:
    """  Асинхронное создание telegram пользователя """
    async with async_session as session:
        async with session.begin():
            user_manage = UserManager(session)
            user = await user_manage.create_telegram_user(
                telegram_id=body.telegram_id,
                username=body.username,
                first_name=body.first_name,
                last_name=body.last_name,
                additional_information=body.additional_information,
            )

            return ShowTelegramUser(
                id=user.id,
                telegram_id=user.telegram_id,
                username=user.username,
                first_name=user.first_name,
                last_name=user.last_name,
                additional_information=user.additional_information,
                account_status=user.account_status
            )


async def _delete_user(
        user_id: int,
        async_session: AsyncSession
) -> None | int:
    """ Асинхронное удаление пользователя """
    async with async_session as session:
        async with session.begin():
            user_manage = UserManager(session)
            deleted_user_id = await user_manage.delete_user(user_id=user_id)
            return deleted_user_id
