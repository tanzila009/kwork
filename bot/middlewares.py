from aiogram.utils.i18n import I18n, FSMI18nMiddleware



async def all_middleware(dp , i18n):
    dp.message.middleware(FSMI18nMiddleware(i18n))

