from __future__ import annotations

import builtins
from urllib.error import URLError

import pytest

from agents.server_manager import ExternalServerContext
from agents.schema import SourceName


@pytest.mark.asyncio
async def test_server_manager_starts_and_stops_pharos(monkeypatch) -> None:
    events: list[tuple[str, dict]] = []

    class DummyFile:
        def close(self) -> None:
            events.append(("log_closed", {}))

    class DummyProc:
        pid = 1234

    async def fake_is_port_in_use(self, port: int) -> bool:
        assert port == 8787
        return False

    def fake_log_event(event: str, **fields) -> None:
        events.append((event, fields))

    monkeypatch.setattr("agents.server_manager.run_source_health_checks", lambda _request: [])
    monkeypatch.setattr("agents.server_manager.log_event", fake_log_event)
    monkeypatch.setattr(builtins, "open", lambda *_args, **_kwargs: DummyFile())
    monkeypatch.setattr("agents.server_manager.os.path.exists", lambda path: True)
    monkeypatch.setattr("agents.server_manager.subprocess.Popen", lambda *_args, **_kwargs: DummyProc())
    monkeypatch.setattr("agents.server_manager.os.getpgid", lambda _pid: 99)
    monkeypatch.setattr("agents.server_manager.os.killpg", lambda _pgid, _sig: events.append(("killpg", {})))
    monkeypatch.setattr(ExternalServerContext, "_is_port_in_use", fake_is_port_in_use)

    class DummyResponse:
        pass

    monkeypatch.setattr("urllib.request.urlopen", lambda _url: DummyResponse())

    async with ExternalServerContext([SourceName.EXT_PHAROS]):
        assert any(event == "external_server_start" for event, _fields in events)

    assert any(event == "external_server_ready" for event, _fields in events)
    assert any(event == "external_server_stop" for event, _fields in events)
    assert any(event == "log_closed" for event, _fields in events)


@pytest.mark.asyncio
async def test_server_manager_raises_on_startup_timeout(monkeypatch) -> None:
    async def fake_is_port_in_use(self, _port: int) -> bool:
        return False

    class DummyFile:
        def close(self) -> None:
            return None

    class DummyProc:
        pid = 1234

    monkeypatch.setenv("A4T_PHAROS_START_TIMEOUT_S", "0.01")
    monkeypatch.setattr("agents.server_manager.run_source_health_checks", lambda _request: [])
    monkeypatch.setattr(builtins, "open", lambda *_args, **_kwargs: DummyFile())
    monkeypatch.setattr("agents.server_manager.os.path.exists", lambda path: True)
    monkeypatch.setattr("agents.server_manager.subprocess.Popen", lambda *_args, **_kwargs: DummyProc())
    monkeypatch.setattr("agents.server_manager.os.getpgid", lambda _pid: 99)
    monkeypatch.setattr("agents.server_manager.os.killpg", lambda _pgid, _sig: None)
    monkeypatch.setattr(ExternalServerContext, "_is_port_in_use", fake_is_port_in_use)
    monkeypatch.setattr("urllib.request.urlopen", lambda _url: (_ for _ in ()).throw(URLError("offline")))

    async def fast_sleep(_delay: float) -> None:
        return None

    monkeypatch.setattr("agents.server_manager.asyncio.sleep", fast_sleep)

    with pytest.raises(RuntimeError, match="failed to report ready within timeout"):
        async with ExternalServerContext([SourceName.EXT_PHAROS]):
            pass
