const phone_str = "+7(903)-123-45-67";

let regexp = /\d/;
console.log(phone_str.match(regexp)); // [ '7', index: 1, input: '+7(903)-123-45-67', groups: undefined ]

// add g flag
regexp = /\d/g;
console.log(phone_str.match(regexp)); // [ '7', '9', '0', '3', '1', '2', '3', '4', '5', '6', '7' ]
console.log(phone_str.match(regexp).join("")); // 79031234567

// 일반 기호와 문자 클래스의 혼합 사용
let str = "Is there CSS4?";
regexp = /CSS\d/;
console.log(str.match(regexp)); // [ 'CSS4', index: 9, input: 'Is there CSS4?', groups: undefined ]

// 여러 개의 문자 클래스 활용
console.log("I Love HTML5!".match(/\s\w\w\w\w\d/)); // [ ' HTML5', index: 6, input: 'I Love HTML5!', groups: undefined ]

// non-character class
console.log(phone_str.match(/\d/g).join("")); // 79031234567

// 위 방법을 더 짧게 할 수 있는 방법은, \D로 숫자가 아닌 문자를 찾아 문자열에서 제거하는 방법이다. 
console.log(phone_str.replace(/\D/g, "")); // 79031234567
