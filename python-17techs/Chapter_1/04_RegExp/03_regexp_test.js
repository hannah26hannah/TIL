// regexp.test 패턴과 일치하는 문자열이 하나라도 있는 경우, 메서드 호출 시 true 그렇지 않으면 false 반환

let str = "I love JavaScript";
let regexp = /LOVE/i;
console.log(regexp.test(str)); // true
