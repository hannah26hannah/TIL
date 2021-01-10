// Number
var num;
var integer = 6;
var float = 3.14;
var hex = 0xf00d; // 61453
var binary = 10; // 10
var octal = 484; // 484
var infinity = Infinity;
var nan = NaN;
// String
/* 작은 따옴표('), 큰 따옴표 (""), ES6 템플릿 문자열 지원 */
var str;
var red = 'Red';
var green = "Green";
var myColor = "My color is " + red;
var yourColor = 'Your color is ' + green;
// Array
// 문자열만 가지는 배열
var fruits = ['Apple', 'banana', 'Mango'];
// or
var AnotherFruits = ['Apple', 'banana', 'Mango'];
// 숫자만 가지는 배열
var oneToSeven = [1, 2, 3, 4, 5, 6, 7];
// or
var AnotherOneToSeven = [1, 2, 3, 4, 5, 6, 7];
// Union Type(다중 타입)의 '문자열과 숫자를 동시에 가지는 배열' 선언
var array = ['Apple', 1, 2, 'Banana', 3];
// or
var AnotherArray = ['Apple', 1, 2, 'Banana', 3];
// any
var someArr = [0, 1, {}, [], 'str', false];
var userArr = [
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
];
// // 특정 값으로 타입 대신해 작성 가능
// let theOtherArray: number[];
// array = [10];
// array.push(10);
// array.push(11); // Error - TS2345
