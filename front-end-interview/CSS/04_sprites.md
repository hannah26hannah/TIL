# CSS sprites
## CSS 스프라이트는 무엇인가요? 그리고 당신이 페이지나 사이트에 구현하는 방법도 설명해주세요.

스프라이트 생성기를 사용해 여러 이미지를 하나로 묶어 적절한 CSS를 생성합니다. 각 이미지는 background-image, background-position, backgground-size 속성이 정의된 해당 CSS 클래스를 갖습니다. 
해당 이미지를 사용하기 위해 요소에 해당 클래스를 추가합니다. 

HTTP 프로토콜 통신 시 브라우저별로 요청을 병렬처리할 때 가능한 갯수가 제한적이므로 애플리케이션이 초기화될 때마다 리소스 요청을 자유롭게 할 수 없으니, 최대한 이 개수를 줄이기 위한 노력으로 모듈 번들링이 발달했고, CSS 스프라이트 기법도 생겨났습니다. 
CSS 스프라이트는 이미지를 개별적으로 요청하는 것이 아닌, 하나의 커다란 이미지 파일을 만들어 위치값으로 조정해 마스킹하는 방식을 의미합니다. 하지만 이는 HTTP/2의 등장으로 여러 이미지를 한 번에 로드하는 방식은 더 이상 크게 중요하지 않게 되었습니다. 


[참고자료](https://uiyoji-journal.tistory.com/25?category=901308)