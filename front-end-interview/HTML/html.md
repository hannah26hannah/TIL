# data- 속성
DOM에 데이터를 저장할 수 있는 사용자 정의 데이터 속성. `data-` 다음에 오는 값이 데이터가 된다. 용도에 맞는 속성이나 요소가 없을 경우 사용하며 웹 페이지에서만 사용 가능한 값이다. 즉, 웹 페이지와 독립적인 소프트웨어가 이 속성을 사용해서는 안 된다. 

# DOCTYPE
Document Type의 약자이다. 문서의 HTML의 버전을 미리 선언해 웹 브라우저가 내용을 올바르게 표시하도록 하다. HTML 문서의 최상단에 지시자 `<!DOCTYPE>`를 추가하는 방식으로 선언되며, HTML5에서 권고하는 방식은 `<!DOCTYPE html>`으로 기존 XHTML, HTML 4.0대 버전에 비해 간소화되었다.

생략할 경우 호환모드로 브라우저가 렌더링된다. 이 경우에 브라우저마다 HTML 문서를 로드하는 방식이 달라 크로스 브라우징 이슈가 훨씬 잦다. 특이한 경우가 아니라면 DOCTYPE을 명시해 브라우저가 표준 모드로 렌더링할 수 있도록 하는 것이 좋다. 

# 표준 모드와 호환 모드
과거 웹 페이지는 넷스케이프와 익스플로러 버전이 따로 존재했으며 웹 표준이 없었다. 이후 W3C에서 웹 표준을 만든 이후 브라우저가 웹 사이트를 제대로 표현할 수 없게 되자 렌더링 시 표준 모드(Standards mode)와 호환 모드(Quirks mode)의 렌더링 옵션을 제공한다. 호환 모드로 렌더링할 경우에는 오래된 웹페이지들을 모던 브라우저에서도 정상적으로 렌더링하도록 하기 때문에 각 브라우저마다 다르게 보일 수 있다. 예를 들어, 익스플로러의 경우 호환 모드에서 박스 모델을 잘못 해석하지만, 나머지 브라우저는 그렇지 않다.

- [DOCTYPE, HTML, XHTML, 그리고 HTML5](https://uiyoji-journal.tistory.com/94?category=901309)

# 시맨틱 마크업
의미가 잘 전달될 수 있도록 작성한 문서를 의미한다. 시맨틱 마크업에서는 각 태그를 용도에 맞게 쓰는 것이 중요하다. 
- `<header>, <footer>` : 헤더와 푸터에 사용
- `<main>, <section>` : 메인 컨텐츠 영역에서 사용
- `<article>` : 독립적인 컨텐츠에 사용
- `<h1>` : 최상위 제목으로 사용
- `<ul>, <li>` : 순서가 없는 목록을 작성할 때 사용
- `<nav>` : 네비게이션 용도로 사용


동일한 스타일링을 위한 요소에 대해서는 이렇게 대응할 수 있다 : 예를 들어 `<strong>`과 `<b>` 태그가 있다. 동일하게 글자 색을 진하게 하지만, 후자의 경우 bold의 약어이므로 태그 자체가 스타일을 가진다. 하지만 전자는 그 안의 내용이 다른 내용보다 강조되어야 한다는 의미론적 성격을 띄므로, 스타일보다는 의미론에 무게를 두어 시맨틱 마크업을 할 수 있다.  

- 시맨틱 마크업은 검색엔진이 시맨틱 태그를 중요한 키워드로 간주하므로, 검색 엔진 최적화(SEO)에 유리하다. 
- 웹 접근성 측면에서도 스크린 리더에 읽힐 때 유용하다. 
- `<div>`나 `<span>` 태그를 중첩적으로 사용하는 것보다 코드 가독성이 높아진다. 


# 동일 출처 정책(SOP)

# 브라우저 렌더링 원리

## 홈페이지가 사용자에게 보이는 순서
- 브라우저의 주요 기능 : 사용자가 선택한 자원(HTML 문서, PDF나 이미지 또는 다른 형태도 가능)을 서버에 요청, 브라우저에 표시. 자원의 주소는 URI에 의해 정해진다. 
    - URI (Uniform Resource Identifier)
- 브라우저는 웹 표준화 기구인 W3C에서 정한 HTML과 CSS 명세에 따라 HTML을 파싱 후 렌더링한다. 

브라우저의 구성 요소
- UI : 주소 표시줄, 이전/다음 버튼, 북마크 메뉴 등 요청 페이지 섹션 제외한 나머지
- 브라우저 엔진 : UI와 렌더링 엔진 사이의 동작 제어
- 렌더링 엔진 : 요청 콘텐츠를 받아 브라우저에 표시. (HTML, XML 문서, 이미지, PDF 등 웹 자원 요청 발생 시 파싱 후 렌더링)
    - 파이어 폭스 (Gecko)
    - 사파리, 크롬 (Webkit)
- 통신 : 네트워크 호출에 사용됨. 플랫폼에 독립적인 인터페이스
- UI 백엔드 : OS의 UI 체계를 사용하는, 플랫폼에 명시되지 않은 일반적 인터페이스
- 자바스크립트 인터프리터 : JS 코드 해석과 실행
- 자료 저장소 : 쿠키를 포함한 모든 자원을 하드 디스크에 저장해야 한다. (HTML5 명세-브라우저에서 지원하는 '웹 데이터 베이스' 정의됨)
*크롬은 다른 브라우저와 달리 탭마다 별도의 렌더링 엔진 인스턴스를 유지한다. 고로 각 탭은 독립된 프로세스로 처리*

렌더링 엔진 동작 과정
1. DOM 트리 구축 위한 HTML 파싱
- 렌더링 엔진은 통신으로부터 요청한 문서의 내용을 얻는 것으로부터 시작. 
- 문서의 내용은 보통 8KB 단위로 전송. 
- 렌더링 엔진은 HTML 문서를 파싱하고, '콘텐츠 트리' 내부에서 태그를 DOM 노드로 변환.
- 외부 CSS 파일과 함께 포함된 스타일 요소 파싱

2. 렌더 트리 구축
- 스타일 정보 + HTML 표시 규칙은 '렌더 트리'라 부르는 또 다른 트리를 생성
- 렌더 트리는 색상, 면적 같은 '시각적 속성' 있는 사각형을 포함하며 정해진 순서로 화면에 표시된다.  

3. 렌더 트리 배치
- 각 노드가 화면의 정확한 위치에 표시되는 것

4. 렌더 트리 그리기
- UI 백엔드에서 렌더 트리의 각 노드를 가로지르며 형상을 만들어내는 그리기 과정이 전개

*모든 HTML을 파싱할 때까지 기다리지 않고, 배치와 그리기 과정을 시작한다. 네트워크로부터 나머지 내용이 전송되기를 기다리는 동시에 받은 내용의 일부를 먼저 화면에 표시한다*

파싱과 DOM 트리 구축
- Parsing : 브라우저가 코드를 이해하고 사용할 수 있는 구조로 변환하는 것. 
- Parsing result : 문서 구조를 나타내는 노드 트리 = Parsing tree or syntax tree

https://d2.naver.com/helloworld/59361