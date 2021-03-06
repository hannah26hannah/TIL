# 함수 선언문과 함수 표현식의 차이
- 함수는 여러 인자를 받아, 그 결과를 출력한다. 
- 파라미터의 개수와 인자의 개수가 일치하지 않아도 오류는 발생하지 않는다. 
- 만일 파라미터 1개가 정의된 함수를 호출할 때, 인자의 개수를 0개만 넣어 실행한다면, 이미 정의된 파라미터(매개변수)는 undefined라는 값을 갖게 된다. 이것은 변수는 초기화됐지만, 값이 할당되지 않았기 때문이다. 
- 자바스크립트에서는 함수도 객체이다. 
- 그러므로 다른 객체처럼 취급해 '넘기거나', '할당'이 가능하다. 
- 함수는 객체 프로퍼티에 할당할 수도 있다. 

```js
const o = {};
o.f = testFunc;
o.f(); // test!!
```

- 함수를 객체 배열 요소로 할당할 수 있다. 
```js
const arr = [1, 2, 3]
arr[1] = testFunc
arr[1](); // test!!
```
# 함수 호출 VS 함수 참조
함수 호출
- 함수 식별자 뒤 괄호`()`를 쓰면 함수 본문을 실행. 
- 함수 호출한 표현식은 반환값이 된다. 
- `testFUnc();`

함수 참조
- 함수 식별자 뒤 괄호를 생략하면 함수는 실행되지 않는다. 
- `testFunc`
- 만일 `const f = testFunc`처럼 함수를 변수에 할당한다면, `f()`처럼 함수를 호출할 수 있다. 

# 원시값 매개변수 vs 객체 매개변수
- 함수를 호출하면 함수 매개변수는 변수 자체가 아니라 그 값을 전달받는다. 
- 따라서 넘겨받은 원시값 매개변수를 함수 내에서 변경하더라도 함수 블럭 내 스코프 밖에서는 변경이 일어나지 않는다. 
- 하지만, 넘겨받은 매개변수가 *객체*이고, 이 객체 자체를 변경하면, 해당 객체는 함수 밖에서도 영향을 받는다. 
> 원시값은 불변하므로 수정 불가. 따라서 원시값을 담은 변수는 수정 가능하지만, 원시값 자체는 바뀌지 않는다. 반면 객체는 바뀔 수 있다. 

# 반환값과 undefined
- 함수는 어떤 타입의 값이라도 반환 가능하다. 
- JavaScript 함수는 반드시 return 값이 존재한다. 없을 경우 기본 반환값이 `undefined`가 반환된다. 
- JavaScript에는 `void` 타입이 없다. 
> 타입 스크립트에서 쓰는 'void'란? 일종의 패턴으로 개발자에게만 보이도록 하는 것인가. 반환값이 undefined인 경우 쓰도록?

# arguments 객체
- 함수 호출 시 넘겨진 실제 인자값을 가지는 객체. 함수가 실행되면, 그 안에는 arguments라는 특별한 지역변수가 자동으로 생성된다. arguments의 타입은 객체이다. 
- 자바스크립트 함수는 선언한 파라미터보다 더 많은 인자를 보낼 수도 있다. 이때 넘어온 인자를 arguments로 하나씩 접근할 수 있다. arguments는 array-like 형태를 띄지만, array는 아니다. 따라서 배열의 메서드는 사용 불가하다.
```js
function a() { console.log(arguments) };
a(1, 2, 3); // { '0': 1, '1': 2, '2': 3} 
```
- 자바스크립트의 가변인자를 받아 처리하는 함수를 만드는 상황에서 arguments 속성이 유용하게 쓰일 수 있다.  (=메서드에 넘겨받을 인자의 개수를 모를 때)
```js
function a() {
    if (arguments.length < 3) { // 인자의 개수가 중요한 경우
        console.log('err');
        return;
    }
    otherMethod(arguments[1]); // 다른 메서드에 가변 인자를 넘겨주고 있다. 
}
```

> arguments 남용 시 변경에 약한 코드가 될 수 있다. arguments를 함부러 수정하는 것은 권고되지 않는다. 수정이 된다하더라도 수정을 해서 해당 값을 직접 바꾸는 것을 지양해야 한다. 

# 함수 선언문과 함수 표현식의 차이
## Function Declaration
```js
function funcName() {
    // .. 
}
```
함수의 호출
```js
function printName(firstName) {
    var myname = 'Jeong';
    return myname+""+firstName;
}
```

## Function Expression
- 변수값에 함수 표현을 담아 놓은 형태
- 유연한 자바스크립트의 언어 특징을 활용한 선언 방식
- 익명 함수 표현식, 기명 함수 표현식으로 나눌 수 있다. 
- 일반적으로 함수 표현식이라 할 때는 '익명 함수 표현식'을 말한다. 
    - 익명 함수 표현식 : 함수 식별자가 없다.
    - 기명 함수 표현식 : 함수 식별자가 존재한다. 
- 함수 표현식은 클로저, 콜백으로 사용할 수 있다는 장점이 있다. 콜백으로 사용 시 다른 함수의 인자로 넘길 수 있다. 

```js
const test1 = function() {
    return '익명 함수 표현식'
}

const test2 = function test2() {
    return '기명 함수 표현식'
}
```

- 함수 선언문은 호이스팅의 영향을 받는다. 함수 표현식은 호이스팅의 영향을 받지 않는다. 
- 함수 선언문은 코드가 구현된 위치와 무관하게 JavaScript Parser에 의해 호이스팅의 영향으로 브라우저가 자바스크립트를 해석할 때 최상단으로 끌어올려진다. 
- 함수 표현식은 함수 선언문과 다르게 선언의 호출 순서에 따라서 정상적으로 함수가 실행되지 않을 수 있다. 
- 함수 표현식 Error Example
```js
// 정상
function printName(firstName) { // Function Declaration
    var inner = function() { // Function Expression
        return 'inner value';
    }

    var result = inner();
    console.log('my name is' + result);
}
printName(); 

// 오류 
function printNmae(firstName) { // Function Declaration
    console.log(inner); // 선언은 되었지만 값은 할당되지 않아 undefined
    var reuslt = inner(); // error
    console.log('name is' + result);

    var inner = function() { // Function Expression
        // ..
    }
}

printName(); // TypeError : inner is not a function 

// JS Parser 내부의 Hoisting 결과
function printName(firstName) {
    var inner; // Hoisting에 의해 변수값이 함수 스코프 내 최상단으로 끌어올려졌다. 
    console.log(inner); // 'undefined'
    var result = inner(); // Error
    console.log('name is' + result);
    inner = function() { // Function Declaration
        return 'inner value';
    }
}
printName(); // TypeError: inner is not a function
```
> `printName`이 실행되는 순간 호이스팅에 의해 `inner`는 `undefined`로 지정된다. 즉, 아직 함수로 인식되고 있지 않음을 의미한다. 
> 함수 표현식의 선언이 호출보다 아래에 있을 경우, Reference Error

# 호이스팅 우선순위
## 같은 이름의 var 변수 선언과 함수 선언에서의 호이스팅
- 변수 선언이 함수 선언보다 우선한다. 
- 값이 할당되어 있지 않은 변수의 경우 함수선언문이 변수를 overwriting한다. 

# Tips
- let/const의 활용
- 함수와 변수를 가급적 코드 상단부에 선언해 호이스팅으로 인한 스코프 꼬임을 방지한다. 

[참고 💬](https://gmlwjd9405.github.io/2019/04/22/javascript-hoisting.html)