// start of the text

let str = "Mary had a little lamb";
console.log(/^Mary/.test(str)); // true

// end of the text
str = "its fleece was white as snow";
console.log(/snow$/.test(str)); // true

// 하지만 문자열 메서드인 startsWith나 endsWith를 사용해도 같은 결과를 얻을 수 있다. 정규 표현식은 복잡한 검사가 필요할 때 사용하면 좋다. 
// str.startsWith(searchString[, position]); returns boolean
str = 'To be, or not to be, that is the question.';
console.log(str.startsWith('To be')); // true
console.log(str.startsWith('not to be')); // false 
console.log(str.startsWith('not to be', 10)) // true

// str.endsWith(searchString[, length]); returns boolean
// length parameter의 default value는 str.length이며 문자열의 길이값은 문자열 전체 길이 안에서만 존재해야 한다. 

console.log(str.endsWith('question.')); // true
console.log(str.endsWith('to be')); // false
console.log(str.endsWith('to be', 19)); // 문자열을 'To be, or not to be,' 로 제한해 검색한다. true 

// 빈 문자열을 찾으면 a 를 삽입하는 예제
console.log("".replace(/^\s+$|^$/gi, "a")); // a 
