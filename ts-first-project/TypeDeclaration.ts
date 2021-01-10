// Number
let num: number;
let integer: number = 6;
let float: number = 3.14;
let hex: number = 0xf00d; // 61453
let binary: number = 0b1010; // 10
let octal: number = 0o744; // 484
let infinity: number = Infinity;
let nan: number = NaN;

// String
/* 작은 따옴표('), 큰 따옴표 (""), ES6 템플릿 문자열 지원 */
let str: string;
let red: string = 'Red';
let green: string = "Green";
let myColor: string = `My color is ${red}`;
let yourColor: string = 'Your color is ' + green;

// Array
// 문자열만 가지는 배열
let fruits: string[] = ['Apple', 'banana', 'Mango'];
// or
let AnotherFruits: Array<string> = ['Apple', 'banana', 'Mango'];

// 숫자만 가지는 배열
let oneToSeven: number[] = [1, 2, 3, 4, 5, 6, 7];
// or
let AnotherOneToSeven: Array<number> = [1, 2, 3, 4, 5, 6, 7];

// Union Type(다중 타입)의 '문자열과 숫자를 동시에 가지는 배열' 선언
let array: (string | number)[] = ['Apple', 1, 2, 'Banana', 3];
// or
let AnotherArray: Array<string | number> = ['Apple', 1, 2, 'Banana', 3];

// any
let someArr: any[] = [0, 1, {}, [], 'str', false];

// Interface or Custom-Type
interface User {
    name: string;
    age: number;
    isValid: boolean;
}
let userArr: User[] = [
    {
        name: 'Han',
        age: 22,
        isValid: false
    },
    {
        name: 'Sol',
        age: 52,
        isValid: false
    },
    {
        name: 'Heo',
        age: 12,
        isValid: true
    }
]

// // 특정 값으로 타입 대신해 작성 가능
// let theOtherArray: number[];
// array = [10];
// array.push(10);
// array.push(11); // Error - TS2345