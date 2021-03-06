# Closure

## Closure란?
> 독립적인 변수를 가리키는 함수이다. 클로저 안에 정의된 함수는 만들어진 환경을 기억한다. 

보통 함수 내 함수를 정의하고 사용할 경우 '클로저'라고 한다. 

Example 1
```js
function getClosure() {
    var text = 'variable 1';
    return function () { // getClosure() 함수는 함수를 반환한다. 
        return text;    // 반환된 함수는 내부에서 선언된 변수인 text를 참조한다.
    }                   // 여기서 반환된 함수를 '클로저'라 부른다. 
}
var closure = getClosure();
console.log(closure()); // 'variable 1'
```

Example 2
```js
var base = 'Hello, ';
function sayHelloTo(name) {
    var text = base + name;
    return function() {
        console.log(text)
    }
}
var hello1 = sayHelloTo('Jully')
var hello2 = sayHelloTo('Emilly')
var hello3 = sayHelloTo('Hannah')
hello1(); // Hello, Jully
hello2(); // Hello, Emilly
hello3(); // Hello, Hannah
```
- 여기서 변수 `text`는 동적으로 변화하는 것이 아닌, 호출한 `hello1()`, `hello2()`, `hello3()` 내에서 각기 다른 컨텍스트 위에 새로 생성된 변수로 보아야 한다. 

## Closure를 쓰는 이유
`prototype`을 통해 객체를 만들 때 Private variable에 대한 접근 권한 이슈가 있다. 

Example
```js
function Hello(name) {
    this._name = name;
}

Hello.prototype.say = function() {
    console.log('Hello, ' + this._name)
}

var hello1 = new Hello('Jully')
var hello2 = new Hello('Emilly')
var hello3 = new Hello('Hannah')

hello1.say(); // Hello, Jully
hello2.say(); // Hello, Emilly
hello3.say(); // Hello, Hannah
hello1._name = 'anonymous'; // (*)
hello1.say(); // Hello, anonymous
```

- 컨벤션에 따라 `_`를 사용함으로써 `Hello()` 함수의 `name` 변수는 private variable로 쓰고자 한다. 
- 하지만 실제로는 * 번째 줄에서 `_name` 변수에 대한 접근이 이루어졌다. 
- 이때 클로저를 통해 외부에서의 변수 접근을 제한할 수 있다. 

```js
function hello(name) {
    var _name = name;
    return function() {
        console.log('Hello, ' + _name)
    }
}

var hello1 = hello('cat');
var hello2 = hello('dog');
var hello3 = hello('butterfly');

hello1();
hello2();
hello3();
```

## 반복문 클로저
```js
var i;
for (i = 0; i < 10; i++) {
    setTimeout(function() {
        console.log(i)
    }, 100)   
}
// 10이 열 번 출력된다. 
```

0.1초 뒤에 호출되는 setTimeout. 그 사이 반복문이 모두 순회되어 i가 10이 된 상태이기 때문이다. 클로저를 통해 기대하는 결과를 만들 수 있다. 

```js
var i;
for (i = 0; i < 10; i++) {
    (function(j) {
        setTimeout(function() {
            console.log(j)
        }, 100)
    })(i);
}
```
즉시 실행 함수를 덧붙여 setTimeout의 익명 함수를 클로저로 만든다. i가 즉시 실행 함수 내부에 j라는 형태로 주입되고, 클로저에 의해 각기 다른 환경 속으로 들어간다. 하지만, i를 넘겨주지 않으면 참조할 i 값이 없으므로 글로벌 i 값을 참조해 기대하는 결과가 나오지 않는다. 

## 클로저의 성능
클로저는 컨텍스트를 가진다. 이를 위해 메모리가 소모된다. 클로저를 생성했지만, 참조하지 않으면 메모리 낭비이다. 클로저를 통해 내부 변수를 참조하는 동안 내부 변수가 차지하는 메모리를 GC가 회수 하지는 않으므로, 클로저 사용이 끝나면 참조를 제거하는 것이 좋다. 
```js
function hello(name) {
  var _name = name;
  return function() {
    console.log('Hello, ' + _name);
  };
}

var hello1 = hello('승민');
var hello2 = hello('현섭');
var hello3 = hello('유근');

hello1(); // 'Hello, 승민'
hello2(); // 'Hello, 현섭'
hello3(); // 'Hello, 유근'

// 여기서 메모리를 release 시키기 클로저의 참조를 제거해야 한다.
hello1 = null;
hello2 = null;
hello3 = null;
```