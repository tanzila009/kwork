from bot.distpatchers import dp
from bot.handlers.main import main
from bot.handlers.order import order


dp.include_routers(*[
    main,
    order
])