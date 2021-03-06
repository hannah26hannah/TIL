# `<link>`

외부 리소스 연결을 위한 태그. 현재 문서와 외부 리소스의 관계를 명시한다. 이 태그는 스타일 시트를 연결할 때 제일 많이 사용하지만, 사이트 아이콘 (파비콘과 홈 화면 아이콘) 연결 등 여러 가지로 사용 가능하다. 

`<head>` 안에 아래처럼 작성한다. 
```html
<link href='main.css' rel='stylesheet'>
```

파비콘 연결을 위해서 아래처럼 자주 사용한다. 
```html
<link rel='icon' href='favicon.ico'>
```

- 아이콘을 위한 rel 값도 여러 개가 존재한다. 다양한 휴대 기기 플랫폼의 특별한 아이콘을 나타내기 위함이다. 
```html
<link rel='apple-touch-icon-precomposed' size='114x114' href='applie-icon-114.png' type='image/png'>
```

`media` 특성을 사용해 미디어 유형이나 쿼리를 지정할 수도 있다. 해당 미디어 조건을 만족할 때만 리소스를 불러오는 식이다. 
```html
<link href='print.css' rel='stylesheet' media='print'>
<link href='mobile.css' rel='stylesheet' media='scrren and (max-width: 600px)'>
```

새로운 성능 및 보안 관련 요소
```html
<link rel='preload' href='myFont.woff2' as='font' type='font/woff2' crossorigin='anonymous'>
```
- `rel='preload'` : 브라우저가 이 리소스를 미리 불러와야 한다는 것을 의미한다. 
- `as` 특성은 가져오는 리소스가 어떤 리소스인지 나타낸다. 
- `crossorigin`은 리소스를 CORS 요청으로 불러와야 하는지에 대한 값.


# 참고
MDN
