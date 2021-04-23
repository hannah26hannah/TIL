# Positioning Related Questions

## `relative`, `fixed`, `absolute`, `static`, `sticky` 요소의 차이점은 무엇인가요?

`position` 속성은 문서 내에서 요소가 어떻게 위치 지어지는지 결정하는 속성으로, `top, right, bottom, left` 속성을 통해 최종적으로 배치될 위치가 결정됩니다.

- `static`은 기본 위치로, 평소 같이 페이지에 위치합니다. `top`, `right`, `bottom`, `left`, `z-index` 속성이 적용되지 않습니다.
- `relative`는 요소의 위치가 레이아웃을 변경하지 않고, 자체에 상대적으로 조정됩니다. 따라서 배치되지 않은 요소의 간격을 남겨둡니다.
  _absolute와 함께 쓰이며, 하위 요소와 상위 요소의 관계를 만들기 위한 선행 조건적인 요소입니다._
- `absolute`는 요소가 페이지의 평소 위치에서 제거되고, 가장 가까운 `static`이 아닌 부모 블록이 있는 경우, 지정된 위치에 배치됩니다. 그렇지 않을 경우 최상위 블록에 의존합니다. `absolute`로 배치된 박스는 `margin`을 가질 수 있고, 다른 `margin`과 충돌하지 않습니다. 이 요소는 다른 요소의 위치에 영향을 주지 않습니다.
  _relative 속성을 가진 가까운 요소와의 관계 안에서 위치를 갖도록 하는 속성입니다._
- `fixed` 요소는 페이지의 평소 위치에서 제거되고, viewport를 기준으로 지정된 위치에 배치되며, 스크롤할 때 이동하지 않습니다.
  _주변의 요소와의 관계와 무관하게, 현재 스크린에서의 절대적인 위치값을 갖도록 하는 속성입니다._
- `sticky`는 `relative`와 `fixed`의 하이브리드로, 요소는 지정된 임계점을 넘을 때까지 `relative` 위치로 처리되며, 특정 지점에서 `fixed`로 처리됩니다.

- [[CSS] position의 이해. static/relative/absolute/fixed 그리고 sticky.](https://uiyoji-journal.tistory.com/95)
