# area
이 태그는 이미지 맵(image-map)에서 하이퍼링크가 연결될 영역을 정의할 때 사용함. 

```html
<img src="/examples/images/img_imagemap.jpg" alt="진실 혹은 거짓" usemap="#vending" style="width:320px; height:240px">
<map name="vending">
    <area shape="rect" coords="210,200,70,130" alt="진실" href="https://ko.wikipedia.org/wiki/%EC%A7%84%EC%8B%A4">
    <area shape="rect" coords="90,60,180,130" alt="거짓" href="https://ko.wikipedia.org/wiki/%EA%B1%B0%EC%A7%93%EB%A7%90">
</map>
<p>표지판을 눌러보세요!!</p>
```

# Properties
|HTML5|name|value|description|
|---|---|---|---|
||alt|텍스트|영역(area)에 대한 대체 텍스트. `href` 속성이 설정되어야 사용 가능|
||coords|좌표|영역의 좌표를 명시함|
|HTML5|download|파일 이름|사용자가 하이퍼링크를 클릭할 때 해당 대상으로 연결되지 않고, 대신 해당 콘텐츠가 다운로드됨을 명시|
||href|URL|해당 영역에 연결된 하이퍼링크의 대상 URL을 명시|
|HTML5|hreflang|언어 코드|대상 URL의 언어를 명시함 *HTML5.1부터 지원 X*
|HTML5|media|미디어 쿼리|대상 URL이 최적화되는 미디어나 매체를 명시함|
|HTML5 Not supported|nohref|값|해당 영역이 연관된 어떠한 링크도 가지고 있지 않음을 명시함
|HTML5|rel|alternate, author, bookmark, help, license, next, nofollow, noreferrer, prefetch, prev, search, tag|현재 문서와 대상 URL 사이의 관계를 명시함|
||shape|default, rect, circle, poly|영역의 모양을 명시함|
||target|_blank, _parent, _self, _top, 프레임이름|영역 클릭 시 대상 URL 문서가 열릴 위치를 명시함|
|HTML5|type|미디어 타입|대상 URL의 미디어 타입을 명시. *HTML5.1부터 지원 X*|

# CSS default value
```css
area {
    display: none;
}
```
# Reference
[HTML `<area>` 태그](http://www.tcpschool.com/html-tags/area)