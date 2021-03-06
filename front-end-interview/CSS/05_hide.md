# hide and show
## 콘텐츠를 시각적으로 숨기는(그리고 screen reader에서만 사용할 수 있게 만드는)다양한 방법은 무엇인가요?
- `width: 0; height: 0` : 요소가 화면에서 어떤 공간도 차지하지 않아, 시각적으로도 보이지 않습니다. 
- `position: absolute; left: -99999px;` : 화면 외부에 배치합니다. 
    - [position in CSS](./position.md)
- `text-indent: -9999px;` : 단, 이는 block level인 요소 내 텍스트에서만 작동합니다. 
- JavaScript의 HTMLElement.hidden property를 이용합니다. 
```js
Element.hidden = true | false
```
    - content that isn't yet relevant but may be needed later
    - content that was previously needed but is not any longer
    - conent that is reused by other parts of the page in a template-like fashion
    - creating an offscrren canvas as adrawing buffer. 
[MDN HTMLElement.hidden](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/hidden)
- Schema.org, RDF, JSON-LD 등의 메타 데이터를 활용합니다.
    - Schema.org
    - RDF
    - JSON-LD
- WAI-ARIA : 웹 페이지의 Accessibility를 높이는 방법을 정의하는 W3C 기술 사양을 활용합니다. 

가장 이상적인 해결책은 WAI-ARIA이고, absolute를 활용한 위치 지정 접근 방법이 가장 손쉽고, 대부분의 요소에 대해서도 이용할 수 있습니다.