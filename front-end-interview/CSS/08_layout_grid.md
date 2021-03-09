# Layout
## Grid
- 그리드 레이아웃은 반응형 웹 사이트 작업에 적합하다. 
- 가장 최신의 레이아웃 기술이며, 현대적인 웹앱에 최적화되어 있다. 
- 
### `grid/inline-grid`
```css
/* Block 특성의 Grid Container 정의 */
display: grid

/* Inline 특성의 Grid Container를 정의 */
display: inline-grid;
```
### `grid-template-rows`
- Grid Container를 정의한다. 정의된 컨테이너의 자식 요소는 자동으로 Grid Items로 정의된다. 그리드를 사용하기 위해서는 컨테이너에 필수로 작성해야 하는 속성. 
```css
grid-template-rows: 100px 200px; 
/* grid-template-rows: 1행 크기 2행 크기 ...; */
```
- 명시적 행의 크기를 정의한다. 
```css
    .container {
        grid-template-rows: [first] 100px [second] 200px [third];
    }
```
- 라인의 이름을 정의할 수도 있다. 
```css
.container {
    grid-template-rows: [row1-start] 100px [row1-end row2-start] 200px; 
}
```
- 라인에 중복된 이름을 지정할 수 있다. 그러나 각 라인은 행과 열의 개수대로 숫자(양수, 음수) 라인 이름이 자동으로 지정되어 꼭 필요하지 않다면 라인 이름을 정의할 필요가 없다.
- `fr(fraction)` 단위를 사용할 수 있다. -> 공간 비율
- `repeat()` 이라는 함수를 사용할 수 있다. 
### `grid-template-columns`
- 명시적 열 크기를 정의한다. 
- 동시에 라인 이름을 정의할 수 있다. 사용법은 `grid-template-rows`와 같다. 

```css
.container {
    display: grid;
    /* grid-template-columns: 1열 크기 2열 크기 ... */
    /* grid-template-columns: [선 이름] 1열 크기 [선 이름] 2열 크기 ...; */

    /* 만일 너비 1200px의 너비 12컬럼 그리드 템플릿을 정의한다면 */
    width: 1200px;
    grid-template-columns: repeat(12, 100px);
}
```
- `repeat()` 함수를 쓴다.
```css
.container {
    display: grid;
    width: 80%;
    grid-template-columns: repeat(12, 1fr);

    /* repeat() 함수는 2번째 인수를 반복하므로 아래처럼도 사용 가능하다. */
    grid-template-columns: repeat(2, 1fr 2fr 3fr);
    /* grid-template-columns: 1fr 2fr 3fr 1fr 2fr 3fr; */
}
```
- 컬럼의 크기를 `fr` 단위를 사용해 아래처럼 비율로 지정할 수도 있다. 컬럼은 비율에 맞게 출력이 되므로 컨테이너의 너비가 가변해도 열 크기를 수정할 필요가 없다. 

### `grid-template-areas`
```css
.container {
    display: grid;
    grid-template-rows: repeat(3, 100px)
    grid-template-columns: repeat(3, 1fr);
    grid-template-areas:
        "header header header"
        "main main aside"
        "footer footer footer"
}
header { grid-area: header; }
main { grid-area: main; }
aside { grid-area: aside; }
footer { grid-area: footer; }
```
- 지정된 그리드 영역 이름(`grid-area`)를 참조해 그리드 템플릿을 생성한다. 
- `grid-area`는 Grid Container가 아닌 Grid Item에 적용되는 속성이다. 
```css
.container {
    display: grid;
    grid-template-rows: repeat(4, 100px)
    grid-template-columns: repeat(3, 1fr);
    grid-template-areas:
        "header header header"
        "main . aside"
        "main . aside"
        "footer footer footer"
}
header { grid-area: header; }
main   { grid-area: main;   }
aside  { grid-area: aside;  }
footer { grid-area: footer; }
```
- `.` 를 사용하거나 명시적으로 `none`을 입력해 빈 영역을 정의할 수 있다. 

### `grid-template`
```css
.container {
    grid-template: <grid-template-rows>/<grid-template-columns>;
    grid-template: <grid-template-areas>;
}
```
- `grid-template-row`, `grid-template-columns`, `grid-template-areas`의 단축 속성이다.
```css
.container {
    display: grid;
    grid-template: 
        "header header header" 80px
        "main main aside" 350px
        "footer footer footer" 130px
        / 2fr 100px 1fr;
/* 위 내용은 아래처럼 해석된다. 
grid-template-rows: 80px 250px 130px;
grid-template-columns: 2fr 100px 1fr;
grid-area: ~
*/
}


header { grid-area: header; };
main { grid-area: main; };
aside { grid-area: aside; };
footer { grid-area: footer; };
```

### `row-gap(row-gap)`
```css
.container {
    row-gap: size;
}
```
- 각 행과 행 사이의 간격(Gutter)을 지정한다. 더 명확하게는 그리드의 선(Grid Line)의 크기를 지정한다고 볼 수 있따. 

### `column-gap(column-gap)`
```css
.container {
    column-gap: size;
}
```
### `gap`
```css
.container {
    gap: <row-gap> <column-gap>;
}
```
- `grid-gap`의 접두사 `grid`는 더 이상 사용되지 않으며, `gap`으로 교체되었으나, 일부 브라우저 지원을 위해 접두사 사용을 고려해볼 수 있다. 

## Responsive Grid
### `auto-fill`, `auto-fit`
```css
.container {
    grid-template-columns: repeat(auto-fill, minmax(120px, 1fr));
}
```
- 행/열 개수를 그리드 컨테이너 및 행/열 크기에 맞게 자동으로 조정한다.
- `repeat()` 함수와 같이 사용되며, 행/열 아이템의 개수가 명확할 필요가 없을 때 혹은 명확하지 않을 때 (반응형 그리드) 유용하다. 
- `auto-fill` 대신 `auto-fit` 사용 가능하다. 차이점은 그리드 컨테이너가 하나의 행/열에 모든 아이템을 수용하고 남는 공간이 있을 때 발생한다. `auto-fill`은 남는 공간을 그대로 유지하고, `auto-fit`은 남는 공간을 축소한다. 

## Terms Related Grid
### Track 
하나의 행이나 열
### Line
Gutter라고 하는 트랙과 트랙 사이의 간격
### Cell
아이템이 배치되는 최소 단위 영역 (Area)
### Area
아이템이 배치되는 하나 이상의 셀로 이루어진 영역

# Reference
- [Grid 101](https://heropy.blog/2019/08/17/css-grid/)
- [Grid Task](https://medium.com/chegg/css-grid-layout-in-examples-f85fd5428ba5) / `08_layout_grid_mission.html`