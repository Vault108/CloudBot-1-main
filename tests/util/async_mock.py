from unittest.mock import MagicMock


class AsyncMock(MagicMock):
    # pylint: disable=useless-super-delegation,invalid-overridden-method
    async def __call__(self, *args, **kwargs):
        return super().__call__(*args, **kwargs)
