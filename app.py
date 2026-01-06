import os
from mcp.server.fast.mcp import FastMCP

mcp = FastMCP("talk2Action", json_response=True)

@mcp.tool()
def extract_event_from_chat(chat: str, timezone: str = "Asia/Seoul") -> dict:
    return {
        "title": "모임",
        "datetime": None,
        "timezone": timezone,
        "place_text": None,
        "participants": [],
        "action_items": [],
        "confidence": 0.3
    }

@mcp.tool()
def draft_announcement(event: dict) -> str:
    title = event.get("title") or "모임"
    dt = event.get("datetime") or "시간 미정"
    place = event.get("place_text") or "장소 미정"
    return f"[공지] {title}/n- 일시: {dt}/n- 장소: {place}/n- 참석: 댓글로 알려줘요"

if __name__ =="__main__":
    port = int(os.environ.get("PORT", "8000"))
    host = os.environ.get("HOST", "0.0.0.0")

    mcp.run(transport="http", host=host, port=port, path="/mcp")