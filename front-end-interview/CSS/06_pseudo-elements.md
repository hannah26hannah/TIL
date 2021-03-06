# pseudo-elements
- CSS Pseudo-elements는 선택자에 의해 추가되는 키워드. 
- 선택한 요소의 특정 부분을 스타일링할 수 있다. 
- 마크업을 수정하지 않고, (`::before`, `::after`), 
    - tooltip 삼각 화살표는 `:before`와 `:after`를 사용한다. 삼각형은 실제 DOM이 아닌 스타일의 일부로 간주되기 때문에 분리하는 것이 좋다.
- text-decoration을 위해 사용하거나 (`::first-line`, `:first-letter`) 
- 마크업에 요소를 추가할 수 있다. (`content: ...`와 결합)
- `.clearfix`에 사용되어 `clear: both`로 영역을 차지하지 않는 요소를 추가할 수 있다. 

## The value for content can be
- A string : `content: 'a string'`
- An Image : `content: url(/path/to/image.svg)` *This image can't be resized*
- Nothing : `content: ''` *useful for clearfix and inserting image as background-images(if set width and height, this can be even resize with background-size)*
- A counter : `content: counter(li)` *useful for styling lists until `:marker` comes along*

Note : *Can't insert HTML inside content*

## `::first-line` and `:first-letter`
`::first-line` allows you to style that first line of text. You could use it to make it larger or set it in small-caps as a stylistic choice. 
- This two psedo-element only works on block-level elements (when display is set to either `block, inline-block, table-caption, table-cell`). 
- If set on an inline element, nothing happens
- If you have both `::first-letter` and `::first-line` on an element, the first letter will inherit from the first line styles. but styles on the `::first-letter` will overwrite when styles conflict.
- 
```css
.test > h1::before {
        content: '●'
}
.test > h1::first-letter {
    color: red;
}
/* ::before content is not colored */
```

## `:` vs `::`
Every browser that supports the double colon (`::`) CSS3 syntax also supports just the(`:`) syntax, but IE 8 only supports the single-colon. 

`::` is the newer format intended to distinguish pseudo content from pseudo-selectors. 

Can I Use에서 :: selection CSS pseudo-element는 Opera Mini, iOS Safari를 제외하고 모두 지원됨 (2021-02-25)
[reference from caniuse `::`](https://www.caniuse.com/?search=%3A%3A)




# Reference
[Pseudo-elements에 대해 설명하고 이 요소가 무엇을 위해 사용되는지 설명하세요.](https://github.com/yangshun/front-end-interview-handbook/blob/master/contents/kr/css-questions.md)
[::before / ::after](https://css-tricks.com/almanac/selectors/a/after-and-before/)