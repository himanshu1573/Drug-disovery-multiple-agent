from __future__ import annotations

import httpx
import pytest

from agents.url_resource_fetcher import UrlResourceFetcher, validate_user_url


def test_validate_user_url_blocks_localhost_and_private_ips() -> None:
    with pytest.raises(ValueError):
        validate_user_url("http://localhost/test")
    with pytest.raises(ValueError):
        validate_user_url("http://127.0.0.1/test")
    with pytest.raises(ValueError):
        validate_user_url("ftp://example.com/file")


def test_validate_user_url_allows_public_https(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("A4T_URL_FETCH_DNS_CHECK", "0")
    validate_user_url("https://example.com/")


@pytest.mark.asyncio
async def test_fetcher_parses_html_title_and_text(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("A4T_URL_FETCH_DNS_CHECK", "0")
    html_body = "<html><head><title>Test Page</title></head><body><h1>Hello</h1><p>KRAS text</p></body></html>"

    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, headers={"content-type": "text/html; charset=utf-8"}, text=html_body)

    transport = httpx.MockTransport(handler)
    async with httpx.AsyncClient(transport=transport, follow_redirects=False) as client:
        fetcher = UrlResourceFetcher(client=client)
        resources = await fetcher.fetch(["https://example.com/test"])
    assert len(resources) == 1
    assert resources[0].title == "Test Page"
    assert "Hello" in resources[0].text
    assert "KRAS text" in resources[0].text
