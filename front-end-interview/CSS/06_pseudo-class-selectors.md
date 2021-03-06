# pseudo-class-selectors
- outside of IE, these have great browser support. 

## Link-related pseudo class selectos
- `:link` : 아직 방문하지 않은 요소를 나타낸다. href 속성을 가진 `<a>, <area>, <link>` 중 방문하지 않은 모든 요소를 선택한다.
- `:visited` : 현재 브라우저에 의해 방문된 요소를 나타낸다. 
- `:hover` : 마우스 커서가 링크 위에 머무를 때 hover state가 된다. 
- `:active` : 클릭되거나 활성화된 요소. 버튼 스타일 링크가 'pressed' 된 것 같은 상태
    - `:link` - `:visited` - `:hover` - `:active` 순(LVHA)으로 링크를 디자인한다. `:active`를 다른 모든 규칙들보다 앞에 배치한다. 방문 여부 상관 없이 요소를 선택하고자 한다면, `:any-link`를 사용한다. 

## input & link related pseudo class selectors
- `:focus` : this will select links that are the current focus of the keyboard. This is not limited to links, but can be used on inputs and textareas as well. 
- `:target` : If you are at URL `www.yoursite.com/#home` then the selector `#home:target` will match.
- `:enabled` : selects inputs that are in the default state of enabled and ready to be used
- `:disabled` : selects inputs that have the disabled attribute. 
- `:checked` : selects checkboxes that are, wait for it, checked.
- `:indeterminate` : Selects radio buttons that are in the purgatory state of neither chosen or unchosen (like when a page loads with radio button choices but no default is set).
- `:required` : Selects inputs with the required attribute.
- `:optional` : Selects inputs that do not have the required attribute.
- `:read-only` / `:read-write` :  Selects elements based on a combination of readonly and disabled attriutes.

## Position/Number-based pseudo class selectors
- `:root` : this usually indicating `<html>`
- `:first-child` : selects the first element within a parent.
- `:last-child` : selects the last element within a parent.
- `nth-child()` : Selects elements based on a simple provided algebraic expression (e.g. “2n” or “4n-1”). Has the ability to do things like select even/odd elements, “every third”, “the first five”, and things like that. 
- `:nth-of-type()` : Works like :nth-child, but used in places where the elements at the same level are of different types. Like if inside a div you had a number of paragraphs and a number of images. You wanted to select all the odd images. :nth-child won’t work there, you’d use `div img:nth-of-type(odd)`. Particularly useful when working with definition lists and their alternating `<dt>` and `<dd>` elements.
    - [[SVG] JavaScript, CSS를 활용한 Path 기반 텍스트 애니메이션](https://uiyoji-journal.tistory.com/57)
- `:first-of-type` : Selects the first element of this type within any parent. So if you have two divs, each had within it a paragraph, image, paragraph, image. Then div img:first-of-type would select the first image inside the first div and the first image inside the second div.
- `:last-of-type` : Same as above, only would select the last image inside the first div and the last image inside the second div.
- `:nth-last-of-type()` – Works like :nth-of-type, but it counts up from the bottom instead of the top.
- `:nth-last-child()` – Works like :nth-child, but it counts up from the bottom instead of the top.
- `:only-of-type` – Selects only if the element is the only one of its kind within the current parent. 

## Relational pseudo class selectors
- `:not()` – Removes elements from an existing matched set that match the selector inside the parameter of `:not()`. So for example, all divs except those with a class of “music” = `div:not(.music)`. The spec says that `:not` selectors cannot be nested, but they can be chained. Some browsers (Firefox) also support comma-separated selectors as the selector parameter, although chaining them would be a far safter bet. Also useful in conjunction with attribute selectors, e.g. `input:not([disabled])`.
- `:empty` – Selects elements which contain no text and no child elements. Like: `<p></p>`

## Text-related pseudo class selectors / elements
- `::first-letter` – Selects the first letter of the text in the element. Typical use: dropcaps.
- `::first-line` – Selects the first line of text in the element. Typical use: setting the first sentence in small-caps as a typographical eye-catcher / lead-in.
- `:lang` – This pseudo selector is in the CSS3 spec but only implemented in IE 8+. Will match anything that either has or is a descendant of an element with a matching lang attribute. For example, :lang(fr) will match any paragraph, even without a lang attribute, if the parent body had lang="fr" as an attribute.

## Content-related pseudo “elements”
- `::before` – Is able to add content before a certain element. For example, adding an opening quote before a blockquote or perhaps an preceding image to set apart a particular paragraph.

- `::after`– Is able to add content after a certain element. For example, a closing quote to a blockquote. Also used commonly for the clearfix, where an empty space is added after the element which clears the float without any need for extra HTML markup.

# Reference
[:link](https://developer.mozilla.org/ko/docs/Web/CSS/:link)
[Meet the Pseudo Class Selectors ](https://css-tricks.com/pseudo-class-selectors/)