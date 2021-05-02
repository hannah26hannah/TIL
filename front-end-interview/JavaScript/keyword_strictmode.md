# strict mode란?

`strict mode`는 ES5에 추가된 키워드입니다. 그렇지 않은 기본 값을 '느슨한 모드(sloppy mode)'라 부르기도 합니다. 

엄격 모드를 지원하지 않는 Internet Explorer 10 버전 이하 같은 브라우저에서는 엄격 모드의 코드가 다른 방식으로 동작할 수 있습니다. 그 떄문에 테스트 없이 엄격 모드에 전적으로 의존하기는 어렵습니다.  엄격 모드의 코드와 느슨한 모드의 코드는 공존이 가능합니다. 

또, 해당 모드를 사용할 경우에는 자바스크립트가 묵인해오던 문법과 런타임 동작에서의 에러들이 그대로 보여집니다. 또 변수 사용을 단순화(simplifying) 해줍니다.

자바스크립트는 오류를 어느 정도 무시하고 넘어갈 수 있는 유연한(?) 언어인데, 그러다보니 코딩 당시에는 편할 수 있지만, 따로는 심각한 버그를 유발하기도 합니다. 사실 ES5 이전에는 기존의 문법을 변형하지 않고 새로운 기능을 추가하는 방식으로 버전이 발전해왔습니다. 하지만 초기에 만들어진 불완전한 문법이 그대로 남아 있거나 새로 추가될 버전에 대한 대비가 안 되어 있다는 점 때문에 ES5에서 `strict mode`가 도입되었고, 이를 사용할 경우에는 용인되어 오던 실수들을 에러로 변환해 바로 수정할 수 있도록 도와줍니다. 

더욱이 어떤 에러는 JavaScript 엔진의 최적화 작업을 어렵게 하는데, 엄격 모드의 코드는 이런 실수도 바로 잡을 수 있게 도와줍니다. 따라서 때로는 엄격 모드의 코드와 동일한 느슨한 모드의 코드를 비교했을 때 전자가 더 빨리 작동하기도 합니다. 
이렇게 사용할 경우에는 업데이트될 미래의 자바스크립트 버전과 대응도 용이하게 됩니다.

엄격 모드는 전체 스크립트 또는 부분 함수에서 적용 가능하지만, `{}`로 묶인 블럭 문에는 적용되지 않습니다. 

- eval 코드
- Function 코드
- 이벤트 핸들러 속성
- WindowTimers.setTimeout() 
위와 연관된 함수들에 전달된 문자열이 전체 스크립트입니다.

엄격모드를 전체 스크립트에 적용하기 위해서는 `"use strict"` 또는 `'use strict'`를 스크립트 최상단에 작성해줍니다. 해당 구문 이전에는 주석만 올 수 있고, 다른 내용이 들어갈 경우 엄격 모드 구문이 무시될 것입니다. 

함수에 적용할 떄는 아래처럼 작성해주면 됩니다. 
```js
function strict() {
  // 함수 레벨에서의 strict mode 문법
  "use strict";
  function nested() {
    return "And so am I";
  }
  return "Hi I'm a strict modefunction " + nested();
}
function noStrict() {
  return "I'm not strict'.";
}

console.log(strict()); // Hi I'm a strict modefunction And so am I
console.log(noStrict()); // I'm not strict'.

```

## 클래스, 모듈에서는 항상 엄격 모드로 실행됩니다.
모던한 문법인 클래스와 모듈에서는 굳이 `use strict`를 선언하지 않아도 항상 엄격 모드로 실행이 됩니다. 가령 클래스 생성자 내 코드 전체에는 자동으로 엄격 모드가 적용됩니다. 
모듈 역시 ECMAScript 2015에 소개된 문법으로, 엄격 모드를 적용할 수 있는 세 번째 방법입니다. JavaScript 모듈 전체 컨텐츠는 엄격 모드 시작을 위한 구문 `use strict` 가 없이도 자동으로 엄격모드가 됩니다.

```js
function strict() {
  // 모듈이므로 기본적으로 엄격합니다.
}
export default strict;
```


## 엄격 모드를 선언하지 않으면 전역 변수를 만들 수 없습니다.

가령 strict mode를 통해 해결할 수 있는 실수들을 살펴봅시다. 원래 변수는 정의되어야 사용이 가능합니다만, 예전에는 단순히 값을 할당하는 것만으로도 변수가 생성되어 전역 변수화되는 것이 가능했습니다. 지금도 여전히 하위 버전과의 호환성을 위해 사용 가능하지만, 이렇게 변수를 생성하는 것은 좋지 않은 습관입니다.

자바스크립트 시작이나 함수 시작에서 `use strict`를 선언하면, 아래처럼 선언 없이 전역 변수화할 경우 에러를 발생시킵니다.

```js
"use strict";
test = "hello"; // Uncaught ReferenceError: test is not defined at ...
```

# read only 객체 수정이 불가능합니다.

```js
'use strict'
var testObj = Object.defineProperties({}, {
    prop1: {
        value: 10,
        writable: false; // by default
    },
    prop2: {
        get: function() {
            // ..
        }
    }
});
testObj.prop1 = 20;
testObj.prop2 = 30;
// Uncaught TypeError: Cannot assign to read only property 'prop1' of object '#<Object>' at ..
```

## `get`으로 선언된 객체는 수정할 수 없습니다. (getter-only property 수정 불가능)

```js
"use strict";
var obj2 = {
  get x() {
    return 17;
  },
};
obj2.x = 5; // throws a TypeError Cannot set property x of #<Object> which has only a getter at ...
```

## extensible 특성이 false로 설정된 객체에 속성을 확장할 수 없습니다. (확장 불가 객체 확장 불가능)

```js
"use strict";
var testObj = new Object();
object.preventExtensions(testObj);
testObj.name = "Bob";

// Uncaught TypeError: Can't add property name, object is not extensible at ..
```

## `delete` 호출이 불가능합니다.

```js
"use strict";
var testvar = 15;
function testFunc() {}
delete testvar;
delete testFunc;

Object.defineProperty(testObj, "testvar", {
  value: 10,
  configurable: false,
});
delete testObj.testvar;
// Uncaught SyntaxError: Delete of an unqualified idenitifer in strict mode.
```

## 리터럴 객체는 동일한 이름의 property를 가질 수 없습니다. (단, ES6에서는 가능합니다.)

```js
"use strict";
var o = {
  p: 1,
  p: 2,
};
// syntax Error
```

## 함수의 동일한 매개 변수 이름을 선언하는 것이 불가능합니다.

```js
"use strict";
function testFunc(param1, param1) {
  return 1;
}
// Uncaught SyntaxError, Duplicate parameter name not allowed in this context.
```

## 8진수 숫자 리터럴 및 이스케이프 문자를 사용할 수 없습니다.

```js
"use strict";
var testoctal = 010;
var testescape = \010;
// Uncaught SyntaxError: Invalid or unexpected token
```

## primitive values의 속성 설정이 불가능합니다.

```js
(function () {
  "use strict";
  false.true = ""; // TypeError
  (14).sailing = "home"; // TypeError
  "with".you = "far away"; // TypeError
})();
// Uncaught TypeError: Cannot create property 'true' on boolean 'false'
```

strict 모드가 아닌 경우에는, 에러가 발생하진 않아도 해당 코드가 무시됩니다.

## 변수 사용의 명료화 (Simplify variable uses)

strict 모드는 변수 이름의 매핑을 단순화하는데, 대부분 컴파일러의 최적화는 변수의 매핑에 달려 있습니다. 자바스크립트 또한 변수의 매핑이 최적화의 크리티컬 이슈인데, strict mode를 사용하면 자바스크립트를 최적화할 수 있습니다.

## with를 사용할 수 없습니다.

```js
var foo = {
  name: "foo",
};
with (foo) {
  console.log(name);
}
```

with는 위와 같이 사용이 불가능합니다. 하지만 with 블록 안에 name은 전역 변수의 name인지, foo의 name인지 모호합니다. 그렇기 때문에 strict mode에서 with 사용이 불가능합니다.

```js
"use strict";
var x = 17;
with (obj) {
  x;
}
// Uncaught Syntax Error. Strict mode code my not include a with statement.
```

## eval 함수는 주변 스코프에 새로운 변수를 추가하지 않습니다.

## eval과 arguments 명료하 (Making eval and arguments simpler)

## 인자값을 수정함으로 arguments의 값이 수정되지 않습니다.

## callee를 지원하지 않습니다.

# securing JavaScript

strict mode를 사용하면, 보안에 강한 자바스크립트를 작성할 수 있습니다. 일부 웹 사이트에서는 사용자에게 자바스크립트 작성이 가능한 기능을 제공합니다. 이때 사용자가 작성한 자바스크립트는 부분적으로 접근을 금지해야 합니다. 접근을 막기 위해서 런타임에 체크를 한다면, 매우 비효율적인 코드가 될 것입니다. 이런 문제는 strict mode를 사용해 해결할 수 있습니다.

## `this`의 값이 `null` 또는 `undefined`인 경우 전역 객체로 변환하지 않습니다.

`this`의 결과가 `undefined`인 경우 `window` 객체로 변환하지 않고, `undefined`가 그대로 보여지게 됩니다.

```js
"use strict";
function fun() {
  return this;
}
console.log(fun()); // undefined
console.log(fun.call(2)); // 2
console.log(fun.apply(null)); // null
console.log(fun.call(undefined)); // undefined
ocnsole.log(fun.bind(true)()); // true
```

## calle, caller를 통해 stack 검색이 불가능합니다.

## arguments의 caller를 지원하지 않습니다.

# Paving the way for future ECMAScript versions

strict mode는 미래의 자바스크립트 버전 도입을 위해 몇 가지 제한 사항을 두었는데, 이 경우 추후에 도입될 자바스크립트 버전으로의 적용이 쉬워져 향후 업데이트될 자바스크립트 버전 대응이 용이합니다.

## 예약된 키워드의 이름으로 변수 또한 함수를 생성할 수 없습니다.

## 함수 선언은 스크립트나 함수의 최상위에서 해야 합니다.

strict mode에서는 함수는 최상위에 선언해야 합니다. 이후의 자바스크립트 버전은 최상위에서 선언하지 않은 함수는 다른 의미를 줄 수 있기 때문입니다.

좀 더 엄격하게 문법 검사를 하고자 할 때 유용하고, 실무에서 많이 사용합니다. 스크립트의 시작이나 함수 시작에서 `use strict`를 선언하면 strict mode로 코드를 작성할 수 있습니다.

# Reference

- [자바스크립트, 엄격모드(strict mode)](https://beomy.tistory.com/13)
- [엄격 모드](https://ko.javascript.info/strict-mode)
- [Strict Mode, MDN](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Strict_mode)