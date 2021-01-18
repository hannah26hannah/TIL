# TypeScript Usage in Vue component

타입스크립트를 Vue 컴포넌트에 적용하는 방법에는 두 가지가 있다. `Vue.extend`를 이용해서 객체로 만드는 방법 그리고 `Class`로 만드는 방법이 있다.

## 1. `Vue.extend`를 이용해서 컴포넌트를 정의하는 방법

이 방법은 타입스크립트를 사용하지 않았을 때의 컴포넌트와 거의 비슷하다.

기존 자바스크립트에서의 Vue 컴포넌트 정의 방법처럼 컴포넌트 생성 옵션 객체로 컴포넌트를 정의한다. 다만, 타입이 선언된 `Vue.extend`를 사용한다.

## 2. `Class`를 이용해 컴포넌트를 정의하는 방법

```tsx
import { Vue, Component } from "vue-property-decorator";
```

클래스 스타일 컴포넌트를 좀 더 편하게 작성하기 위해 `vue-property-decorator`를 사용한다.

- @Component 외에 클래스 내부에
- [@Prop](#prop)
- [@Watch](#watch)
- [@Event](#event)
- [@Emit](#emit)
- [@Model](#model)
- [@Inject](#inject)
- [@Provide](#provide)

  위 목록의 Decorator를 제공한다.

### @Prop()

```tsx
@Prop(options: (PropOptions | Constructor[] | Constructor) = {}) decorator
```

```tsx
import { Vue, Component, Prop } from "vue-property-decorator";

@Component
export default class Sample extends Vue {
  @Prop(Number) propA!: number;
  @Prop({ default: "default value" }) propB!: string;
  @Prop([String, Boolean]) propC!: string | boolean;
}
```

위 형식을 취한다.

위 코드는 즉 아래와 동일하다.

```tsx
export default {
  props: {
    propA: {
      type: Number,
    },
    propB: {
      default: "default value",
    },
    propC: {
      type: [String, Boolean],
    },
  },
};
```

default 옵션을 사용해 기본값을 지정할 수도 있다.

```tsx
// views/Home.vue

<template>
    <div class="home">
        <Sample msg="This is Sample" />
    </div>
</template>

<script lang="ts">
import { Vue, Component } from "vue-property-decorator";
import { Sample } from "@/components/Sample.vue";

@Components({
    components: {
        Sample
    }
})

export default class Home extends Vue {}
</script>

// src/components/Sample.vue

<template>
    <div class="hello">{{ msg }}</div>
</template>

<script lang="ts">
import { Vue, Component, Prop } from "vue-property-decorator";

@Component
export default class Sample extends Vue {
    @Prop() private msg!: string;
}
</script>
```

### @Emit()

Emit decorator는 상위 컴포넌트에서 하위 컴포넌트로 이벤트를 바인딩할 때 주로 사용한다.

```tsx
@Emit(event?:string)
```

Emit 하고자 하는 Event 명을 string 형식으로 넣어 선언해준다.

```tsx
@Emit('change')
private onChange(value: string) {}
```

만일, 'change'처럼 emit되는 이벤트명을 넣지 않을 경우, 함수 명을 이벤트 명으로 사용한다.
이때, 이벤트명을 넣지 않아 자동으로 이벤트 emit이 선언된 경우에는 camelCase의 함수명이 cebab-case 함수명으로 적용된다.
i.g. onChange -> on-change

```tsx
// views/Home.vue
<template>
    <div class="home">
        <Sample msg="This is Sample"
        @onClick="handleClick" />
    </div>
</template>
<script lang="ts">
import { Vue, Component } from "vue-property-decorator";
import { Sample } from "@/components/Sample.vue";

@Components({
    components: {
        Sample
    }
})
export default class Home extends Vue {
    private handleClick() {
        console.log('click');
    }
}
</script>

// src/components/Sample.vue
<template>
    <div class="hello">{{ msg }}
        <button @click="onClick">클릭</button>
    </div>
</template>
<script lang="ts">
import { Vue, Component, Prop } from "vue-property-decorator";

@Component
export default class Sample extends Vue {
    @Prop() private msg!: string;
    @Emit('onClick')
    private onClick() {
        // 이 onClick() 함수가 실행되면 상위 클래스로 onClick 이벤트를 Emit되고, handleClick event를 trigger 해 로그를 찍는다.
    }
}
</script>
```

Event Emit과 더불어 데이터를 함께 전달하고자 할 때는, 코드를 아래처럼 개선해줄 수 있다.

```tsx
// views/Home.vue
<template>
    <div class="home">
        <Sample msg="This is Sample"
        @onClick="HandleClick" />
    </div>
</template>
<script lang="ts">
import { Vue, Component } from "vue-property-decorator";
import { Sample } from "@/components/Sample.vue";

@Components({
    components: {
        Sample
    }
})
export default class Home extends Vue {
    private handleClick(message: string) {
        console.log(message);
    }
}
</script>

// src/components/Sample.vue
<template>
    <div class="hello">{{ msg }}
        <button @click="(event) => onClick('클릭 이벤트 발생')">클릭</button>
    </div>
</template>
<script lang="ts">
import { Vue, Component, Prop } from "vue-property-decorator";

@Component
export default class Sample extends Vue {
    @Prop() private msg!: string;
    @Emit('onClick')
    private onClick(message: string) {
        // 이 onClick() 함수의 인자에 전달하고자 하는 데이터의 타입을 적어준다.
    }
}
</script>
```

### @Model()

`@Prop` Decorator와 다르게 양방향 데이터 바인딩을 위한 Decorator.

```tsx
@Model(event?: string, options: (PropOptions) | Constructor[] | Constructor) = {}) decorator
```

선언은 아래와 같이 한다.

```
import { Vue, Component, Model } from "vue-property-decorator"

@Component
export default class Sample extends Vue {
    @Model('change', { type: Boolean}) checked!: boolean
}
```

위는 아래와 동일하다.

```tsx
export default {
  model: {
    prop: "checked",
    event: "change",
  },
  props: {
    checked: {
      type: Boolean,
    },
  },
};
```

@Model을 실제 샘플 코드에 적용해보면 아래와 같다.

```tsx
// views/Home.vue
<template>
    <div class="home">
        {{ count }}
        <Sample v-model="count" />
    </div>
</template>
<script lang="ts">
import { Vue, Component, Watch } from "vue-property-decorator";
import { Sample } from "@/components/Sample.vue";

@Components({
    components: {
        Sample
    }
})
export default class Home extends Vue {
    private count: number = 0;
}
</script>

// src/components/Sample.vue
<template>
    <div>
        <button @click="(event) => onClick(count+1)">Add</button>
    </div>
</template>
<script lang="ts">
import { Vue, Component, Prop, Emit, Model } from "vue-property-decorator";

@Component
export default class Sample extends Vue {
    @Model('change', { type: Number})
    private count!:number;
    @Emit('change')
    private onChange(count: number) {}
    // count 변수는 @Model 데코레이터와 선언되어, 버튼 클릭 시 count 변수에 1이 더해지도록, change event는 emit된다.
}
</script>
```

### @Watch()

값의 변경에 따라 선언한 함수를 실행하도록 한다.

```tsx
@Watch('count')
onChangeCount(val: number, oldVal: number) {
    // function
}
```

이전 Home.vue 파일에서 count 변수의 값이 변경될 때마다 log를 출력해보자.

```tsx
@Watch('count')
private onChangeCount(val: number, oldVal: number) {
    console.log(`${oldVal} -> ${val}`);
}

```

### @Inject()

### @Provide()

위 두 Decorator는 고급 플러그인/컴포넌트 라이브러리에서 주로 사용되며, 일반 애플리케이션 코드에서는 사용 빈도가 낮음.

---

# 참고

- [1](https://withseungryu.tistory.com/45)
- [2](https://blog2.deliwind.com/20181109/frontend-vue-typescript-2/)
