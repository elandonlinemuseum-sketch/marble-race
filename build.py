#!/usr/bin/env python3
"""app.html(아티팩트용 조각) -> index.html(단독 실행 파일) 생성"""
import pathlib
here = pathlib.Path(__file__).parent
frag = (here / "app.html").read_text(encoding="utf-8")
html = f"""<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="광고 없는 구슬 레이스 추첨기. 이름을 넣고 구슬을 굴려 순위로 당첨자를 정합니다.">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='7' fill='%230E1220'/%3E%3Ccircle cx='11' cy='12' r='5' fill='%23F0B429'/%3E%3Ccircle cx='21' cy='19' r='5' fill='%233FBFA8'/%3E%3Ccircle cx='13' cy='24' r='4' fill='%23FF5C7A'/%3E%3C/svg%3E">
<style>:root{{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}}
body{{margin:0;font:14px system-ui}}img{{max-width:100%}}[hidden]{{display:none!important}}</style>
</head>
<body>
{frag}
</body>
</html>
"""
(here / "index.html").write_text(html, encoding="utf-8")
print("index.html 생성 완료:", len(html), "bytes")
