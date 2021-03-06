# Z-index와 Stack Context

## `z-index`와 `stacking context`가 어떻게 형성되는지 설명하세요.
CSS의 `z-index` 속성은 겹치는 요소의 쌓이는 순서를 제어하며, `z-index`는 `position`이 `static`이 아닐 때 사용할 수 있습니다.

z-index 값이 없을 경우에는 DOM에 나타난 순서대로 요소가 쌓입니다. 즉, 동일한 계층에서 가장 아래의 것이 맨 위에 보이는 식입니다. 

`stack context`는 레이어를 포함하는 요소입니다. 지역 스택 컨텍스트 내에서 자식의 `z-index` 값은 문서 루트가 아닌 해당 요소를 기준으로 설정됩니다. 해당 컨텍스트 외부 레이어는 그 사이의 레이어에 올 수 없습니다. 요소 A의 하위 요소 B, B의 하위 요소 C가 있을 때, 아무리 요소 C의 z-index가 요소 A의 z-index보다 높아도, 요소 C는 요소 A보다 위에 올 수 없습니다. 

~~*페이지 위에 요소들은 HTML 문서에서 작성된 순서대로 레이어를 가지는데, 그 레이어의 순서를 지정해주는 속성입니다. z-index의 숫자가 높을수록 상위 레이어에 속합니다.*~~
