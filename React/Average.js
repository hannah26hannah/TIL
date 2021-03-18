import React, { useCallback, useMemo, useRef, useState } from 'react';
import MyComponent from './MyComponent';

const getAverage = (numbers) => {
  console.log('평균값 계산 중 .. 💬');
  if (numbers.length === 0) return 0;

  const sum = numbers.reduce((a, b) => a + b);
  return sum / numbers.length;
};
const Average = () => {
  const [list, setList] = useState([]);
  const [number, setNumebr] = useState('');
  const inputEl = useRef(null);

  const onChange = useCallback((e) => {
    setNumebr(e.target.value);
  }, []); // 컴포넌트가 처음 렌더링될 때만 함수를 생성

  const onInsert = useCallback(
    (e) => {
      const nextList = list.concat(parseInt(number));
      setList(nextList);
      setNumebr('');
      inputEl.current.focus();
    },
    [number, list]
  ); // number 혹은 List가 바뀌었을 때만 함수 생성

  const avg = useMemo(() => getAverage(list), [list]);
  return (
    <div>
      <input value={number} onChange={onChange} ref={inputEl} />
      <button onClick={onInsert}>등록</button>
      <ul>
        {list.map((item, index) => (
          <li key={index}>{item}</li>
        ))}
      </ul>
      평균 : {avg}
      <MyComponent />
    </div>
  );
};

export default Average;
