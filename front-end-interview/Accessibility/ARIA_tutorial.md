# ARIA Tutorial 
## 📜 Accordian
`Accordian.html`

- `role='navigation'` 대신 `<nav>` 태그를 활용한다. 
- 최상위 제목에는 `<h1>`을 사용한다. 
- Collapsable한 버튼에는 `aria-expanded='false|true'`를 통해 스크린 리더 사용자가 할 수 있는 행위를 오디오로 읽힐 수 있도록 한다. collapse event가 일어날 때 해당 속성도 빠짐없이 toggle 되도록 한다. 
- collapse event의 대상이 되는 요소는 `aria-controls='해당 요소의 id'`로 명시해준다. 
