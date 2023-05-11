"""Code for sending and handling HTTP requests to external services"""

import logging
from http import HTTPStatus

import aiohttp

logger = logging.getLogger(__name__)


async def fetch_page_content(url: str, status_message_override: dict[HTTPStatus, str] | None = None) -> str:
    """Handles fetching the content from a given web address"""

    result = ''
    status_message = {
        HTTPStatus.NOT_FOUND: "Could not find resource.",
    }
    if status_message_override is not None:
        status_message |= status_message_override

    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url=url) as request:

                if request.status == HTTPStatus.OK:
                    result = await request.text()

                elif request.status in status_message:
                    logger.error(
                        status_message.get(
                            HTTPStatus(request.status),
                            f"[{request.status}] - {request.reason or 'Unidentified problem'}",
                        ),
                    )

        except aiohttp.ClientConnectionError as err:
            logger.error("Connection error: %s", err)

    return result
