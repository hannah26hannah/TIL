# About `this` keyword

실행 컨텍스트

브라우저 상에서 `this`를 출력해보면 `Window`가 나온다. strict 모드일 경우 undefined이다.
만일

```js
let user = {
  name: "John",
  age: 30,
};

user.sayHi = function () {
  alert("hi");
};
```

자바스크립트에서는 객체의 프로퍼티에 함수를 할당해서 객체가 할 수 있는 일을 부여한다. user.sayHi라는 객체 프로퍼티에 함수 표현식으로 만든 함수를 할당해보자. 이렇게 객체 프로퍼티에 할당된 함수를 우리는 '메서드'라고 부른다. 위 경우에는 객체 user에 할당된 sayHi가 메서드라 할 수 있다.

물론 이미 정의된 함수를 사용해 만들 수도 있다.

```js
let user = {
  name: "hannah",
  age: 28,
};

function sayHello() {
  console.log("hello");
}
// 선언된 함수를 메서드로 등록한다.
user.sayHi = sayHello;
user.sayHi(); // hello
```

이렇듯 객체를 사용해 객체를 표현하는 방식을 객체 지향 프로그래밍이라고 부른다. OOP는 그 자체만으로 학문의 분야를 만드는 중요한 주제이다. 올바른 개체를 선택하는 방법, 개체 사이의 상호작용을 나타내는 방법 등에 관한 의사 결정은 객체 지향 설계를 기반으로 이뤄진다. 관련 추천 도서로는 에릭 감마의 GoF의 디자인 패턴, 그래디 부치의 UML을 활용한 객체지향 분석 설계 등이 있다.

객체 리터럴 안에 메서드 선언 시 사용할 수 있는 단축 구문도 있다.

```js
// 아래 두 객체는 동일하게 동작한다.
user = {
  sayHi: function () {
    alert("hello");
  },
};

user = {
  sayHi() {
    alert("hi");
  },
};
// 단축 구문이 훨씬 더 깔끔하다. 하지만, 일반적인 방법과 단축 구문이 100% 동일하다고 볼 수는 없다. 객체 상속과 관련된 미묘한 차이가 존재하는데, 지금으로선 이 차이가 중요하진 않다.
```

메서드와 `this`
메서드는 객체에 저장된 정보에 접근할 수 있어야 제 역할을 할 수 있다. 모든 메서드가 그런 건 아니지만, 대부분의 메서드가 객체 프로퍼티 값을 활용한다.

user.sayHi()의 내부 코드에서 객체 user에 저장된 이름(name)을 이용해 인사말을 만들고자 한다면 객체 내부의 프로퍼티를 사용한다 할 수 있다.

이때, 메서드 내부에서 this 키워드로 객체에 접근하게 되는 것이다.

이때 this는 객체를 나타낸다. 정확히 말하자면 메서드를 호출할 때 사용된 객체를 말한다.

```js
let user = {
  name: "hannah",
  age: 28,
  sayHi() {
    alert(`${this.name}, hi!`);
  },
};
user.sayHi(); // hannah, hi!
```

user.sayHi()가 실행되는 동안에 this는 user를 나타낸다. this를 사용하지 않고 외부 변수를 참조해 객체에 접근하는 것도 가능하다.

```js
let user = {
  name: "John",
  age: 30,
  sayHi() {
    alert(`${user.name}, Hello!`);
  },
};
```

하지만 이렇게 외부 변수를 사용해서 객체를 참조하면, 예상하지 못한 에러가 발생할 수 있는데, user를 복사해서 다른 변수에 할당하고(admin = user) user에는 전혀 다른 값으로 덮어씌웠다고 하면, sayHi()는 원치 않는 값, 즉 null 값을 참조하게 될 것이다.

this.name으로 인수를 받았다면, 에러가 발생하지 않았을 것이다.

자바스크립트의 this는 다른프로그래밍 언어에서의 this와 동작이 다르다. 자바스크립트는 모든 함수에 this를 사용할 수가 있다.

그렇다면 다른 프로그래밍 언어에서는 this 사용이 어떻게 이뤄지는 것일까?

```js
function sayHi() {
  console.log(this.name);
}
```

이렇게 코드를 작성해도 문법 에러가 발생하지 않는다.
this 값은 런타임에 결정된다. 컨텍스트에 따라 달라질 것이다.
동일 함수라도 다른 객체에서 호출한다면, this가 참조하는 값이 달라질 것이다.

```js
let user = {
  name: "John",
};
let admin = {
  name: "Admin",
};

function sayHi() {
  alert(this.name);
}

user.f = sayHi;
admin.f = sayHi;
// 별개의 객체에서 동일한 함수를 사용함.

// this는 점 앞의 객체를 참조하기 때문에, this 값이 달라진다.
user.f(); // John (this == user)
admin.f(); // Admin (this == admin)

admin["f"](); // Admin (점과 대괄호는 동일하게 동작함)
```

obj.f()를 호출한 것이라면 this는 f를 호출하는 동안의 obj입니다.

만일 객체가 없을 때 sayHi() 함수를 호출한다면 어떻게 될까요? 이때 this는 undefined입니다.

```js
function sayHi() {
  alert(this);
}
sayHi(); // undefined
```

이런 코드를 엄격 모드에서 실행하면 this에는 undefined가 할당됩니다. 만일 this.name 같이 undefined의 프로퍼티에 접근하려고 한다면 에러가 발생할 것입니다. 그런데 엄격 모드가 아니면 this는 전역 객체를 참조하려고 할 것입니다. 브라우저 환경에서는 window라는 전역 객체를 참조합니다.
사실, 이런 동작 차이는 ES5에서 use strict가 도입된 배경이기도 합니다.
이런 식으로 작성되는코드는대게 실수로 작성된 경우가 많습니다.함수 본문에 this가 사용되었다면, 객체 컨텍스트 내에서 함수를 호출한 것이라고 예상하면 됩니다.

다른 언어를 사용하다 자바스크립트로 넘어온 개발자는 this를 혼동하기 쉽습니다. this는 항상 메서드가 정의된 객체를 참조할 것이라고 착각하기 때문입니다. 이런 개념을 bound this라고 합니다.
하지만, 자바스크립트는 런타임에 의해 결정됩니다. 메서드가 어디에 정의되었는지는 무관하게 this는 점 앞의 객체가 무엇인지에 따라 결정됩니다. 이런 경우 pros와 cons가 있는데, 유연하긴 하지만, 실수를 일으키기 쉽습니다.

this가 없는 화살표 함수.
화살표 함수는 일반 함수랑 달리 '고유한' this를 가지진 않습니다. 만일 화살표 함수에서 this를 참조하고자 한다면, 화살표 함수가 아닌 '평범한' 외부 함수에서 this를 가지고 오려고 할 것입니다.

아래 예시에서는 arrow() 함수의 this는 외부 함수인 user.sayHi()의 this가 될 것입니다.

```js
let user {
    firstName: '보라',
    sayHi() {
        let arrow = () => alert(this.firstName);
        arrow();
    }
}
user.sayHi();// 보라
```

별개의 this가 만들어지는 건 원치 않고, 외부 컨텍스트에 있는 this를 이용하고 싶을 경우 화살표 함수가 유용합니다.

즉, 객체 프로퍼티에 저장된 함수는 우리는 '메서드'라고 부르고,
object.doSomething()은 객체를 '행동'할 수 있게 하고
메서드는 this로 객체를 참조한다.
this는 런타임에 결정된다.
함수 선언 시 this 사용할 수 있지만, 함수 호출 전까지는 this는 값이 할당되지 않는다.
함수는 복사되어 객체 간전달될 수 있다.
함수를 객체프로퍼티에 저장해 object.method() 같이 메서드 형태로 호출하면 this는 objct를 참조한다.

화살표 함수가 독특한 이유는 자신만의 this를 가지지 않기 때문이다. 만일 화살표 함수 내부에서 this를 사용한다면, 외부에서 this를 가지고 온다.

quiz
객체 리터럴에서 this 사용하기

```js
function makeuser() {
  return {
    name: "hannah",
    ref: this,
  };
}
let user = makeUser();

alert(user.ref.name);

// 에러가 발생한다.
```

this 값을 설정해줄 때 객체 정의가 사용되지 않기 때문입니다. this 값은 호출 시점에 결정이 됩니다. 위 코드에서는 makeUser() 내 this는 undefined이 됩니다. 메서드로 호출된 것이 아니라 함수로서 호출된 것이기 때문입니다. 그래서 this 값은 전체 함수가 됩니다. 코드 블록과 객체 리터럴은 여기서 영향을 주지 않습니다.
따라서 ref: this는 함수의 현재 this 값을 가져옵니다.
this의 값이 undefined가 되도록 함수를 다시 작성하면 아래와 같습니다.

```js
function makeUser() {
  return this; // 이번에는 객체리터럴을 사용하지 않았습니다.
}
alert(makeUser().name); // cannot read property 'name' of undefined
```

에러가 발생하지 않게 하려면 코드를 아래처럼 수정해봅시다.

```js
function makeUser() {
  return {
    name: "John",
    age: 28,
    ref() {
      return this;
    },
  };
}
let user = makeuser();
console.log(user.ref().name); // 'John'
```

이렇게 하면, user.ref()가 메서드가 되고, this는 `.` 앞의 객체가 되기 때문에 에러가 발생하지 않는다.

계산기 만들기

```js
let calculator = {
  // value1: 0,
  // value1: 0,
  read() {
    this.value1 = +prompt("첫 번째 값을 입력해주세요", 0);
    this.value2 = +prompt("두 번째 값을 입력해주세요", 0);
  },
  sum() {
    return this.value1 + this.value1;
  },
  mul() {
    return this.value1 * this.value2;
  },
};
calculator.read();
alert(calculator.sum());
alert(calculator.mul());
```

prompt 앞에 +를 붙여서 `parseInt()` 함수가 해주는 기능과 동일한 결과를 낸다.
객체 내에서 값을 초기화하지 않아도 `this.a로 a 프로퍼티에 접근 동일

체이닝 문제

```js
let ladder = {
  step: 0,
  up() {
    this.step++;
    return { this };
  },
  down() {
    this.step--;
    return { this };
  },
  showStep() {
    console.log(this.step);
    return { this };
  },
};
// 메서드를 연이어 호출하고자 한다면 아래처럼 쓸 수 있다.

ladder.up();
ladder.up();
ladder.down();
ladder.showStep();

// 이때 up, down, showStep을 수정해 아래처럼 메서드 호출 체이닝이 가능하도록 해보자.

ladder.up().up().down().showStep();
```

```js
let ladder = {
  step: 0,
  up() {
    this.step++;
    return this;
  },
  down() {
    this.step--;
    return this;
  },
  showStep() {
    alert(this.step);
  },
};

ladder.up().up().down().showStep();
```

메서드가 호출될 때마다 객체 자기 자신을 반환하게 하면 됩니다.

체이닝이 길어질 땐 메서드 호출을 별도의 줄에 작성하면 가독성이 좋아진다.
