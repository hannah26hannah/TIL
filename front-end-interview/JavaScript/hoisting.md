# Hoisting

Hoisting은 '끌어올린다'라는 뜻으로, JavaScript의 변수 및 함수 선언문이 유효 스코프의 최상단으로 끌어올려지는 과정을 말한다. 실제 메모리 상에서의 변화는 아니며, JavaScript 내부적으로 처리되는 부분이다. 

- JavaScript Parser가 함수 실행 전 해당 함수를 검토한다. 
- 함수 내 존재하는 변수 및 함수 선언에 대한 정보를 기억하고 실행하는 것이며, 스코프는 `{}` 함수 블럭 내이다. 
- `var` 변수 '선언'과 함수 '선언문'에서만 호이스팅이 일어난다. 
- '할당'은 호이스팅의 적용 대상이 아니다. 
- `let`, `const` 변수 선언과 `함수 표현식`도 호이스팅의 적용 대상이 아니다. 
- 따라서 스코프 내 꼬임을 방지하기 위해서는 `const`와 `let`을 적절히 사용하고, 변수와 함수의 선언을 상단에 작성하도록 한다. 

```js
console.log("hello");
var myname = "Hannah"; 
let myname2 = "Jeong";

// JS Parser 내부의 Hoisting 결과 
var myname; // Declaration
console.log("hello"); 
myname = "Hannah"; // Assignment
let myname2 = "Jeong"; // Hoisting X
```

Example 2
- 함수 표현식(Function Expression)은 호이스팅되지 않는다. 

```js
foo();
foo2();

function foo() { // 함수 선언문
    console.log("Hello"); 
}

var foo2 = function () { // 함수 표현식
    console.log("Hello 2"); 
}

// JS Parser 내부의 Hoisting 결과
var foo2; // 함수 표현식의 변수값 Declaration
function foo() { // 함수 선언문
    // .... 
}
foo();
foo2(); // Error

foo2 = function() {
    // .. 
}
```
> 변수 `foo2`가 호이스팅되어 참조는 가능하지만, 값이 할당된 상태가 아니므로 `undefined` Error를 낼 것이다. 

Example 3
- 함수와 변수 선언문 중에서는 함수 선언문이 먼저이다. 
```js
func();
var func = function() { console.log('변수 호이스팅')}
function func() {
    console.log('함수 호이스팅')
}
// '함수 호이스팅'
```