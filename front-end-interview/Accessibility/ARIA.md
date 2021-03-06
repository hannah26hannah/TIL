# ARIA
> 페이지를 새로 고침하지 않고도 콘텐츠를 Ajax 방식으로 갱신했을 때 전맹 시각장애인은 어떤 응답을 받을 수 있을까. 갱신 사실을 보조 기기가 즉시 알려줄 수 있으면 좋겠다. 비장애인이 화면에 등장하는 툴팁을 보면서 비밀번호를 바르게 생성하는 동안 시각장애인은 아무런 안내도 받지 못한 상태로 잘못된 비밀번호를 계속 입력할 수도 있다. 

접근가능한 리치 인터넷 애플리케이션(Accessible Rich Internet Application, ARIA)는 장애를 가진 사용자가 웹 컨텐츠와 웹 어플리케이션(특히 JavaScript로 개발한 경우)에 더 쉽게 접근하는 방법을 정의하는 여러 특성을 말한다. 

RIA에서 스크린리더 및 보조기기 등에서 접근성 및 상호 운용성을 향상시키기 위한 목적으로 탄생했고, 웹 애플리케이션에 Role, Property, State 정보를 추가해 이를 개선하도록 제공한다. 

# Role
UI에 포함된 특정 컴포넌트의 역할을 정리한다. 
## Abstract Roles
Roles의 분류 체계를 만들고 역할을 정의하기 위한 Roles이다. WAI-ARIA를 구축하는 기반이다. 
- command
- composite
- input
- landmark
- range
- roletype
- section
- sectionhead
- select
- structure
- widget
- window

## Widget Roles
독립형 사용자 인터페이스를 동작시키기 위한 목적의 Roles이다. 더 큰 Roles에 포함되거나 복합 위젯의 일부로 사용된다. 
### 독립형 widget Roles
- button
- checkbox
- gridcell
- link
- menuitem
- menuitemcheckbox
- menuitemradio
- option
- progressbar
- radio
- scrollbar
- searchbox
- separator
- slider
- spinbutton
- switch
- tab
- tabpanel
- textbox
- treeitem
### 복합형 widget Roles (단독으로 사용 X)
- combobox
- grid
- listbox
- menu
- menubar
- radiogroup
- tablist
- tree
- treegrid

> "tablist"를 활용한 탭 메뉴 예시 - 탭목록(tablist)과 본문(tabpanel)이 따로 나뉘어 있는 마크업 구조에서는 스크린 리더 등 보조 기기를 사용하는 이용자에게는 정보 접근이 어려울 수 있다. 이때 tab 관련 widget role을 사용해 좀 더 정확한 정보를 제공할 수 있다. 

```html
<div class='tab-wrap'>
    <ul role='tablist' class='list_tab'>
          <!-- 
            1. role="tab"을 사용하여 탭메뉴의 탭요소 역할 부여
            2. aria-controls="{ID}"를 사용하여 해당 탭의 본문과 연결
            3. aria-seleceted="{boolen}"를 사용하여 해당 탭이 선택유무 명시
            4. 초점을 받지 못하는 li요소에 tabindex="0"을 사용하여 초점을 받게함
        -->
        <li role="tab" tabindex="0" aria-selected="ture" aria-controls="section1" id="tab1">
            탭메뉴1</li>
        <li role="tab" tabindex="0" aria-selected="false" aria-controls="section2" id="tab2">
            탭메뉴2</li>
        <li role="tab" tabindex="0" aria-selected="false" aria-controls="section3" id="tab3">
            탭메뉴3</li>
    </ul>
     <!-- 탭메뉴 본문 -->
    <div class="tab_content">
        <!--
             1. role="tabpanel"을 사용하여 탭메뉴의 본문 역할 부여
             2. aria-labelledby="{ID}을 사용하여 탭메뉴와 본문 연결"
        -->
        <section role="tabpanel" id="section1" aria-labelledby="tab1">
            탭메뉴1의 본문
        </section>
        <section role="tabpanel" id="section2" aria-labelledby="tab2">
            탭메뉴2의 본문
        </section>
        <section role="tabpanel" id="section3" aria-labelledby="tab3">
            탭메뉴3의 본문
        </section>                              
    </div>
</div>
```
## Document Structure Roles
## Landmark Roles
이렇게 네 가지로 구분된다. 


ARIA의 많은 위젯은 HTML5로 통합된 경우가 있어, 이때 구현하려는 기능을 가진 요소가 존재한다면 시맨틱 HTML5 명세를 ARIA보다 선호하도록 한다. 

# 1. HTML을 의미있게 작성한다.
대부분의 WAI-ARIA 명세는 HTML 요소와 속성을 흉내낸다. 올바른 HTML을 사용하면, WAI-ARIA 사용을 최소화할 수 있다. 
```html
<!-- X -->
<a href="#" role="button">...</a>

<!-- O -->
<button type="button">...</button>
```
보조기기는 두 예를 모두 '버튼'으로 간주할 것이지만, 첫 번째의 예제는 브라우저는 문맥 메뉴를 통해 링크와 관련된 기능(새 탭에서 링크 열기, 링크 주소 복사 등)을 제공하므로 사용자를 혼란스럽게 합니다. 또, 첫 번째 예제에서 '버튼'이라는 설명을 제공받으므로, 보조기기 사용자는 '스페이스' 키를 눌러 버튼 기능을 사용하려고 시도할 수 있습니다. 하지만, `<a>` 요소는 '엔터' 키만으로 실행 가능합니다. 즉, `<button>` 요소는 엔터와 스페이스키로 실행할 수 있으므로, `<a>` 요소로부터 '버튼'이라는 설명을 들은 보조기기 사용자는 혼란스러울 것입니다. 

# 2. Tab 목록, Tab, Tab 패널
`(role="tablist|tab|tabpanel")`
탭은 스타일이 아닌, 현재 페이지 내용에 색인을 제공하는 구조(tablist, tab, tabpanel)을 의미합니다. 사이트 탐색 도구에 해당하는 요소는 `nav > h2 + ul` 또는 `aside > h2 + ul` 구조로 마크업하면 좋습니다. 
- role
- aria-selected
- aria-labelledby



# 참고

[MDN](https://developer.mozilla.org/ko/docs/Web/Accessibility/ARIA)
[레진 WAI-ARIA 가이드라인](https://tech.lezhin.com/2018/04/20/wai-aria)
[WAI-ARIA](https://www.biew.co.kr/entry/WAI-ARIA-%EC%9B%B9%ED%8D%BC%EB%B8%94%EB%A6%AC%EC%8B%B1)