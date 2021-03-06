# `display`
- CSS에서 레이아웃을 제어하기 위한 가장 중요한 프로퍼티
- 대부분의 엘리먼트에 대한 기본값은 block이나 inline이다. 

## `block`
- 대표적으로 `p`, `form`이 있다. HTML5에 새로 추가된 엘리먼트로 `header`, `footer`, `section` 등이 있다. 

## `inline`
- 대표적으로 `a` 태그가 있다. 단락의 흐름을 방해하지 않은 채로 텍스트를 감싼다. 

## `none`
- JavaScript에서 엘리먼트를 실제로 삭제-재생성하지 않고도 엘리먼트를 보이고-감추는 데 흔히 사용된다. 
- `visibility`와 다르다. `display: none`을 설정 시, 엘리먼트는 페이지 상에서 마치 존재하지 않는 것처럼 렌더링된다. `visibility: hidden`으로 설정하면 엘리먼트는 감춰지겠지만, 해당 엘리먼트가 완전히 보이지는 않아도 여전히 페이지 상에서 공간을 차지한다. 


# Main Layout Tip
```css
 body {
    width: 100%;
    height: 100%;
    box-sizing: border-box;
}
main {
    width: 600px;
    margin: 0 auto;
    background-color: beige;
}
```
- 블록 레벨 엘리먼트의 `width`를 설정하면, 컨테이너 좌우 가장자리로 늘어나지 않게 지정할 수 있다. 그 후 좌우 `margin`을 위처럼 설정하면 해당 엘리먼트는 컨테이너 상에서 가로 중앙으로 오게 할 수 있다. 
- 이 Trick은 브라우저 창이 엘리먼트의 너비보다 좁을 때 페이지에 가로 스크롤바를 생성한다. 
- 해결 
    ```css
    main {
        max-width: 600px;
        margin: 10% auto;
        background-color: beige;
    }
    ```
    - `width` 대신 `max-width`를 쓴다. 브라우저가 작은 창을 처리하는 방식을 개선한다. 이는 사이트를 모바일 환경에서도 사용할 수 있게 만들 때도 중요하다. 넓은 범위의 브라우저에서 `max-width`를 지원한다.


# Box Model Tip
- 엘리먼트의 너비를 설정할 경우 해당 엘리먼트는 실제로 설정한 것 이상이 될 수 있다. 이는 엘리먼트의 테두리와 패딩 탓이다. 
- 이는 `box-sizing`이라는 새로운 CSS 프로퍼티를 통해 해결할 수 있다. 엘리먼트에 `box-sizing`을 추가하면 해당 엘리먼트의 패딩과 테두리가 더는 너비를 늘리지 않는다. 
```css
* {
  -webkit-box-sizing: border-box;
     -moz-box-sizing: border-box;
          box-sizing: border-box;
}
```
- 페이지 상의 모든 엘리먼트에 적용하는 코드이다. 

# Position Tip
- `position: relative`는 별도의 프로퍼티를 작성하지 않는한 기본값인 `position: static`과 동일하게 동작한다. 
- `position: fixed`는 viewport에 상대적으로 위치가 지정된다. 페이지가 스크롤되어도 늘 같은 곳에 위치한다. 
- 모바일 브라우저의 경우 고정 엘리먼트 지원이 불안정하다. 
- `position: absoulte`는 절대 위치가 지정된 엘리먼트가 기준으로 삼는 조상 엘리먼트가 없을 시에는 `document.body`를 기준으로 삼는다. 또한, 페이지 스크롤에 따라 움직인다. (여기서 위치가 지정된 엘리먼트란, `position: static`이 아닌 엘리먼트를 말한다.)
```css
.container {
    position: relative;
}
nav {
    position: absolute;
    left: 0;
    /* 위 코드는 float: left로 대체될 수 있다.  */
    width: 200px;
    
}

section {
    /* nav만큼의 공간을 마련하기 위해 section은 모두 오른쪽으로 200px 밀린다 */
    margin-left: 200px;
}
body {
    /* footer에 지정한 height만큼의 공간을 margin-bottom에 만든다. */
    margin-bottom: 200px;
}
footer {
    /* 스크롤 되어도 footer 영역은 계속 사라지지 않고 viewport 하단에 위치한다. */
    position: fixed;
    bottom: 0;
    left: 0;
    height: 70px;
    background-color: white;
    width: 100%;
}
```

# Float Tip
- 이미지 주위를 텍스트로 감싸기 위해 만들어진 속성이다.
```html
 <article>
        <div class='img'></div>
        <p>나랏말ᄊᆞ미 中듀ᇰ國귁에 달아 文문字ᄍᆞᆼ와로 서르 ..
        </p>
</article>
```
```css
.img {
    float: right;
    margin: 0 0 1em 1em;
    width: 200px;
    height: 200px;
    background-color: orange;
}
```
- `clear` 프로퍼티는 `float` 동작 방식을 제어하기 위해 중요하다. 
```html
<div class='box'></div>
<section>...</section>
```
- 실제로는 `<section>` 엘리먼트는 `<div>` 다음에 존재하지만, 보여질 때는 `<section>` 안의 텍스트가 `<div>` 주위에 떠 있는 모습을 띈다. 
```css
section { clear: left; }
```

- HTML을 작성한 순서대로 `<div>`에 영향을 받지 않도록 `<section>`를 아래로 내리고자 한다면, `clear: left;`를 지정해주면 된다. 

```html
<article class='clearFix'>
    <div class='img'></div>
    <p>나랏말ᄊᆞ미 中듀ᇰ國귁에 달아 文문字ᄍᆞᆼ와로 서르 ..
    </p>
</article>
```
- img와 p를 감싸는 article이 img를 채 다 감싸지 못할 때 article에 `overflow: auto`를 추가해준다.
```css
article {
    border: 1px solid blue;
}
.img {
    float: right;
    margin: 0;
    width: 200px;
    height: 200px;
    background-color: orange;
}
.clearFix {
    overflow: auto;
}
```

## 📜 Float의 작동 원리
- Float은 CSS 위치 지정 속성 중 하나로, `float` 속성이 적용된 엘리먼트는 페이지 흐름의 일부가 된다. `position: absolute`가 페이지 흐름에서 제외되는 것과 달리 다른 요소(가령 Floating 요소 주위로 흐르는 텍스트) 위치에 영향을 준다.
- Float은 블록 레벨 엘리먼트를 의도적으로 좌우 배치할 때 주로 사용한다. 하지만, float을 사용할 경우 float이 설정된 요소는 브라우저가 높이 값을 인지하지 못한다는 문제가 있어 이를 해결하기 위해 clear하는 다양한 방법이 존재한다. 이를 통해 해당 엘리먼트의 높이 값을 인지하기 위함이다. 

## 📜 Float을 Clear하는 방법과 해당 방법이 어울리는 상황은?
- CSS `clear` 속성은 엘리먼트가 플로팅 요소로부터 어떻게 moved/cleared 되어야 하는지, 즉 `float` 속성 해제에 대한 속성이다. 아래 값을 가진다. 
- `none` : 기본 값으로, clear를 설정하지 않은 것과 같다.
- `left` : 왼쪽으로 붙는 float 정렬을 취소한다.
- `right` : 오른쪽으로 붙는 float 정렬을 취소한다.
- `both` : 양측 모두 붙는 float 정렬을 취소한다.


1. float된 요소를 감싸는 컨테이너 태그에 의도적으로 높이 값을 지정한다. 하지만 반응형 레이아웃을 고려할 때, 자동 높이 값 설정을 사용하지 못한다. 
2. 또는 float된 요소를 감싸는 컨테이너 태그에 `overflow: hidden`을 적용해준다. 하지만, 해당 요소 안의 컨텐츠를 박스 외부로 표현할 방법은 없다. 또는 `overflow: auto`를 적용할 수도 있다. 이 경우에는 특정 브라우저에서 스크롤바가 표시되는 문제가 있다. 
3. float된 요소 다음 태그에 `clear:both`를 지정해준다. 단, 이 경우 clear 속성을 적용하는 요소에 대해서는 `margin-top`이 적용되지 않는다.
```html
<main class='container'>
    <img class='floating'></img>
    <div style='clear: both;'></div>
</div>
```
4. 가장 권장되는 방법으로, 컨테이너에 `:after`를 사용한 가상 선택자를 사용해 `float`를 제거한다.
```css
#container {
    content: "",
    display: block;
    clear: both;
}
```

# `%` Tip
- 특정 엘리먼트를 담는 블록에 상대적인 측정 단위. 
- 이미지 크기를 제한하는 데 `min-width, max-width`를 쓸 수 있다. 

# `%` width and media query Tip
- 문제 상황 : 위에서 만든 `nav`와 `section` 템플릿을 아래 CSS를 적용해 `float`으로 레이아웃을 수정했다. 창 너비가 줄어들면 `nav` 콘텐츠는 지저분해지는 문제가 있다. 

```html
<main class='container'>
    <nav>
        <ul>
            <li>포트폴리오</li>
            <li>시간</li>
            <li>방향</li>
            <li>연락처</li>
        </ul>
    </nav>
    <section>content1</section>
    <section>content1</section>
</main>
```

```css
.container {
    width: 100%;
    height: 100%;
}
nav {
    float: left;
    width: 25%;
}

section {
    margin-left: 25%;
    margin-bottom: 1rem;
}
```
- 개선 과제 : 이를 반응형으로 만들기 위해 미디어 쿼리를 사용한다. 메뉴를 사이드바에 두기에는 브라우저 창의 크기가 너무 작을 떄, 메뉴를 한 칼럼에 표시되도록 수정한다. 
```css
@media (max-width: 425px){ 
    nav li {
        display: inline
    }
}
@media (min-width: 426px) {
    nav {
        float: left;
        width: 25%;
    }
    section {
        margin-left: 25%;
    }
}
```

# multiple text column tip
```html
<section class='three'>...</section>
```
- 문제 상황 : 반응형으로 컬럼의 개수를 조절하기
```css
.three {
    padding: 1em;
    
    /* column-width가 지정되어야 column-count: auto;가 적용된다. column-width에 의해 automatically 적용되는 프로퍼티이므로 */
    column-count: auto;
    column-width: 8rem;
}

@media (max-width: 425px){ 
    .three {
        column-count: 2;
        column-gap: 1em;
    }
}

@media (min-width: 426px) {
    .three {
        column-count: 3;
        column-gap: 1em;
    }
}
```


# Referecne
[CSS Layout Basic](https://ko.learnlayout.com/)
[CSS float 해제를 위한 clear 방법](https://neul-carpediem.tistory.com/278)